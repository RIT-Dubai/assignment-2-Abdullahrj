import os.path
import csv
import plotter


def main():
    def student_average(param):
            param = ["stu", r"C:\Users\abdul\Downloads\GCIS.123.600-assignment2-sample.csv", "Altamimi",'Abdullah']
            f = param[1]
            if len(param) != 4:
                print("Usage: stu <filename> <first name> <last name>")
                student_average(["stu", r"C:\Users\abdul\Downloads\GCIS.123.600-assignment2-sample.csv", "Altamimi",'Abdullah'])
            elif len(param) == 4:
                try:
                    csv_file = open(f)
                    csv_reader = csv.reader(csv_file)
                    firstname = param[3]
                    lastname = param[2]
                    for row in csv_reader:
                        try:
                            while firstname in row:
                                if lastname in row:
                                    plot = row[2:]
                                    if plotter.add_data_point(plot) == True:
                                        print('Plotting complete. (window may be hidden)')
                                        break
                                    elif plotter.add_data_point(plot) == False:
                                        print('Plot failed. (student not found)')
                                        break

                        except:
                            print('name not found in csv file')
                            break



                except:
                    print('file does not exist')

            else:
                print('file does not exist')
            if plotter.plot(param) == True:
                    print('Plot finished, window may be hidden.')
            elif plotter.plot(param) == False:
                    print('Plot failed, no such student.')



    def print_average(string):
            string = input('enter ')

            #quit function
    def quits():
            sure = input("are you sure?")
            while sure == 'y':
                print('goodbye!')
                return True
            while sure == 'Y':
                print('goodbye!')
                return True
            else:
                return False
    def bye():
        user = input(">>")
        string = user.split()
        try:
            if string[0] == "quit":
                while quits() == True:
                    break
            if string[0] == 'stu':
                    student_average(["stu",r"C:\Users\abdul\Downloads\GCIS.123.600-assignment2-sample.csv","Altamimi","Abdullah"])
        except:
            if user == "":
                user = input("enter a command or 'quit' to quit")
                quits()
    bye()


main()











