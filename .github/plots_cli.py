import os.path
def main():


    def student_average():
        param = input('enter file name, first name, last name')
        wparam = param.split()
        if len(wparam) != 3:
                print("Usage: stu <filename> <first name> <last name>")
                student_average()
        elif len(wparam) == 3:
            try:
                f = open(wparam[0])
            except:
                if os.path.isfile(f) == False:
                    print('file does not exist')
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

    #command function
    def bye():
        user = input(">>")
        string = user.split()
        try:
            if string[0] == "quit":
                while quits() == True:
                    break
            if string[0] == 'stu':
                student_average()
        except:
            if user == "":
                user = input("enter a command or 'quit' to quit")
                quits()








    bye()




main()
