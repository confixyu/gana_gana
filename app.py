
# This the Flask app for the raffle of the meetup

from flask import Flask, request, render_template, redirect, url_for

import csv
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
   return render_template('app.html')

@app.route("/reward")
def reward():
   rewards = []
   with open('reward.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
         for row in spamreader:
            print(', '.join(row))
            rewards.append(row[0])
   return render_template('reward.html', rewards = rewards)

@app.route("/participant")
def participant():
   participants = []
   with open('participants.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
         for row in spamreader:
            print(', '.join(row))
            participants.append(row[0])
   return render_template('participant.html', participants = participants)

# Upload file
@app.route('/upload')
def upload_file():
   return redirect(url_for('index'))
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8000")