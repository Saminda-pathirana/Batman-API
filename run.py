from flask import Flask, _request_ctx_stack, g, request, jsonify
import logging
from flask_restful import abort
from redis import Redis, RedisError, StrictRedis
from flask_cache import Cache
import jwt
import sys
from flask.ext.socketio import SocketIO

# from flask_swagger import swagger
from flask_restful_swagger_2 import Api

#: Import the list of common helpers
from common import request_field, request_header, exception_error_messages, validate_access_by_endpoint

#: Import the list of resources
from resources.queue import Queue

#: Import mysqlAlchemy instance
from common.mysqldb import db


class RedisHandler(logging.Handler):
    """Redis handler for logging"""
    def __init__(self, channel, conn, *args, **kwargs):
        """initialise channel and connection to Redis"""
        logging.Handler.__init__(self, *args, **kwargs)
        self.channel = channel
        self.redis_conn = conn

    def emit(self, record):
        """initialise channel and connection to Redis"""
        attributes = [
            'name', 'msg', 'levelname', 'funcName'
        ]
        record_dict = dict(
            (attr, getattr(record, attr)) for attr in attributes)
        ctx = _request_ctx_stack.top

        attributes = [
            'environ', 'path', 'endpoint', 'url_rule'
        ]
        if ctx is not None:
            record_dict['request'] = dict(
                (attr, getattr(ctx.request, attr)) for attr in attributes)
        try:
            self.redis_conn.publish(self.channel, record_dict)
        except RedisError:
            pass

app = Flask(__name__)
socketio = SocketIO(app)
app.config.from_object('config')
db.init_app(app)

errors = exception_error_messages()
api = Api(app, prefix='/v1', catch_all_404s=True, errors=errors, api_spec_url='/docs/swagger', base_path='/v1')

#: instantiate a redis connection and a logging handler
redis_conn = Redis()
app.config['CACHE_TYPE'] = 'redis'
app.cache = Cache(app)
app.redis_con = StrictRedis()

handler = RedisHandler('api-logs', redis_conn)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)


@app.before_request
def before_request():
    g.user = {}
    api_token = request_header('batman-API-Token')
    locale = request_header('batman-Locale') or 'en'
    if api_token:
        try:
            payload = jwt.decode(api_token, app.config['JWT_SECRET'])
            if not g.user:
                g.user = {}
            if not payload:
                abort(403, message="Invalid or expired token")
            # g.user['uid'] = payload['userId'] if 'userId' in payload else None
            # g.user['kid'] = payload['kid'] if 'kid' in payload else None
            # g.buyer_id = payload['userId'] if 'userId' in payload else None
            # g.token_id = payload['kid'] if 'kid' in payload else None
            # g.device_id = payload['device'] if 'device' in payload else ''
            # g.app_id = payload['app'] if 'app' in payload else ''
            # g.store_uuid = payload['sid'] if 'sid' in payload else None
        except jwt.ExpiredSignatureError:
            if request.endpoint != 'authtoken':
                abort(403, message="Invalid or expired token")
        except ValueError:
            print(ValueError)
            print("Unexpected error:", sys.exc_info()[0])
            abort(403, message="Invalid or expired token")
    elif request.endpoint != 'authtoken':
        abort(403, message="Invalid or expired token")
    #validate_access_by_endpoint()

#: Endpoint List
#: Store
api.add_resource(
    Queue,
    '/queue'
)


# @app.route("/spec")

# Run server
if __name__ == "__main__":
    socketio.run(app, host= '192.168.1.231')
