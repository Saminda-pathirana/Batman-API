from flask import request, current_app, g, json
from .reqparse import RequestParser
import six


def request_field(var, default_value=None):
    """Get values from POST or GET"""
    if request.method == 'POST' and var in request.form:
        return request.form[var]
    elif var in request.args:
        return request.args.get(var)
    else:
        return default_value


def request_header(var):
    """Get value from headers"""
    return request.headers.get(var) if var in request.headers else None


def exception_error_messages():
    """Error handling"""
    return {
        'ResourceDoesNotExist': {
            'message': "A resource with that ID no longer exists",
            'code': '10002',
            'link': '',
            'status': 410
        }
    }


class AwesomeDict(dict):
    def __missing__(self, key):
        return key


def jpt(value):
    if g.get('locale') == 'ar':
        return current_app.lang_ar.gettext(six.text_type(value))
    else:
        return six.text_type(value)


def jpm(msg_code, code=None, empty=False, link=None, params=None):
    # Copy it to make it immutable
    messages = {
        'store_not_found': {
            'message': "Store not found",
            'code': '100010',
            'link': '#/Stores',
            'status': 404
        }
    }
    msg = messages.get(msg_code) if msg_code in messages else None
    # if params:
    if msg and 'link' in msg:
        if code:
            msg['code'] = code
        # if link:
        #     msg['link'] = link
        # msg['link'] = request.url_root + msg['link']
        try:
            msg['message'] = jpt(msg['message'])
            msg['message'] = msg['message'].format_map(AwesomeDict(**params))
        except:
            pass
        # + '#' + str(message['code'])
    if not msg and not empty:
        msg = {
            'message': msg_code
        }
    return msg


def parse_args(params=None, **kwargs):
    """
    request parser
    """
    pagination = kwargs.get('pagination', True)

    # if no pagination and no params
    if not pagination and not params:
        return []

    # set default vars
    page = kwargs.get('page', 1)
    max_records = kwargs.get('max_records', 500)
    parser = RequestParser(bundle_errors=True)

    # parse default pagination args
    if pagination:
        parser.add_argument(
            'page',
            type=int,
            help= 'Page value should be an integer')
        parser.add_argument(
            'recordsPerPage',
            type=int,
            help='Records per page value should be an integer')

    # parse custom args
    if params:
        for key, param in params.items():
            parser.add_argument(key, **param)

    args = parser.parse_args()

    # create limit offset and max_records check.
    # Also set the default values if empty
    if pagination:
        # current_app.logger.info(
        #     args.decode('utf8'))
        args['page'] = kwargs.get('page') or args['page']
        args['recordsPerPage'] = \
            kwargs.get('records_per_page') or args['recordsPerPage']
        if not args['recordsPerPage']:
            args['recordsPerPage'] = 24
        if not args['page']:
            args['page'] = 1
        if args['recordsPerPage'] > max_records:
            args['recordsPerPage'] = max_records
        args['offset'] = (abs(args['page']) - 1) * args['recordsPerPage']

    return args
