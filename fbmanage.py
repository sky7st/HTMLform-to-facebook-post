import requests
import re
import json

'''
class FbApiUse is for fbapi v2.11
'''
class FbApiUse:
    def __init__(self, fbParmToken):
        self.fbApiUrl = "https://graph.facebook.com/v2.11/"
        self.fbParmToken = fbParmToken
    
    def PostFanpage(self, fanPageId, message):
        postFanPageUrl = "https://graph.facebook.com/v2.11/" + fanPageId + "/feed"
        postData = {
            "access_token" : self.fbParmToken,
            "message" : message
        }
        postFanPageRes = requests.post(postFanPageUrl, data=postData)
        resJson = json.loads(postFanPageRes.text)
        '''
        resJson : if Post success=> request {"id":"PostId"}
                  if error => request {'error': {'message': 'Duplicate status message', 'type': 'OAuthException', 
                  'code': 506, 'error_subcode': 1455006, 'is_transient': False, 
                  'error_user_title': 'Duplicate Status Update','error_user_msg': 'This status update is identical to the last one you posted. Try posting something different, or delete your previous update.',
                   'fbtrace_id': 'Aw6nhBDHeDq'}} ...etc

        '''
        if 'id' in resJson.keys(): #post Page Success
            return "post_success"
        else:
            if 'error' in resJson.keys():
                message = resJson['error']['message']
                parser = self.messageParser("PostFanpage", message)
                print("There're something wrong.Please check.")
                return "Error:" + parser

    def messageParser(self,method, message):
        if method == "PostFanpage":
            if "Duplicate status message" in message:
                return "error_duplicate_post"
            elif "Some of the aliases you requested do not exist" in message:
                return "wrong_fanPageId"
            else:
                return "post_success"
if __name__ == "__main__" :
    token = "EAACAguZCz0IMBAMmB5ctg3PJbWrgQmnP9CLFZA5UMPXWuy7gGtgMYASh3ZCZCXaStNeutA3MPcJ7i7MELhWGMdGDpEZC0ZByPvQ5Hyaqk6FrgnZCZCSzRaHVkVmQMJVj8YOkLTfOa8nIpjqNt2HDDl5WA1XaEAA43Wvlc6SRRPap92iVp4bqH9Yf"
    api = FbApiUse(token)
    message = u"測試20171108334"
    fanPageId = "363831297404398"
    res = api.PostFanpage(fanPageId, message)
    print(res)