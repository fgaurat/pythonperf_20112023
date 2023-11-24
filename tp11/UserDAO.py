import sqlite3
from User import User

class UserDAO:

    def __init__(self,db_file):
        self.__con = sqlite3.connect(db_file)
    
    def findAll(self):
        cur = self.__con.cursor()
        res = cur.execute("SELECT * FROM users_tbl")
        for d in res.fetchall():
            
            u = User(*d)
            yield u
        
    def __enter__(self):
        print('Starting')
        return self

    def __exit__(self, *exc):
        print('Finishing')
        print(exc)
        self.__con.close()
        return False
    
    
    def __del__(self):
        self.__con.close()
    
    