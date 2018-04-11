import pandas as pd
import csv
import os


class Filer:
    """A class to load and sale data from CSV, XLSX and TXT file."""

    # Jonno's
    @staticmethod
    def read_excel(file_name):
        special_char = "\|!#$%&/()=?»«@£§€{};'<>,"
        for character in file_name:
            if character in special_char:
                raise NameError
        xl = pd.ExcelFile(file_name)
        print(xl.sheet_names)
        print(xl.parse('Sheet1'))
        df = pd.read_excel(file_name, sheet_name='Sheet1')
        content = df.values.tolist()
        for employee in content:
            if not isinstance(employee[6], str):
                employee[6] = employee[6].strftime("%d-%m-%Y")
        print(content)
        return content

    @staticmethod
    def save_excel(file_name, employee_list):
        special_char = "\|!#$%&/()=?»«@£§€{};'<>,"
        for character in file_name:
            if character in special_char:
                raise NameError
        if os.path.isfile(file_name):
            raise FileExistsError('file already exists, please rename')
        df = pd.DataFrame.from_records(employee_list)
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
        df.to_excel(writer, index=False, header=False, sheet_name='Sheet1')
        writer.save()
        print("Data is saved")

    # Renees:
    @staticmethod
    def read_csv(file_name):
        """
        >>> Filer.read_csv('notFile.csv')
        Traceback (most recent call last):
        ...
        FileNotFoundError: No such file or directory

        >>> Filer.read_csv('test_renee.csv')
        [['EMPID', 'GENDER', 'AGE', 'SALES', 'BMI', 'SALARY', 'BIRTHDAY'], ['A001', 'M', '26', '200', 'Normal', '20', '08-10-1991'], ['A002', 'F', '26', '300', 'Normal', '30', '09-10-1991']]
        """
        try:
            if os.path.isfile(file_name):
                with open(file_name, newline='') as file_data:
                    reader = csv.reader(file_data)
                    content = list(reader)
                    return content
            else:
                raise FileNotFoundError
        except NameError as e:
            print(e)
        except FileNotFoundError:
            raise FileNotFoundError('No such file or directory')
        except OSError:
            raise OSError('can not open the file', file_name)
        except IndexError as e:
            print(e)
        except TypeError as e:
            print('read_csv() missing 1 required argument: file_name')
        except Exception as e:
            print('there is something wrong', file_name)

    @staticmethod
    def save_csv(file_name, employee_list):
        """
        >>> Filer.save_csv('saveFile.csv',[('A001', 'M', 26, 200, 'Normal', 20, '08-10-1991'), ('A002', 'F', 26, 300, 'Normal', 30, '09-10-1991')])
        Data is saved

        >>> Filer.read_csv('saveFile.csv')
        [['A001', 'M', '26', '200', 'Normal', '20', '08-10-1991'], ['A002', 'F', '26', '300', 'Normal', '30', '09-10-1991']]

        >>> Filer.save_csv('saveFile1.csv')
        Traceback (most recent call last):
        ...
        TypeError: save_csv() missing 1 required positional argument: 'employee_list'

        >>> Filer.save_csv('#######.csv', [1,2,3])
        can not save the file #######.csv

        """
        try:
            special_char = "\|!#$%&/()=?»«@£§€{};'<>,"
            for character in file_name:
                if character in special_char:
                    raise NameError
            if os.path.isfile(file_name):
                raise FileExistsError('file already exists')
            df = pd.DataFrame(employee_list)
            df.to_csv(file_name, index=False, header=False)
            print("Data is saved")
        except TypeError as e:
            raise TypeError('save_csv() missing argument: ', employee_list)
        except OSError as e:
            print(e)
        except IndexError as e:
            print(e)
        except Exception as e:
            print('can not save the file', file_name)

    # Chamillas:
    @staticmethod
    def read_txt(file_name):
        """
        >>> Filer.read_txt('noFile.txt')
        Traceback (most recent call last):
        FileNotFoundError: [Errno 2] No such file or directory: 'noFile.txt'

        >>> Filer.read_txt('')
        Traceback (most recent call last):
        FileNotFoundError: [Errno 2] No such file or directory: ''

        >>> Filer.read_txt()
        Traceback (most recent call last):
        TypeError: read_txt() missing 1 required positional argument: 'file_name'

        >>> Filer.read_txt(10)
        Traceback (most recent call last):
        OSError: [WinError 6] The handle is invalid

        >>> Filer.read_txt($$@#&)
        Traceback (most recent call last):
        SyntaxError: invalid syntax

        >>> Filer.read_txt('noFile.txt','noFile.txt')
        Traceback (most recent call last):
        TypeError: read_txt() takes 1 positional argument but 2 were given

        """

        with open(file_name, "r+") as fo:
            data = [line.split("$") for line in fo]
        return data

    @staticmethod
    def save_txt_file(file_name, employee_list):
        """
        # Chami -- added 19-03-2018
        >>> Filer.save_txt_file('saveFile.txt',[('A001', 'M', 26, 200, 'Normal', 20, '08-10-1991'), ('A002', 'F', 26, 300, 'Normal', 30, '09-10-1991')])
        Data saved to file

        >>> Filer.save_txt_file('saveFile1.txt')
        Traceback (most recent call last):
        TypeError: save_txt_file() missing 1 required positional argument: 'employee_list'

        >>> Filer.save_txt_file([('A001', 'M', 26, 200, 'Normal', 20, '08-10-1991'), ('A002', 'F', 26, 300, 'Normal', 30, '09-10-1991')])
        Traceback (most recent call last):
        TypeError: save_txt_file() missing 1 required positional argument: 'employee_list'

        # >>> Filer.save_txt_file('',[('A001', 'M', 26, 200, 'Normal', 20, '08-10-1991'), ('A002', 'F', 26, 300, 'Normal', 30, '09-10-1991')])
        # Can not save file

        >>> Filer.save_txt_file(saveFile1,[('A001', 'M', 26, 200, 'Normal', 20, '08-10-1991'), ('A002', 'F', 26, 300, 'Normal', 30, '09-10-1991')])
        Traceback (most recent call last):
        NameError: name 'saveFile1' is not defined

        >>> Filer.save_txt_file('saveFile1.txt',[('', '', , , '', , ''), ('A002', 'F', 26, 300, 'Normal', 30, '09-10-1991')])
        Traceback (most recent call last):
        SyntaxError: invalid syntax

        >>> Filer.save_txt_file('saveFile1.txt',('A001', 'M', 26, 200, 'Normal', 20, '08-10-1991'), ('A002', 'F', 26, 300, 'Normal', 30, '09-10-1991'))
        Traceback (most recent call last):
        TypeError: save_txt_file() takes 2 positional arguments but 3 were given

        >>> Filer.save_txt_file()
        Traceback (most recent call last):
        TypeError: save_txt_file() missing 2 required positional arguments: 'file_name' and 'employee_list'

        """
        try:
            with open(file_name, "w") as f:
                for item in employee_list:
                    for i in item:
                        f.write(str(i)+'$')
                    f.write("\n")
                f.close()
                print("Data saved to file")
        except NameError as e:
            print(e)
        except OSError:
            print("Can not save file", file_name)
        except IndexError as e:
            print(e)
        except Exception as e:
            print(e)
        except Exception as e:
            print("Something went wrong: " + e)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
