## @file AALst.py
#  @author Shesan Balachandran
#  @brief Abstract object of department allocations
#  @date 02/06/2019

from StdntAllocTypes import DeptT


## @brief An abstract data structure for the student allocation list
class AALst:

    ## @brief Initializer
    #  @details Initialize the student allocation list
    @staticmethod
    def init():
        AALst.s = []
        for d in DeptT:
            alloc_assoc_list_t = (d, [])
            AALst.s.append(alloc_assoc_list_t)

    ## @brief Add Student
    #  @details Adds a student into the corresponding department
    #  @param dep Name of the department
    #  @param m Macid of the student
    @staticmethod
    def add_stdnt(dep, m):
        for x in AALst.s:
            if x[0] == dep:
                x[1].append(m)
                break

    ## @brief Get allocated students
    #  @details Gets the allocated students of a department
    #  @param d Name of the department
    #  @return List of macids of the allocated student
    @staticmethod
    def lst_alloc(d):
        for x in AALst.s:
            if x[0] == d:
                return x[1]

    ## @brief Get number of allocations
    #  @details Gets the number of allocated students of a department
    #  @param d Name of the department
    #  @return Number of students allocated for a department
    @staticmethod
    def num_alloc(d):
        for x in AALst.s:
            if x[0] == d:
                return len(x[1])
