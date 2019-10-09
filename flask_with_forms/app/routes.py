from app import app, db
from app.forms import FeatureRequestForm, ClientFilter
from app.misc import refit_client_priorities, highest_priority
from app.models import Client, FeatureRequest
from flask import render_template, flash, redirect, url_for
from flask import send_from_directory

# serve from sub-domain, ie, '/somedir/'
SUBDIR = '/flaskapp'
# serve from top-level domain dir, ie '/'
SUBDIR = ''

links = [
    {"uri":"{}/".format(SUBDIR),
        "name":"Home"},
    {"uri":"{}/feature_request".format(SUBDIR),
        "name": "Create Feature Request"},
    {"uri":"{}/view_requests".format(SUBDIR),
        "name": "View Feature Requests"}
]

@app.route('{}/'.format(SUBDIR))
@app.route('{}/control_panel'.format(SUBDIR))
def control_panel():
    return render_template('control_panel.html', title=
        'Control Panel - Home', links=links,
        root_url=SUBDIR)

@app.route('{}/feature_request'.format(SUBDIR), methods=['GET', 'POST'])
def feature_request():
    form = FeatureRequestForm()
    if form.validate_on_submit():
        # clamp priority to one plus highest
        high = highest_priority(form.client.data)
        if form.priority.data >= high:
            form.priority.data = high + 1
        # if lower than top move the rest up
        refit_client_priorities(form.priority.data, form.client.data)
        # insert
        f = FeatureRequest(title=form.title.data,
            description=form.description.data,
            client_id=form.client.data,
            priority=form.priority.data,
            target_date=form.target_date.data,
            product_area=form.product_area.data)
        db.session.add(f)
        db.session.commit()
        client = db.session.query(Client).filter(
            Client.id==int(form.client.data)).first().name
        flash('"{}" feature created for "{}".'.
            format(form.title.data, client))
        return redirect(url_for('feature_request'))
    return render_template('feature_request.html', title=
        'Feature Request creation form', form=form, links=links,
        root_url=SUBDIR)

@app.route('{}/view_requests'.format(SUBDIR), methods=['GET', 'POST'])
def view_requests():
    form = ClientFilter()
    requests = FeatureRequest.query.order_by(
        FeatureRequest.client_id.asc()).order_by(
        FeatureRequest.priority.asc()).all()
    products=["","Policies","Billing","Claims","Reports"]
    processed = []
    for r in requests:
        o = {}
        o['target_date'] = r.target_date.strftime("%B %d, %Y")
        o['client'] = db.session.query(Client).filter(
            Client.id==r.client_id).first().name
        o['product_area'] = products[ int(r.product_area) ]
        o['priority'] = r.priority
        o['title'] = r.title
        o['description'] = r.description
        processed.append(o)
    fields=('client','priority','title','description','product_area',
        'target_date')
    return render_template('view_requests.html', title='View Requests',
        form=form, links=links, requests=processed, request_fields=fields,
        root_url=SUBDIR)

@app.route('{}/static/<path:path>'.format(SUBDIR))
def send_static(path):
    return send_from_directory('static', path)

