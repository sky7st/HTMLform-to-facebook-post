# -*- coding: utf-8 -*-
import sys,os,time,random
import csv
from flask import Flask
from flask import render_template
from flask import request
from config import DevConfig

import fbmanage

app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def result():
    postTime = time.strftime("%Y/%m/%d %H:%M")
    fullTime = time.strftime("%Y%m%d_%H%M%S")
    message = request.form.get('message')
    chdir = os.getcwd() 
    with open(chdir+'/response/test.csv', 'w', newline='',encoding='utf-8') as file:  
        csvCursor = csv.writer(file)
        
        csvHeader = ('time', 'message')
        data = [csvHeader,(postTime, message)]
        for ls in data:
            csvCursor.writerow(ls)

    print("csv write")
    return render_template('result.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0',threaded=True)