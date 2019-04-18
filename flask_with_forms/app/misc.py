
from app import db
from app.models import FeatureRequest

def refit_priorities_demo(new_priority, client_id):
    """ S will contain integer: 1 to N. n can be any positive integer > 0.
        In the event that N is less than or equal to the highest integer in S,
        then every int in S greater-than n will need to be remapped to one
        higher.
    """
    assert(n>=1)
    if len(S) == 0:
        S.append(n)
    elif n >= len(S):
        S.append(n)
    else:
        index = n-1
        S.append(S[-1]+1)
        for x in range(len(S)-1,index,-1):
            print('move {} to {}'.format(S[x-1],S[x]))
            S[x]=S[x-1]+1
        S[index]=n

def refit_client_priorities(new_priority, client_id):
    """
        Simply move all priorities up by one given a client and priority
    """
    for record in db.session.query(FeatureRequest).filter(
        FeatureRequest.client_id == client_id).filter(
        FeatureRequest.priority >= new_priority).order_by(
        FeatureRequest.priority.desc()).all():
        record.priority += 1
    db.session.commit()

def highest_priority(client_id):
    o = db.session.query(FeatureRequest).filter(
        FeatureRequest.client_id == client_id).order_by(
        FeatureRequest.priority.desc()).first()
    if o:
        return o.priority
    else:
        return 0
