import json


def resource_not_found(error):
    return json.dumps('Resource not found'), 404


def resource_internal_error(error):
    return json.dumps('Internal server error'), 500
