## @file StdntAllocTypes.py
#  @author Shesan Balachandran
#  @brief Library of types. Includes Gender, Department and Student type
#  @date 02/06/2019

import enum
import typing
from SeqADT import SeqADT


## @brief An abstract data type of genders
class GenT(enum.Enum):
    male = 1
    female = 2


## @brief An abstract data type of departments
class DeptT(enum.Enum):
    civil = 1
    chemical = 2
    electrical = 3
    mechanical = 4
    software = 5
    materials = 6
    engphys = 7


## @brief An abstract data type of student info
class SInfoT(typing.NamedTuple):
    fname: str
    lname: str
    gender: GenT
    gpa: float
    choices: SeqADT
    freechoice: bool
