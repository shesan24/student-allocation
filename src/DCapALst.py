## @file DCapALst.py
#  @author Shesan Balachandran
#  @brief Abstract object of department capacity
#  @date 02/06/2019


## @brief An abstract data structure for the department capacity data
class DCapALst:

    ## @brief Initializer
    #  @details Initialize the department capacity data structure
    @staticmethod
    def init():
        DCapALst.s = []

    ## @brief Check for department
    #  @details Checks if the department is in the data structure
    #  @param d Name of the department
    #  @return True or False based on whether department in data structure
    @staticmethod
    def elm(d):
        for x in DCapALst.s:
            if x[0] == d:
                return True
        else:
            return False

    ## @brief Add Department
    #  @details Adds a department and it's capacity to the data structure
    #  @param d Name of the department
    #  @param n Capacity of the department
    #  @exception throws KeyError if department already in list
    @staticmethod
    def add(d, n):
        if DCapALst.elm(d):
            raise KeyError
        else:
            DCapALst.s.append((d, n))

    ## @brief Remove Department
    #  @details Removes a department and it's capacity from the data structure
    #  @param d Name of the department
    #  @exception throws KeyError if department is not in list
    @staticmethod
    def remove(d):
        for x in DCapALst.s:
            if x[0] == d:
                DCapALst.s.remove(x)
                break
        else:
            raise KeyError

    ## @brief Get Capacity
    #  @details Gets the capacity of a department
    #  @param d Name of the department
    #  @exception throws KeyError if department is not in list
    @staticmethod
    def capacity(d):
        for x in DCapALst.s:
            if x[0] == d:
                return x[1]
        else:
            raise KeyError
