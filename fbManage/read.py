import csv,os
import fbmanage
parentPath = os.path.abspath(os.pardir)
responsePath = parentPath + '/server/response/'
newPostNum = len(os.listdir(responsePath))

def csvResponseReader(responsePath,mode='1'):
    readerLs = []
    allPostCsvPath = parentPath + '/server/allPost.csv'
    for filenames in os.listdir(responsePath):
        file = responsePath + filenames
        print(file)
        with open(file, 'r',  newline='',encoding='utf-8') as fin:
            reader = csv.reader(fin)
            for row in reader:
                time = row[0]
                message = row[1]
                if mode == '1' or mode == '':
                    print("發文時間:{}".format(time))
                    print("發文內容:{}".format(message))
                    res = api.PostFanpage(fanPageId, message)
                    print("發文狀態:{}".format(res))
                    if res == "post_success":
                        with open(allPostCsvPath, 'a', newline='',encoding='utf-8') as all:
                            writter = csv.writer(all)
                            data = [(time, message)]
                            for ls in data:
                                writter.writerow(ls)
        os.remove(file)        
    print("所有文章已發文完畢")

if __name__ == "__main__":
    token = "EAACAguZCz0IMBAMmB5ctg3PJbWrgQmnP9CLFZA5UMPXWuy7gGtgMYASh3ZCZCXaStNeutA3MPcJ7i7MELhWGMdGDpEZC0ZByPvQ5Hyaqk6FrgnZCZCSzRaHVkVmQMJVj8YOkLTfOa8nIpjqNt2HDDl5WA1XaEAA43Wvlc6SRRPap92iVp4bqH9Yf"
    api = fbmanage.FbApiUse(token)
    fanPageId = "363831297404398"
    
    print("總共有{}篇文章尚未審核".format(newPostNum))
    if newPostNum == 0:
        print("不需要審核")
    else:
        print("請選擇模式 (1)不審核全部PO出 (2)手動審核 (3)關鍵字審核(開發中) (4)定時不審核PO出 (5)定時關鍵字審核")
        choose = input()
        csvResponseReader(responsePath, mode=choose)






