import csv
import sqlite3

def main():
    with sqlite3.connect(r".\tp08\formation.db") as con:
        cur = con.cursor()

        with open(r'.\tp08\MOCK_DATA.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sql = """INSERT INTO users_tbl(first_name,last_name,email,gender,ip_address)
                VALUES (?,?,?,?,?)"""
                values = list(row.values())[1:]
                cur.execute(sql,values)
                        
if __name__=='__main__':
    main()
