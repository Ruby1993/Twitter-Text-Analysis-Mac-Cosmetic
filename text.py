import pyodbc
import pandas as pd



conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=us-noc-bia01;"
                      "Database=SentimentAnalysis;"
                      "Trusted_Connection=yes;"
                      "uid=ruizhang;pwd=ASDasd!123")

cursor=conn.cursor()
# Get a list of system objects sorted by views, tables, procedures, and functions created by the user
content = ""
sql = "SELECT * FROM mac_february_04"
cursor.execute(sql)
rows = cursor.fetchall()

output=pd.DataFrame()
for i in rows:
    #print (i)
    output=output.append({'id':i[0], "text":i[1], 'favorited': i[2], 'favoriteCount':i[3],'replyToSN': i[4], 'PostedTime':i[5],'truncated':i[6],
    'replyToSID': i[7], 'replyToUID':i[9], 'StatusSource': i[10], 'screenName': i[11], 'retweetCount':i[12], 'isRetweet':i[13],
    'retweeted':i[14],'log':i[15],'lat':i[16]},ignore_index=True)



print (len(output))

output.to_csv('Mac_0402_TextAnalysis.csv',sep=',',index = False,encoding='utf-8')
