# Hotcake-Oven-API

**Platform API** RESTful implementation for backend services of Hotcake-Oven.

API methods return JSON in response to HTTP requests.

###Installation

```
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```
`Rename and edit config_sample.py to config.py`


### Authentication
API Token is required to be included in header
```
"X-JadoPado-API-Token": {API_Token}
```

### Endpoints Available
```
/v1/stores
```

### Stores Endpoint

Action | HTTP request | Description
--- | --- | ---
List all stores | `GET` /stores | Lists all stores with pagination.
List a store | `GET` /stores/{store_id} | Filter and list store by id.

####Example Response
```
{
    "id": 0,
    "name": "Store 1",
    "city": "Colombo"
}
```

####Unit Tests
Run unit tests by executing **tests_run.py**