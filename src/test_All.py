## @file test_All.py
#  @author Shesan Balachandran
#  @brief Test Module for SeqADT, DCapALst, SALst
#  @date 02/06/2019

import pytest

from SeqADT import SeqADT
from StdntAllocTypes import DeptT, GenT, SInfoT
from DCapALst import DCapALst
from AALst import AALst
from SALst import SALst


class TestSeqADT:
    def test_constructor(self):
        seq = SeqADT([DeptT.civil, DeptT.chemical])
        assert vars(seq) == {'_SeqADT__i': 0, '_SeqADT__s': [DeptT.civil, DeptT.chemical]}

    def test_start(self):
        seq = SeqADT([DeptT.civil])
        seq.next()
        seq.start()
        assert vars(seq) == {'_SeqADT__i': 0, '_SeqADT__s': [DeptT.civil]}

    def test_next(self):
        seq = SeqADT([DeptT.civil, DeptT.chemical])
        assert seq.next() == DeptT.civil
        assert seq.next() == DeptT.chemical

    def test_next_raises_stop_iteration(self):
        seq = SeqADT([])
        with pytest.raises(StopIteration):
            seq.next()

    def test_end(self):
        seq = SeqADT([])
        seq2 = SeqADT([DeptT.civil])
        assert seq.end()
        assert not seq2.end()


class TestDCapALst:
    def test_init(self):
        DCapALst.init()
        assert DCapALst.s == []

    def test_elm(self):
        DCapALst.init()
        DCapALst.s.append((DeptT.chemical, 5))
        assert not DCapALst.elm(DeptT.civil)
        assert DCapALst.elm(DeptT.chemical)

    def test_add(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 5)
        assert DCapALst.s[0][0] == DeptT.civil
        assert DCapALst.s[0][1] == 5

    def test_add_raises_keyerror(self):
        DCapALst.init()
        DCapALst.s.append((DeptT.chemical, 3))
        with pytest.raises(KeyError):
            DCapALst.add(DeptT.chemical, 5)

    def test_remove(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 5)
        DCapALst.remove(DeptT.civil)
        assert DCapALst.s == []

    def test_remove_raises_keyerror(self):
        DCapALst.init()
        with pytest.raises(KeyError):
            DCapALst.remove(DeptT.chemical)

    def test_capacity(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 5)
        assert DCapALst.capacity(DeptT.civil) == 5

    def test_capacity_raises_keyerror(self):
        DCapALst.init()
        with pytest.raises(KeyError):
            DCapALst.capacity(DeptT.chemical)


class TestSALst:
    def test_init(self):
        SALst.init()
        assert SALst.s == []

    def test_elm(self):
        SALst.init()
        student_t = ('macid1', SInfoT('fname1', 'lname1', GenT.male, 4.0,
                                      SeqADT([DeptT.civil]), True))
        SALst.s.append(student_t)
        assert not SALst.elm('macid2')
        assert SALst.elm('macid1')

    def test_add(self):
        SALst.init()
        student_t = ('macid1', SInfoT('fname1', 'lname1', GenT.male, 4.0,
                                      SeqADT([DeptT.civil]), True))
        SALst.add(student_t[0], student_t[1])
        assert SALst.s[0][0] == student_t[0]
        assert SALst.s[0][1] == student_t[1]

    def test_add_raises_keyerror(self):
        SALst.init()
        student_t = ('macid1', SInfoT('fname1', 'lname1', GenT.male, 4.0,
                                      SeqADT([DeptT.civil]), True))
        SALst.s.append(student_t)
        with pytest.raises(KeyError):
            SALst.add('macid1', ())

    def test_remove(self):
        SALst.init()
        student_t = ('macid1', SInfoT('fname1', 'lname1', GenT.male, 4.0,
                                      SeqADT([DeptT.civil]), True))
        SALst.s.append(student_t)
        SALst.remove('macid1')
        assert SALst.s == []

    def test_remove_raises_keyerror(self):
        SALst.init()
        with pytest.raises(KeyError):
            SALst.remove('macid1')

    def test_info(self):
        SALst.init()
        student_t = ('macid1', SInfoT('fname1', 'lname1', GenT.male, 4.0,
                                      SeqADT([DeptT.civil]), True))
        SALst.s.append(student_t)
        assert SALst.info('macid1') == student_t[1]

    def test_info_raises_keyerror(self):
        SALst.init()
        with pytest.raises(KeyError):
            SALst.info('macid1')

    def test_sort(self):
        SALst.init()
        student_t1 = ('macid1', SInfoT('fname1', 'lname1', GenT.male, 4.0,
                                       SeqADT([DeptT.civil]), True))
        student_t2 = ('macid2', SInfoT('fname2', 'lname2', GenT.male, 3.0,
                                       SeqADT([DeptT.civil]), True))
        student_t3 = ('macid3', SInfoT('fname3', 'lname3', GenT.male, 12.0,
                                       SeqADT([DeptT.civil]), False))
        student_t4 = ('macid4', SInfoT('fname4', 'lname4', GenT.male, 7.0,
                                       SeqADT([DeptT.civil]), False))
        SALst.s.append(student_t1)
        SALst.s.append(student_t2)
        SALst.s.append(student_t3)
        SALst.s.append(student_t4)
        assert SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0) == ['macid1']
        assert SALst.sort(lambda t: not t.freechoice and t.gpa >= 4.0) == ['macid3', 'macid4']

    def test_sort_no_student_meet_requirement(self):
        SALst.init()
        student_t1 = ('macid1', SInfoT('fname1', 'lname1', GenT.male, 4.0,
                                       SeqADT([DeptT.civil]), False))
        student_t2 = ('macid2', SInfoT('fname2', 'lname2', GenT.male, 7.0,
                                       SeqADT([DeptT.civil]), False))
        SALst.s.append(student_t1)
        SALst.s.append(student_t2)
        assert SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0) == []

    def test_average(self):
        SALst.init()
        student_t1 = ('macid1', SInfoT('fname1', 'lname1', GenT.male, 4.0,
                                       SeqADT([DeptT.civil]), True))
        student_t2 = ('macid2', SInfoT('fname2', 'lname2', GenT.male, 12.0,
                                       SeqADT([DeptT.civil]), False))
        student_t3 = ('macid3', SInfoT('fname3', 'lname3', GenT.female, 7.0,
                                       SeqADT([DeptT.civil]), False))
        SALst.s.append(student_t1)
        SALst.s.append(student_t2)
        SALst.s.append(student_t3)
        expected_male_avg = 8.0
        tested_male_avg = SALst.average(lambda x: x.gender == GenT.male)
        assert abs(expected_male_avg - tested_male_avg) < 0.000001

    def test_average_raises_valueerror(self):
        SALst.init()
        student_t1 = ('macid1', SInfoT('fname1', 'lname1', GenT.male, 4.0,
                                       SeqADT([DeptT.civil]), True))
        student_t2 = ('macid3', SInfoT('fname3', 'lname3', GenT.male, 12.0,
                                       SeqADT([DeptT.civil]), False))
        SALst.s.append(student_t1)
        SALst.s.append(student_t2)
        with pytest.raises(ValueError):
            SALst.average(lambda x: x.gender == GenT.female)

    def test_allocate(self):
        AALst.init()
        DCapALst.init()
        SALst.init()
        DCapALst.s.append((DeptT.civil, 2))
        DCapALst.s.append((DeptT.chemical, 2))
        student_t1 = ('macid1', SInfoT('fname1', 'lname1', GenT.male, 3.0,
                                       SeqADT([DeptT.civil, DeptT.chemical]), True))
        student_t2 = ('macid2', SInfoT('fname2', 'lname2', GenT.male, 12.0,
                                       SeqADT([DeptT.civil, DeptT.chemical]), False))
        student_t3 = ('macid3', SInfoT('fname3', 'lname3', GenT.male, 4.0,
                                       SeqADT([DeptT.civil, DeptT.chemical]), True))
        student_t4 = ('macid4', SInfoT('fname4', 'lname4', GenT.male, 7.0,
                                       SeqADT([DeptT.civil, DeptT.chemical]), False))
        SALst.s.append(student_t1)
        SALst.s.append(student_t2)
        SALst.s.append(student_t3)
        SALst.s.append(student_t4)
        SALst.allocate()
        assert AALst.lst_alloc(DeptT.civil) == ['macid3', 'macid2']
        assert AALst.lst_alloc(DeptT.chemical) == ['macid4']

    def test_allocate_raises_runtimeerror(self):
        AALst.init()
        DCapALst.init()
        SALst.init()
        DCapALst.s.append((DeptT.civil, 2))
        student_t1 = ('macid1', SInfoT('fname1', 'lname1', GenT.male, 6.0,
                                       SeqADT([DeptT.civil]), True))
        student_t2 = ('macid2', SInfoT('fname2', 'lname2', GenT.male, 12.0,
                                       SeqADT([DeptT.civil]), False))
        student_t3 = ('macid3', SInfoT('fname3', 'lname3', GenT.male, 4.0,
                                       SeqADT([DeptT.civil]), False))
        SALst.s.append(student_t1)
        SALst.s.append(student_t2)
        SALst.s.append(student_t3)
        with pytest.raises(RuntimeError):
            SALst.allocate()
