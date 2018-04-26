import sqlite3
from sqlite3 import Error


class EmployeeDatabase:

    #  jonno
    def create_connection(self, db_file):
        """Create a database connection to SQLite Database """
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
            print("Database created")
            self.drop_employee_table(conn)
            self.create_employee_table(conn)
        except NameError:
            print("Incorrect file format for db name")
        except Error as e:
            print(e)
        finally:
            conn.close()

    #  jonno
    def drop_employee_table(self, conn):
        conn.execute('''DROP TABLE IF EXISTS EMPLOYEES''')
        print("Table Dropped")

    def create_employee_table(self, conn):
        try:
            conn.execute('''CREATE TABLE EMPLOYEES
            (EMPID TEXT PRIMARY KEY,
            GENDER CHAR(1),
            AGE INT,
            SALES INT,
            BMI TEXT,
            SALARY INT,
            DOB TEXT);''')
            print("Employee Table created successfully")
        except Error as e:
            print(e)
        finally:
            conn.close()


db = EmployeeDatabase()
db.create_connection("test2.db")
# db.get_ave_salary()