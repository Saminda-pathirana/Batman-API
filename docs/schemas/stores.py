from flask_restful_swagger_2 import Schema


class GetStoreModel(Schema):
    #: Lists the schema for stores endpoint get request
    type = 'object'
    properties = {
        'id': {
            'type': 'integer',
            'format': 'int64',
        },
        'name': {
            'type': 'string'
        }
    }
    required = ['name']
