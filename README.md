# Batman-API

**Platform API** RESTful implementation for backend services of Batman-Game.

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
"batman-API-Token": {API_Token}
```

### Endpoints Available
```
/v1/Queue
```

####Unit Tests
Run unit tests by executing **tests_run.py**
