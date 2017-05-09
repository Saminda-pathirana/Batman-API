"""List of parameters used for the documentation"""

page = {
    'name': 'page',
    'description': 'Page Number',
    'in': 'query',
    'required': False,
    "type": "integer",
}

records_per_page = {
    'name': 'recordsPerPage',
    'description': 'Records Per Page',
    'in': 'query',
    "type": "integer",
    'required': False,
}

store_id = {
    'name': 'store_id',
    'description': 'Store Id',
    'in': 'query',
    "type": "integer",
    'required': False,
}
