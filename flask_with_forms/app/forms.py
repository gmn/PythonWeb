
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField
from wtforms import DateField, SubmitField
from wtforms.validators import DataRequired, NoneOf, NumberRange

CLIENTS=[("0", "- select -"), ("1", "Client A"), ("2", "Client B"),
    ("3", "Client C")]
PRODUCT_AREAS=[("0", "- select -"), ("1", "Policies"), ("2", "Billing"),
    ("3", "Claims"), ("4", "Reports")]
CLIENT_FILTER=[(".request", "Showing All Clients"), (".A", "Client A"),
    (".B", "Client B"), (".C", "Client C")]

class FeatureRequestForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    client = SelectField('Client', coerce=str, choices=CLIENTS,
        validators=[NoneOf(["0"], message="Must select a client")])
    priority = IntegerField('Client Priority',
        validators=[NumberRange(min=1,
        message="Can't be less than 1. 1 is the highest priority.")])
    target_date = DateField('Target Date', format="%Y-%m-%d",
        id="datepicker")
    product_area = SelectField('Product Area', choices=PRODUCT_AREAS,
        validators=[NoneOf(["0"], message="Must select Product area")])
    submit = SubmitField('Create Feature Request')

class ClientFilter(FlaskForm):
    filter = SelectField("Filter by Client", choices=CLIENT_FILTER,
        id="client_filter", default=".request")

