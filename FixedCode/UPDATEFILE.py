import mysql.connector
class updatefile:
    def updatefile1(self):
        try:
            db = mysql.connector.connect(host="localhost",user="root",password="root",db="casestudy2",port="3306" )
            cursor = db.cursor()
        except:
            print "Invalid Host or port id"
        q="update Accenture_employee set Flag ='Y' WHERE Rolloffdate like '9999-%-%';"
        cursor.execute(q)
        db.commit()
        db.close()
#obj3 = updatefile()
#obj3.updatefile1()
