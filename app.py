from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable = False)
    event_description = db.Column(db.String(200), unique = False)
    event_location = db.Column(db.String(200), unique = False)
    event_time = db.Column(db.String(50), unique = 	False)
    event_date = db.Column(db.String(50), unique = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    
    def __repr__(self):
        return '<Event Name %r>' %self.id
    





@app.route('/', methods = ["POST", "GET"])
@app.route('/home', methods = ["POST", "GET"])
def index():
    return render_template("index.html")

@app.route('/add_event', methods = ["POST", "GET"])
def form():
    
    if request.method == "POST":
        name = request.form['event_name']
        new_event_name = Event(event_name = name)
        
        description = request.form['event_description']
        new_event_description = Event(event_description = description)
        
        location = request.form['event_location']
        new_event_location = Event(event_location = location)

        
        try:
            db.session.add(new_event_name)
            db.session.add(new_event_description)
            db.session.add(new_event_location)
            db.session.add(new_event_date)
            db.session.add(new_event_time)
            
            db.session.commit()
           
            return redirect('/add_event')
        
        except:
            
            return "There was trouble adding your event."
        
        finally:
            
            return redirect('/')
    
    else:
        Events = Event.query.order_by(Event.date_created)
        return render_template("form.html", events = Events)
   
@app.route('/event/<int:id>')
def event(id):
    Events = Event.query.order_by(Event.date_created)
    return render_template("event.html", events = Events)

if __name__ == '__main__':
    app.run(debug=True)