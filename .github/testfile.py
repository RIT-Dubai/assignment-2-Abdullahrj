import plots_cli
def test_student_average(stu):
    stu = ["stu",r"C:\Users\abdul\Downloads\GCIS.123.600-assignment2-sample.csv","Altamimi","Abdullah"]
    assert stu[0]
    assert stu[1]
    assert stu[2]
    assert stu[3]

def test_class_average(cavg):
    cavg = ['cavg',r'C:\Users\abdul\Downloads\GCIS.123.600-assignment2-sample.csv']
    assert plots_cli.class_average == 51
def test_print_average(avg):
    avg = [r"C:\Users\abdul\Downloads\GCIS.123.600-assignment2-sample.csv",9]
    assert avg == True
def test_quits():
    if plots_cli.main().sure == "y" or "Y":
        assert print('goodbye!')
