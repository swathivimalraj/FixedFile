import mysql.connector
class createconnection:
    def createsql(self):
        #global result
        db = mysql.connector.connect(host="localhost",user="root",password="root",db="casestudy2",port="3306" )
        cursor = db.cursor()
        #s = 'CREATE TABLE employee (emp_id VARCHAR(255), f_name VARCHAR(255) ,l_name VARCHAR(255));create table dept (emp_id varchar(90),f_name varchar(90),l_name VARCHAR(255));'
        # filter() removes trailing empty list item
        fd = open('createstatements.sql', 'r')
        sqlFile = fd.read()
        fd.close()
        # all SQL commands (split on ';')
        sqlCommands = sqlFile.split(';')
        print (sqlCommands)
        # Execute every command from the input file
        for command in sqlCommands:
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
            print (command)
            try:
                cursor.execute(command)
            except OperationalError, msg:
                print "Command skipped: ", msg
        db.commit()
        db.close()
'''if __name__ == "__main__":
    obj1 = createconnection()
    obj1.createsql()'''