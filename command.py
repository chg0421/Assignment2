from cmd import Cmd
from controller import Controller
from command_line import CommandLine


class Command(Cmd):
    """
    Command File Version 1
    """
    c = Controller()
    cl = CommandLine()

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.my_name = "unknown"

    # load and save valid employee into the database
    def valid_employee(self, file_name):
        employees = self.c.load_file(file_name)
        if employees:
            while True:
                ans = input("There are " + str(len(employees['Valid'])) +
                            " Employees validated in the file"
                            "\n Do you want to add them to the Database?"
                            "\n [Y/N]"
                            "\n>>>")
                if ans.upper() == "Y":
                    self.add_data(employees['Valid'])
                    break
                elif ans.upper() == "N":
                    print("Data not added to the database")
                    break
                else:
                    print("Invalid input try again")

    # load and save invalid employee into the database
    def invalid_employee(self, file_name):
        employees = self.c.load_file(file_name)
        if len(employees["Invalid"]) is not 0:
            while True:
                ans = input("There's" + str(len(employees['Invalid'])) +
                            " Employee(s) invalid"
                            "\n Do you want to save to invalid.csv?"
                            "\n [Y/N]"
                            "\n >>>")
                if ans.upper() == "Y":
                    self.c.save_invalid(employees['Invalid'])
                    break
                elif ans.upper() == "N":
                    print("Invalid Data not saved")
                    break
                else:
                    print("Invalid Input")

    def do_store(self, file_name):
        self.valid_employee(file_name)
        self.invalid_employee(file_name)

    # Jono
    def add_data(self, content):
        """
        Adds file to database
        :param content: content from loaded file (List)
        :return:
        """
        self.c.add_to_database(content)
        print("items added to database")

    def get_all_employees(self):
        return self.c.get_all_employees()

    # Chami
    def do_save(self, file_name):
        """
        Syntax: save [file_name]
        :param file_name: a string representing a file name e.g example.txt
        :return: None
        """
        # destination = F:\ARA3\Python\Assignment\test
        if file_name:
            employee_list = self.get_all_employees()
            self.c.save_file(file_name, employee_list)
            print(file_name)
        else:
            print("File did not save.")

    # Renee
    def do_chart(self, option):
        """
        Syntax: to output a Bar Chart or Pie Chart
        :param option: option indicates what chart
        /a to view average sale and average salary in the bar chart,
        /sb to view the sales of individual employee in the bar chart
        /sl to view the sales of individual employee in the line chart
        /sp to view the salary detail of individual employee in the pie chart
        :return:
        """

        if option and option.strip():
            if option.lower() == "/a":
                self.c.print_chart_average()
            elif option.lower() == "/sb":
                self.c.print_chart_sales()
            elif option.lower() == "/sp":
                self.c.print_chart_pie()
            elif option.lower() == "/sl":
                self.c.print_chart_line()
            else:
                print("Invalid input try again")
        else:
            print("please enter your option")

    # Jono
    def do_quit(self, line):
        """
        To quit the application
        :param line:
        :return:
        """
        print("Quitting.....")
        return True

    def command_line_arguments(self):
        self.cl.greeting()
        self.cl.set_name()
        self.cl.set_number_of_command()


if __name__ == "__main__":
    command = Command()
    command.command_line_arguments()
    command.cmdloop()
