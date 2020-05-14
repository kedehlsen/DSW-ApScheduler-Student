from flask import Flask
from flask import render_template
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
 
import time
 
app = Flask(__name__)

#TODO: add the code for the ApScheduler here
def scheduled_task():
    return "It is now 4:06pm</p>"
 
@app.route('/')
def welcome():
   scheduler = BackgroundScheduler({'apscheduler.timezone':'America/Los_Angeles'})
   scheduler.start()
   scheduler.add_job(scheduled_task, trigger='cron', hour=16, minute=6)
   return render_template('home.html')
  
if __name__=="__main__":
    app.run(debug=False)
