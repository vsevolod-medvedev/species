import datetime


def serialize_ext(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError('%r is not JSON serializable' % obj)
