DEBUG=True
JSONIFY_PRETTYPRINT_REGULAR=False
JWT_SECRET='JWTSECRET'
HMAC_KEYS={"demo":"demo","beta":"demo"}
ACCESS_TOKENS=["demotoken","betatoken"]

# CLOUDINARY={
# 'url':'https://cloudinary.com/image/upload/',
# 'transformations':{
# '30':'transformation',
# '50':'transformation',
# }}
#
# TWILIO={'sid':'',
# 'token':'',
# 'sender':'+SENDERNUMBER'}
#
# MANDRILL={
# 'username':'USERNAME',
# 'password':'PASSWORD',
# 'sender':'no-reply@jadopado.com',
# 'sender_name':'JadoPado',
# 'port':'2525',
# 'host':'smtp.mandrillapp.com',
# 'apikey':'API_KEY'
# }

SQLALCHEMY_DATABASE_URI='mysql://root:@localhost/batman_v1'
SQLALCHEMY_TRACK_MODIFICATIONS = False
