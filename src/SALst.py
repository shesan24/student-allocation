## @file SALst.py
#  @author Shesan Balachandran
#  @brief Abstract object for holding students and perfoming functions like allocation
#  @date 02/06/2019

from DCapALst import DCapALst
from AALst import AALst


## @brief An abstract data structure for the student info
class SALst:
    ## @brief Initializer
    #  @details Initialize the list of student info data structure
    @staticmethod
    def init():
        SALst.s = []

    ## @brief Add Student
    #  @details Adds a student to the list of student info data structure
    #  @param m Macid of the student
    #  @param i Student info as the student info type
    #  @exception throws KeyError if student already in list
    @staticmethod
    def add(m, i):
        if SALst.elm(m):
            raise KeyError
        else:
            student_t = (m, i)
            SALst.s.append(student_t)

    ## @brief Remove Student
    #  @details Removes a student from the list of student info data structure
    #  @param m Macid of the student
    #  @exception throws KeyError if student is not in list
    @staticmethod
    def remove(m):
        for x in SALst.s:
            if x[0] == m:
                SALst.s.remove(x)
                break
        else:
            raise KeyError

    ## @brief Check for student
    #  @details Checks if the student is in list of student info data structure
    #  @param m Macid of the student
    #  @return True or False based on whether the student is in the structure
    @staticmethod
    def elm(m):
        for x in SALst.s:
            if x[0] == m:
                return True
        else:
            return False

    ## @brief Get student info
    #  @details Gets information about a student from the list of the student
    #  info data structure
    #  @param m Macid of the student
    #  @exception throws KeyError if student is not in list
    #  @return Student info as the student info type
    @staticmethod
    def info(m):
        for x in SALst.s:
            if x[0] == m:
                return x[1]
        else:
            raise KeyError

    ## @brief Local/Helper Function
    #  @details Get student gpa
    #  @param m Macid of the student
    #  @param s List of the student info data structure
    @staticmethod
    def __get_gpa__(m, s):
        for x in s:
            if x[0] == m:
                return x[1].gpa

    ## @brief Local/Helper Function
    #  @details Partition students at a pivot, smaller GPAs to the left of pivot and
    # greater GPAs to the right of pivot
    #  @param arr List of the student info data structure
    #  @param first Index where partitioning starts
    #  @param last Index where partitioning ends
    @staticmethod
    def __partition__(arr, first, last):

        future_pivot = first - 1
        temp_pivot = SALst.__get_gpa__(arr[last], SALst.s)

        for i in range(first, last):
            if SALst.__get_gpa__(arr[i], SALst.s) >= temp_pivot:
                future_pivot += 1
                arr[future_pivot], arr[i] = arr[i], arr[future_pivot]

        future_pivot += 1
        arr[future_pivot], arr[last] = arr[last], arr[future_pivot]

        return future_pivot

    ## @brief Local/Helper Function
    #  @details Using the partition function, recursively sort the left and right
    # side at a pivot
    #  @param arr List of the student info data structure
    #  @param first Index where partitioning starts
    #  @param last Index where partitioning ends
    @staticmethod
    def __quicksort__(arr, first, last):
        if first < last:
            pivot = SALst.__partition__(arr, first, last)
            SALst.__quicksort__(arr, first, pivot - 1)
            SALst.__quicksort__(arr, pivot + 1, last)

    ## @brief Sorts Students
    #  @details Sort students in the list of student info data structure
    #  based on a requirement function(like filtering students)
    #  @param f requirement function
    #  @return List of student macids in sorted order
    @staticmethod
    def sort(f):
        sorted_students = []
        for x in SALst.s:
            if f(x[1]):
                sorted_students.append(x[0])
        SALst.__quicksort__(sorted_students, 0, len(sorted_students) - 1)
        return sorted_students

    ## @brief Get average
    #  @details Gets average of students in the list of student info data
    #  structure based on a requirement function (like filtering students)
    #  @param f Requirement function
    #  @exception throws ValueError if no students meet the requirement
    #  @return Average of filtered students
    @staticmethod
    def average(f):
        total_avg = 0
        filtered_list = []
        for stdnt in SALst.s:
            if f(stdnt[1]):
                filtered_list.append(stdnt)

        avg_count = len(filtered_list)

        if(avg_count == 0):
            raise ValueError
        else:
            for student in filtered_list:
                total_avg += student[1].gpa

        return total_avg / avg_count

    ## @brief Allocate students
    #  @details Allocate students in the list of student info data
    #  structure to the corresponding departments of choice depending on
    #  if they met the requirements
    #  @exception throws RunTimeError if a student meeting all the
    #  requirments could not be allocated into any of their department choices
    @staticmethod
    def allocate():
        AALst.init()

        f = SALst.sort(lambda t: (t.freechoice) and t.gpa >= 4.0)
        for m in f:
            ch = SALst.info(m).choices
            AALst.add_stdnt(ch.next(), m)

        s = SALst.sort(lambda t: (not t.freechoice) and t.gpa >= 4.0)
        for m in s:
            ch = SALst.info(m).choices
            alloc = False
            while (not alloc) and (not ch.end()):
                d = ch.next()
                if AALst.num_alloc(d) < DCapALst.capacity(d):
                    AALst.add_stdnt(d, m)
                    alloc = True
            if not alloc:
                raise RuntimeError
