import csv,os
import fbmanage
chdir = os.getcwd() 
responsePath = chdir + '/response/'
newPostNum = len(os.listdir(responsePath))

def csvResponseReader(responsePath,mode='1'):
    readerLs = []
    for filenames in os.listdir(responsePath):
        file = responsePath + filenames
        print(file)
        with open(file, 'r',  newline='',encoding='utf-8') as fin:
            reader = csv.reader(fin)
            for row in reader:
                if mode == '1' or mode == '':
                    print("發文時間:{}".format(row[0]))
                    print("文章內容:{}".format(row[1]))
                    res = api.PostFanpage(fanPageId, row[1])
                    print("狀態:{}".format(res))
        os.remove(file)


        
        # print("所有文章已PO出")

if __name__ == "__main__":
    token = "EAACAguZCz0IMBAMmB5ctg3PJbWrgQmnP9CLFZA5UMPXWuy7gGtgMYASh3ZCZCXaStNeutA3MPcJ7i7MELhWGMdGDpEZC0ZByPvQ5Hyaqk6FrgnZCZCSzRaHVkVmQMJVj8YOkLTfOa8nIpjqNt2HDDl5WA1XaEAA43Wvlc6SRRPap92iVp4bqH9Yf"
    api = fbmanage.FbApiUse(token)
    fanPageId = "363831297404398"
    
    print("一共有{}個文章尚未審核".format(newPostNum))
    print("請選擇模式(1)不審核全部送出 (2)手動審核 (3)關鍵字自動審核(開發中) (預設:不審核)")
    # csvResponseReader(responsePath)
    choose = input()
    csvResponseReader(responsePath, mode=choose)






