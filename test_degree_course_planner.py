import pytest
from tkinter import *
from tkinter import filedialog, messagebox

from degree_course_planner import Course, check_pre_requisites, update_passing_course

physics_course = Course(
    'PHYS', 
    '2210', 
    'Physics for Scientists and Engineers I', 
    None, 
    ['P1', 'M1'], 
    False, 
    ['Spring', 'Fall'], 
    4, 
    22.50, 
    False, 
    grid_row= 1, 
    grid_column= 13
    )

physics2_course = Course(
    'PHYS', 
    '2220', 
    'Physics for Scientists and Engineers II', 
    None, 
    [physics_course], 
    False, 
    ['Spring'], 
    4, 
    33.50, 
    False, 
    grid_row= 1, 
    grid_column= 10
    )

@pytest.mark.parametrize("course_instance", [physics_course])
def test_update_passing_course(course_instance):
    update_passing_course(course_instance)
    assert course_instance.has_passed is True

# NOTE: pytest, esp. parametrize, does not need test functions to be called to find and run.
# test_update_passing_course(physics_course)