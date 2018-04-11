from employee_database import EmployeeDatabase
from filer import Filer
from validator import Validator
from chart_maker import ChartMaker


class Controller:
    f = Filer()
    v = Validator()
    db = EmployeeDatabase()
    chart = ChartMaker()

    # Jono's
    def load_file(self, file):
        try:
            if ".csv" in file[-4:]:
                content = self.f.read_csv(file)
            elif ".xlsx" in file[-5:]:
                content = self.f.read_excel(file)
            elif ".txt" in file[-4:]:
                content = self.f.read_txt(file)
            else:
                message = "incorrect format please see help load"
                raise NameError(message)
            validated_employees = self.validate_items(content)
            return validated_employees
        except NameError as e:
            print(e)
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(e)

    def validate_items(self, content):
        valid_employees = []
        invalid_employees = []
        for employee in content:
            item = self.v.validate_all(employee)
            if False in item:
                invalid_employees.append(employee)
            else:
                valid_employees.append(employee)
            emp = {'Valid': valid_employees, 'Invalid': invalid_employees}
        return emp

    def add_to_database(self, content_list):
        for item in content_list:
            self.db.insert_employee(item)

    def get_all_employees(self):
        try:
            employees = self.db.get_all_employee()
            if len(employees) > 0:
                return employees
            else:
                raise IndexError
        except IndexError:
            print("No employees in database")
        except Exception as e:
            print(e)

    # renee
    def print_chart_average(self):
        ave_sales = self.db.get_ave_sales()
        ave_salary = self.db.get_ave_salary()
        self.chart.make_bar_average(ave_sales, ave_salary)

    def print_chart_sales(self):
        employees = self.db.get_all_employee()
        self.chart.make_bar_sales(employees)

    def print_chart_pie(self):
        employees = self.db.get_all_employee()
        self.chart.make_pie(employees)

    def print_chart_line(self):
        employees = self.db.get_all_employee()
        self.chart.make_line(employees)

    # Chami
    def save_file(self, file_format, employee_list):
        """
        # Chami -- added 19-03-2018
        >>> Controller.save_file('test1.txt', [['A001', 'M', '26', '200', 'Normal', '20', '08-10-1991'],['A001', 'M', '26', '200', 'Normal', '20', '08-10-1991']])
        Traceback (most recent call last):
        TypeError: save_file() missing 1 required positional argument: 'employee_list'

        >>> Controller.save_file('test1.txt',)
        Traceback (most recent call last):
        TypeError: save_file() missing 2 required positional arguments: 'file_format' and 'employee_list'

        >>> Controller.save_file()
        Traceback (most recent call last):
        TypeError: save_file() missing 3 required positional arguments: 'self', 'file_format', and 'employee_list'

        >>> Controller.save_file('test1.txt', [[],[]])
        Traceback (most recent call last):
        TypeError: save_file() missing 1 required positional argument: 'employee_list'

        >>> Controller.save_file('test1.txt', [[,[]])
        Traceback (most recent call last):
        SyntaxError: invalid syntax

        >>> Controller.save_file('test1.txt', [['A001', 'M', '26', '200', 'Normal', '20', '08-10-1991']['A001', 'M', '26', '200', 'Normal', '20', '08-10-1991']])
        Traceback (most recent call last):
        TypeError: list indices must be integers or slices, not tuple



        """
        try:
            if ".csv" in file_format:
                self.f.save_csv(file_format, employee_list)
            elif ".xlsx" in file_format:
                self.f.save_excel(file_format, employee_list)
            elif ".txt" in file_format:
                self.f.save_txt_file(file_format, employee_list)
            else:
                raise NameError("can not save that file type")
        except NameError as e:
            print(e)
        # except exception part needed


    def save_invalid(self, invalid_employees):
        try:
            self.f.save_txt_file("invalid.csv", invalid_employees)
        except:
            print("Whoops something went wrong")
