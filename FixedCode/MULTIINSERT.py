from dateutil import parser
import mysql.connector
class fixed:
    def file1(self):
        f = open('rawdata.prn', 'r')
        line = f.readline()
        db = mysql.connector.connect(host="localhost", user="root", password="root", db="casestudy2",
                                     port="3306")
        cursor = db.cursor()
        while line:
            line = f.readline()
            x = line
            chunks, chunk_size = len(x), int(len(x) / 1)
            if chunks != 0:
                i = [x[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
                s = str(i)
                self.Employeeid, self.EmpName, self.Gender, self.Empmobileno, self.OnBoadDate,= s[2:13], s[13:38], s[38:45],s[45:58],s[58:71]
                self.Rollindate, self.Rolloffdate, self.Employeeaddress, self.Employeeemail=s[71:84],s[84:97],s[97:117],s[117:147]
                self.Employeedob,self.Deptid, self.DeptName, self.Deptdesc, self.Projectid=s[147:160],s[160:170],s[170:190],s[190:210],s[210:220]
                self.ProjectName,self.ProjectDescription, self.Projectlocation, self.Projeffdate=s[220:231],s[231:251],s[251:271],s[271:284]
                self.Projenddate, self.salaryid, self.salarydate, self.salaryamt,self.Bonus=s[284:297],s[297:307],s[307:320],s[320:330],s[330:338]
                self.Designationid,self.DesignationName,self.Designationdescription=s[338:353],s[353:373],s[373:395]
                ei, en, g,eno = self.Employeeid.strip(), self.EmpName.strip(),self.Gender.strip(),self.Empmobileno.strip()
                obd,rid , rod, ea = self.OnBoadDate.strip(), self.Rollindate.strip(),self.Rolloffdate.strip(),self.Employeeaddress.strip()
                ee ,ed , di,dn = self.Employeeemail.strip(),self.Employeedob.strip(),self.Deptid.strip(), self.DeptName.strip()
                dd, pi,pn, pd,pl = self.Deptdesc.strip(),self.Projectid.strip(),self.ProjectName.strip(),self.ProjectDescription.strip(),self.Projectlocation.strip()
                pefd,ped,si,sd,sa,b = self.Projeffdate.strip(),self.Projenddate.strip(),self.salaryid.strip(), self.salarydate.strip(), self.salaryamt.strip(),self.Bonus.strip()
                di,dn,dd=self.Designationid.strip(), self.DesignationName.strip(), self.Designationdescription.strip()
                obddt = parser.parse(obd).date()
                riddt = parser.parse(rid).date()
                roddt = parser.parse(rod).date()
                eddt = parser.parse(ed).date()
                pefddt =parser.parse(pefd).date()
                peddt = parser.parse(ped).date()
                sddt =parser.parse(sd).date()

                EMPLOYEE ="insert into employee (Employeeid,EmpName,Gender,Empmobileno,OnBoadDate,Rollindate,Rolloffdate,Employeeaddress,Employeeemail,Employeedob) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format (ei,en,g,eno,obddt,riddt,roddt,ea,ee,eddt)
                ACCENTUREEMPLOYEE = "insert into Accenture_employee (Employeeid,EmpName,Gender,Empmobileno,OnBoadDate,Rollindate,Rolloffdate,Employeeaddress,Employeeemail,Employeedob,Deptid,Projectid,salaryid,salaryamt,Desinationid) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}');".format (ei,en,g,eno,obddt,riddt,roddt,ea,ee,eddt,di,pi,si,sa,di)
                DEPT = 'insert into dept values( "{}","{}","{}");'.format(di,dn,dd)
                PROJECT ='insert into project values( "{}","{}","{}","{}","{}","{}");'.format(pi,pn,pd,pl,pefddt,peddt)
                SALARY = 'insert into salary values( "{}","{}",{},{});'.format(si,sddt,sa,b)
                DESIGNATION = 'insert into designation values("{}","{}","{}");'.format(di,dn,dd)
                cursor.execute(EMPLOYEE)
                cursor.execute(DEPT)
                cursor.execute(PROJECT)
                cursor.execute(SALARY)
                cursor.execute(DESIGNATION)
                cursor .execute(ACCENTUREEMPLOYEE)
        db.commit()
        db.close()
'''if __name__ == "__main__":
    obj1 = fixed()
    obj1.file1()'''

