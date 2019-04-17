## @file Read.py
#  @author Shesan Balachandran
#  @brief Library of functionalities like extracting student info, department info
#  @date 02/06/2019

from StdntAllocTypes import *
from DCapALst import DCapALst
from SALst import SALst


## @brief Read Student Data
#  @details Reads student information from text file
#  @param s The name of the file to be read
def load_stdnt_data(s):
    with open(s, 'r') as stdnt_data:
        contents = stdnt_data.readlines()

    SALst.init()

    dept_dict = {
        'civil': DeptT.civil,
        'chemical': DeptT.chemical,
        'software': DeptT.software,
        'electrical': DeptT.electrical,
        'engphys': DeptT.engphys,
        'materials': DeptT.materials,
        'mechanical': DeptT.mechanical
    }

    for line in contents:
        student_info = line.replace(' ', '').replace('[', '').replace(']', '')
        student_info = student_info.strip('\n').split(',')

        macid = student_info[0]
        fname = student_info[1]
        lname = student_info[2]

        gender = GenT.female
        if student_info[3] == 'male':
            gender = GenT.male

        gpa = float(student_info[4])

        tmp_choices = []
        for x in student_info[5:-1]:
            if x in dept_dict:
                tmp_choices.append(dept_dict.get(x))
        choices = SeqADT(tmp_choices)

        freechoice = False
        if student_info[-1] == 'True':
            freechoice = True

        sinfo = SInfoT(fname, lname, gender, gpa, choices, freechoice)

        SALst.add(macid, sinfo)


## @brief Read Department Capacity Data
#  @details Reads department capacity information from text file
#  @param s The name of the file to be read
def load_dcap_data(s):
    with open(s, 'r') as dept_capacity:
        contents = dept_capacity.readlines()

    DCapALst.init()

    dept_dict = {
        'civil': DeptT.civil,
        'chemical': DeptT.chemical,
        'software': DeptT.software,
        'electrical': DeptT.electrical,
        'engphys': DeptT.engphys,
        'materials': DeptT.materials,
        'mechanical': DeptT.mechanical
    }

    for line in contents:
        dept_info = line.replace(' ', '').split(',')
        dept = dept_dict.get(dept_info[0])
        cap = int(dept_info[1])
        DCapALst.add(dept, cap)
