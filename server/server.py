# -*- coding: utf-8 -*-
import sys,os,time,random
import csv
from flask import Flask
from flask import render_template
from flask import request
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def result():
    postTime = time.strftime("%Y/%m/%d %H:%M")
    fullTime = time.strftime("%Y%m%d_%H%M%S")
    message = request.form.get('message')
    chdir = os.getcwd() 
    filename = fullTime + "_" + str(random.randint(0,99999)) + ".csv"
    with open(chdir+'/response/' + filename, 'w', newline='',encoding='utf-8') as file:  
        csvCursor = csv.writer(file)        

        data = [(postTime, message)]
        for ls in data:
            csvCursor.writerow(ls)

    print("csv write")
    return render_template('result.html')
if __name__ == '__main__':
    print("server staring.....")
    app.run(host='0.0.0.0', threaded=True, port=8080)