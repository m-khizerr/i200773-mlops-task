import pytest
from main import StudentsInMLOps

def test_enrollStudents():
    StudentsInMLOps.enrollStudents(5)
    assert StudentsInMLOps.getTotalStrength() == 5

def test_dropStudents():
    StudentsInMLOps.enrollStudents(10)
    StudentsInMLOps.dropStudents(3)
    assert StudentsInMLOps.getTotalStrength() == 7

def test_getTotalStrength():
    assert StudentsInMLOps.getTotalStrength() == 0

def test_getClassName():
    assert StudentsInMLOps.getClassName() == "StudentsInMLOps"
