from flask import Flask, request, render_template 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jixsiczlihklpp:a49f4da96259a3c401180cbe64385b12ca7409290b261e356316ae5124d39cf7@ec2-18-210-159-154.compute-1.amazonaws.com:5432/d5dm9dn7tpu39m'
app.config['SQLALCHEMY_DATABASE_URI'] = False

db = SQLAlchemy(app)

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
        
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def ret():
    return render_template('home.html')

@app.route('/complete', methods=['POST'])
def complete():
    if request.method == 'POST':
        client = request.form['client']
        phone_number = request.form['phone_number']
        payment_method = request.form['payment_method']
        print(client, phone_number, payment_method)
        client_data = Client(client, phone_number, payment_method)
        db.session.add(client_data)
        db.session.commit()

        date = request.form['date']
        time = request.form['time']
        
        if (int(request.form['service']) >= 401 and int(request.form['service']) <= 405):
            service = 'Haircut'
        else:
            service = 'ColoringSession'

        appointment_data = Appointment(date, time, service)
        db.session.add(appointment_data)
        db.session.commit()

        if (int(request.form['stylist']) == 201):
            stylist = 'Clowney Pennywise'
            sid = 201
        if (int(request.form['stylist']) == 202):
            stylist = 'Edward S. Hands'
            sid = 202
        if (int(request.form['stylist']) == 203):
            stylist = 'Stylist Joe'
            sid = 203
        if (int(request.form['stylist']) == 301):
            stylist = 'John Bows'
            sid = 301
        if (int(request.form['stylist']) == 302):
            stylist = 'Miranda Cosgrove'
            sid = 302
        if (int(request.form['stylist']) == 303):
            stylist = 'Missy Andrews'
            sid = 303
        print(date, time, service, stylist, sid)
        if client == '' or phone_number == '' or payment_method == '' or date == '' or stylist == '':
            return render_template('home.html', alert='Enter the required fields to progress')
        return render_template('complete.html')

if __name__ == '__main__':
    app.run(debug=True)