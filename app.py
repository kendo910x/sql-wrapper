#coding: utf-8
from flask import Flask, request, make_response
import MySQLdb
import os
app = Flask(__name__, static_folder='.')
con = MySQLdb.connect(
    user='root',
    passwd='password',
    host= os.environ['MYSQL_HOST'],
    db='mydb',
    charset='utf8')
cur = con.cursor()
sql = 'CREATE TABLE IF NOT EXISTS nametbl ( firstname CHAR(50), lastname CHAR(50) NOT NULL PRIMARY KEY)' 
print(sql)
cur.execute(sql)
cur.close
con.close
@app.route('/', methods=['POST'])
def index():
    sql = request.form['sql']
    print(sql)
    con = MySQLdb.connect(
        user='root',
        passwd='password',
        host= os.environ['MYSQL_HOST'],
        db='mydb',
        charset='utf8')
    cur = con.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    con.commit()
    cur.close
    con.close
    print(result)
    if len(result) == 0:
        html = '<html><body>'
        html = html + 'No name found.<br>'
        html = html + '<a href="/">return</a>'
        html = html + '</body></html>'
    else:
        answer = result[0][0]
        html = '<html><body>'
        html = html + 'The first name is "%s".<br>' %(answer)
        html = html + '<a href="/">return</a>'
        html = html + '</body></html>'
    return(html)
    print(html)
    return(html)
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80) 
