import pymysql
def connection():
    con=pymysql.connect(host='localhost',user='root',password='HACKZ',db='hotel',port=3306)
    cm=con.cursor()
    return cm,con