import sqlite3
from sqlite3 import Error


class GetData:
    #  jonno
    def insert_employee(self, item):
        """insert an employee into employee table"""
        try:
            conn = sqlite3.connect('test2.db')
            conn.execute("INSERT INTO EMPLOYEES "
                         "(EMPID, GENDER, AGE, SALES, BMI, SALARY, DOB)"
                         "VALUES (?, ?, ?, ?, ?, ?, ?)",
                         (item[0], item[1], item[2], item[3],
                          item[4], item[5], item[6]))
            print("item added successfully")
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

    # renee
    @staticmethod
    def get_all_employee():
        """
        Query all rows in the employee table
        :param conn: the Connection object
        :return:
        """
        conn = sqlite3.connect('test2.db')
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM EMPLOYEES")
            rows = cur.fetchall()
            employee_list = []
            for row in rows:
                employee_list.append(row)
            return employee_list
        except (sqlite3.ProgrammingError, sqlite3.Error) as e:
            print("TABLE EMPLOYEES not found")
        except sqlite3.Error as er:
            print("Database error: ", er.message)
        except Exception as e:
            print(e)

    # Renee
    @staticmethod
    def get_ave_salary():

        conn = sqlite3.connect('test2.db')
        cur = conn.cursor()
        try:
            cur.execute("SELECT AVG(SALARY) FROM EMPLOYEES")
            ave_salary = cur.fetchone()[0]
            if ave_salary < 0:
                raise ValueError("wrong value")
            else:
                return ave_salary
        except (sqlite3.ProgrammingError, sqlite3.Error) as e:
            print("TABLE EMPLOYEES not found")
        except sqlite3.Error as er:
            print("Database error: ", er.message)
        except Exception as e:
            print(e)
        finally:
            if conn:
                conn.close()

    # Chami
    def get_ave_sales(self):
        """
        >>> get_ave_sales(40)
        Traceback (most recent call last):
        TypeError: get_ave_salary() takes 0 positional arguments but 1 was given

        >>> get_ave_sales()
        Traceback (most recent call last):
        TypeError: get_ave_salary() takes 0 positional arguments but 1 was given

        :return:
        """
        conn = sqlite3.connect('test2.db')
        cur = conn.cursor()
        cur.execute("SELECT avg(sales) FROM EMPLOYEES")
        ave_sales = round(cur.fetchone()[0], 2)
        return ave_sales
