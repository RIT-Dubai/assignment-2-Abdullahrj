import numpy as np
import csv
import plotter


def main():
        def help():
            print('stu <filename> <first name> <last name> - plot student grades\n cavg <filename> - plot class average\n avg <filename> <number> - prints the average for the grade item\n quit - quits\n help - displays this message')
            bye()

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
                    elif string[0] == 'help':
                        help()
                    elif string[0] == 'stu':

                            if len(string) != 4:
                                print('incorrect usage, "Usage: stu <filename> <last name> <first name>"')
                            else:
                                userfile = string[1]
                                first_name= string[3]
                                last_name= string[2]
                                param = ["stu", r"C:\Users\abdul\Downloads\GCIS.123.600-assignment2-sample.csv", "Altamimi", "Abdullah"]
                                student_average(["stu", userfile, last_name,first_name])
                    elif string[0] == 'avg':
                        if len(string) != 3:
                            print('incorrect usage: avg <filename> <grade item>')
                        else:
                            userfile = string[1]
                            gradeitem = string[2]
                            print_average(["avg",userfile,gradeitem])
                    elif string[0] == "cavg":
                        if len(string) != 2:
                            print('incorrect usage: cavg <filename>')
                        else:
                            userfile = string[1]
                            class_average(['cavg',userfile])
                except IndexError:
                    user = input("enter a command or 'quit' to quit")
                    quits()
        def student_average(param):
            plotter.plot(trace_plot=True)
            f = param[1]
            if len(param) != 4:
                print("Usage: stu <filename> <first name> <last name>")
                bye()
            elif len(param) == 4:
                        csv_file = open(f)
                        csv_reader = csv.reader(csv_file)
                        firstname = param[3]
                        lastname = param[2]
                        for row in csv_reader:
                            try:
                                    while firstname in row:
                                            if lastname in row:
                                                try:
                                                    plot = row[2:]
                                                    plotter.init('my graph','x-axis','y-axis')

                                                    for i in range(len(plot)):
                                                        plotter.add_data_point(plot[i])
                                                        plotter.plot()
                                                        break
                                                    if plotter.plot() == True:
                                                        print('Plotting complete. (window may be hidden)')
                                                        break
                                                    elif plotter.plot() == False:
                                                        print('Plot failed. (student not found)')
                                                        break
                                                except:
                                                    print('Plot failed')
                                                    break
                            except:
                                print('name not found')






        def class_average(cavg):

            f = open(cavg[1],"r")
            next(f)
            average = 0
            Sum = 0
            row_count = 0
            for row in f:
                    for column in row.split(','):
                        try:
                                x = float(column)
                                Sum += x
                                row_count += 1


                        except ValueError:
                            pass
            print("Avg =",Sum/row_count)


















        def print_average(avg):
            csv=avg[1]
            f = open(csv)
            average=0
            Sum = 0
            column= 12
            for i in range(0,column):
                for n in range(i):
                    n=float(n)
                    Sum += n
            average = Sum / 12
            print(average)





        bye()



if __name__ == '__main__':
    main()












