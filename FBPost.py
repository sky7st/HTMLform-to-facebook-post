#coding=utf-8
import requests
import re
import json

accessToken = "EAACAguZCz0IMBAMmB5ctg3PJbWrgQmnP9CLFZA5UMPXWuy7gGtgMYASh3ZCZCXaStNeutA3MPcJ7i7MELhWGMdGDpEZC0ZByPvQ5Hyaqk6FrgnZCZCSzRaHVkVmQMJVj8YOkLTfOa8nIpjqNt2HDDl5WA1XaEAA43Wvlc6SRRPap92iVp4bqH9Yf"

fanPageId = "363831297404398"

postFanPageUrl = "https://graph.facebook.com/v2.11/" + fanPageId + "/feed"

postData = {
    "access_token" : accessToken,
    "message" : u"此文章由python&永久權杖發出"
}

res = requests.post(postFanPageUrl, data=postData)
print(res.text)