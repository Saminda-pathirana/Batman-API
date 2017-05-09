from flask import g, request
from flask_restful import abort


def validate_access_by_endpoint():
    if request.endpoint not in ['stores']:
        abort(403, message="not allowed")
