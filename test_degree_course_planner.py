import pytest
from tkinter import *
from tkinter import filedialog, messagebox
from unittest.mock import patch

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

'''# 3. Test execution with correct mock path
# NOTE: Replace 'main_file' with your actual module path if it isn't 'main_file.py'
@patch("main_file.messagebox.showwarning")
def test_check_pre_requisites(mock_warning, physics2_course):'''
@pytest.mark.parametrize("course_instance2", [physics2_course])
def test_check_pre_requisites(course_instance2):
    # check first conditional. Test for messagebox.showwarning
    with patch("degree_course_planner.messagebox.showwarning") as mock_warning:
        check_pre_requisites(course_instance2)

        # Assert that showwarning was called once
        mock_warning.assert_called_once()

        # Assert exact arguments passed: (title, message)
        mock_warning.assert_called_once_with(
            "Take Pre-requisite Course", f"Need to take pre-requisite course, {course_instance2.pre_requisites[0].abbreviation_name} {course_instance2.pre_requisites[0].abbreviation_number}, before taking {course_instance2.abbreviation_name} {course_instance2.abbreviation_number}."
        )

# print(f"\n{physics2_course.pre_requisites=}")
# test_check_pre_requisites(physics2_course)