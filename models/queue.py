from common.mysqldb import db


class queue(db.Model):
    __tablename__ = 'queue'

    idqueue = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(45))
    status = db.Column(db.String(45))

    def __init__(self, device_id, status):
        self.device_id = device_id
        self.status = status
    #
    # def __repr__(self):
    #     return '<jpmarket_stores %r' % self.name
