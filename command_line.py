import sys


class CommandLine:

    # renee
    @staticmethod
    def greeting():
        try:
            print(sys.argv[1])
        except NameError as e:
            print(e)
        except IndexError as e:
            print("Index Error :", e)

    # Jono
    @staticmethod
    def set_name():
        try:
            ans = input("What is your name?")
            sys.argv[2] = ans
            print("Welcome " + sys.argv[2])
            print("for help with commands type help")
        except NameError as e:
            print(e)
        except IndexError as e:
            print("Index Error :", e)

    # Chami -- added 19-03-2018
    @staticmethod
    def set_number_of_command():
        try:
            print("Number of Command-line Arguements: ", len(sys.argv))
            print("You are working on : ", sys.argv[0])
        except NameError as e:
            print(e)
        except IndexError as e:
            print("Index Error :", e)