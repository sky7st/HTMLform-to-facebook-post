# -*- coding: utf-8 -*-
import sys,os
import time
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
    message = request.form.get('message')
    chdir = os.getcwd() 
    with open(chdir+'/response/test.csv', 'w', newline='',encoding='utf-8') as file:  
        csvCursor = csv.writer(file)
        
        csvHeader = ('time', 'message')
        data = [csvHeader,(postTime, message)]
        for ls in data:
            csvCursor.writerow(ls)

    print("csv write")

    token = "EAACAguZCz0IMBAMmB5ctg3PJbWrgQmnP9CLFZA5UMPXWuy7gGtgMYASh3ZCZCXaStNeutA3MPcJ7i7MELhWGMdGDpEZC0ZByPvQ5Hyaqk6FrgnZCZCSzRaHVkVmQMJVj8YOkLTfOa8nIpjqNt2HDDl5WA1XaEAA43Wvlc6SRRPap92iVp4bqH9Yf"
    fanPageId = "363831297404398"
    fbApi = fbmanage.FbApiUse(token)
    res = fbApi.PostFanpage(fanPageId, message)
    return render_template('result.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0',threaded=True)