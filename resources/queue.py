from flask_restful import fields, marshal_with
from sqlalchemy import and_
from flask_restful_swagger_2 import swagger, Resource

from common import parse_args
from models import queue

from common.mysqldb import db

# from docs.schemas.stores import GetStoreModel
# from docs.responses.stores import get_store_response
# from docs.parameters import page, records_per_page, store_id

QUEUE_FIELDS = {
    'idqueue': fields.Integer,
    'device_id': fields.String,
    'status': fields.String(default="")
}


class Queue(Resource):
    #: Handling swagger documentation for this endpoint
    # @swagger.doc({
    #     'tags': ['Stores'],
    #     'description': 'List stores',
    #     'parameters': [store_id, page, records_per_page],
    #     'responses': {
    #         '200': {
    #             'description': 'OK',
    #             'schema': GetStoreModel,
    #             'examples': get_store_response
    #         }
    #     }
    # })
    @marshal_with(QUEUE_FIELDS, envelope='data')
    def get(self):
        arg_params = {
            'store_id': {
                'type': int,
                'help': 'Incorrect format for store_id'
            }
        }
        args = parse_args(arg_params)
        query = queue.query

        #: Get store by store id
        if args['store_id'] is not None:
            query = query.filter(and_(queue.id == args['store_id']))

        query = query.offset(args['offset']).limit(args['recordsPerPage'])
        response = query.all()

        return response

    def post(self):
        arg_params = {
            'device_id': {
                'type': str,
                'help': 'Incorrect format for device_id'
            }
        }
        args = parse_args(arg_params)
        newEntry = queue(args['device_id'], "waiting")
        db.session.add(newEntry)
        db.session.commit()

        response = {'status': 'SUCCESS'}
        return response
