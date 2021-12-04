from app import db

class Client(db.Model):
    __tablename__ = 'client'
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    phone_number = db.Column(db.String(10))
    payment_method = db.Column(db.String(6))

    def __init__(self, name, phone_number, payment_method):
        self.name = name
        self.phone_number = phone_number
        self.payment_method = payment_method

class Appointment(db.Model):
    __tablename__ = 'appointment'
    apid = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date())
    time = db.Column(db.Time())
    service = db.Column(db.String(20))

    def __init__(self, date, time, service):
        self.date = date
        self.time = time
        self.service = service

class Schedules(db.Model):
    __tablename__ = 'schedules'
    cid = db.Column(db.Integer, db.ForeignKey(Client.cid))
    apid = db.Column(db.Integer, db.ForeignKey(Appointment.apid))

    def __init__(self, cid, apid):
        self.cid = cid
        self.apid = apid

class Stylist(db.Model):
    __tablename__ = 'stylist'
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    expertise = db.Column(db.String(50))

    def __init__(self, sid, name, expertise):
        self.sid = sid
        self.name = name
        self.expertise = expertise

class Scheduled(db.Model):
    __tablename__ = 'scheduled'
    sid = db.Column(db.Integer, db.ForeignKey(Stylist.sid))
    apid = db.Column(db.Integer, db.ForeignKey(Appointment.apid))

    def __init__(self, sid, apid):
        self.sid = sid
        self.apid = apid

class Service(db.Model):
    __tablename__ = 'service'
    serid = db.Column(db.Integer, primary_key=True)
    style = db.Column(db.String(20))

    def __init__(self, serid, style):
        self.serid = serid
        self.style = style

class Offers(db.Model):
    __tablename__ = 'offers'
    sid = db.Column(db.Integer, db.ForeignKey(Stylist.sid))
    serid = db.Column(db.Integer, db.ForeignKey(Service.serid))

    def __init__(self, sid, serid):
        self.sid = sid
        self.style = style

class Haircut(db.Model):
    __tablename__ = 'haircut'
    serid = db.Column(db.Integer, primary_key=True)
    style = db.Column(db.String(20))

    def __init__(self, serid, style):
        self.serid = serid
        self.style = style

class ColoringSession(db.Model):
    __tablename__ = 'coloringsession'
    serid = db.Column(db.Integer, primary_key=True)
    materials = db.Column(db.PickleType(mutable=True))

    def __init__(self, serid, materials):
        self.serid = serid
        self.materials = materials