import MULTIINSERT as m
import UPDATEFILE as u
import MULTICREATE as c
if __name__ == "__main__":
    obj2 = c.createconnection()
    obj2.createsql()
    obj1 = m.fixed()
    obj1.file1()
    obj3 = u.updatefile()
    obj3.updatefile1()