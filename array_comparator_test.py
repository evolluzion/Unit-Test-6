import pytest
from array_comparator import ArrayComparator

def test_compare_arrays_equal():
    comparator = ArrayComparator([6, 5, 4], [4, 5, 6])
    assert comparator.compare_arrays() == "Средние значения равны"

def test_compare_arrays_first_bigger():
    comparator = ArrayComparator([4, 5, 6], [1, 2, 3])
    assert comparator.compare_arrays() == "Первый список имеет большее среднее значение"

def test_compare_arrays_second_bigger():
    comparator = ArrayComparator([1, 2, 3], [4, 5, 6, 7, 8])
    assert comparator.compare_arrays() == "Второй список имеет большее среднее значение"

def test_compare_arrays_empty():
    comparator = ArrayComparator([], [])
    assert comparator.compare_arrays() == "Средние значения равны"

def test_compare_arrays_zeros():
    comparator = ArrayComparator([0, 0, 0], [0, 0])
    assert comparator.compare_arrays() == "Средние значения равны"
    
def test_compare_arrays_negative_numbers():
    comparator = ArrayComparator([-1, -2, -3], [1, 2, 3])
    assert comparator.compare_arrays() == "Второй список имеет большее среднее значение"

def test_compare_arrays_float_numbers():
    comparator = ArrayComparator([1.5, 2.5, 3.5], [1.2, 2.2, 3.2])
    assert comparator.compare_arrays() == "Первый список имеет большее среднее значение"
    
def test_compare_arrays_one_empty():
    comparator = ArrayComparator([1, 2, 3], [])
    assert comparator.compare_arrays() == "Первый список имеет большее среднее значение"
    
def test_compare_arrays_same_average_different_length():
    comparator = ArrayComparator([1, 2, 3], [1, 2, 2, 3])
    assert comparator.compare_arrays() == "Средние значения равны"