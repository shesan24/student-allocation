## @file SeqADT.py
#  @author Shesan Balachandran
#  @brief Abstract data type representing the student choice list
#  @date 02/06/2019


## @brief An abstract data type that represents the student's choice list
class SeqADT():
    ## @brief Constructor of the SeqADT type
    #  @details Constructs the SeqADT data type.
    #  @param x List of departments
    def __init__(self, x):
        self.__s = x
        self.__i = 0

    ## @brief Reset current index.
    # @details Sets the current index to start of list (so 0)
    def start(self):
        self.__i = 0

    ## @brief Check for end of listt
    #  @details Identifies whether the current index of the list is at the end
    #  @return  True or False based on whether the current index is at the end of list
    def end(self):
        return self.__i >= len(self.__s)

    ## @brief Get element at the current index
    #  @details Returns the value at the current index and increments the index by one
    #  @exception throws StopIteration if current index has already reached
    #  the end of the list
    #  @return Value of the item at the current index
    def next(self):
        if self.end():
            raise StopIteration
        else:
            curr_item = self.__s[self.__i]
            self.__i = self.__i + 1
            return curr_item
