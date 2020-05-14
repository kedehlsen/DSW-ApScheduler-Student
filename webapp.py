from flask import Flask
from flask import render_template
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
 
import time
 
app = Flask(__name__)

#TODO: add the code for the ApScheduler here
def scheduled_task():
    timed_message = Markup("<p>It is now 3:02pm</p>")
 
@app.route('/')
def welcome():
   scheduler = BackgroundScheduler({'apscheduler.timezone':'America/Los_Angeles'})
   scheduler.start()
   scheduler.add_job(scheduled_task, trigger='cron', hour=15, minute=2)
   return render_template('home.html', timed_message= message)
  
if __name__=="__main__":
    app.run(debug=False)
