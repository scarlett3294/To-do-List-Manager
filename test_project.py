import pytest
from project import tasks, add_task, complete_task, remove_task, list_all_tasks, list_pending_tasks, list_completed_tasks

def test_add_task():
    add_task("Test Task A")  # Call the add_task function with the task description
    add_task("Test Task B")
    add_task("Test Task C")
    add_task("Test Task D")
    assert len(tasks) == 4

def test_complete_task():
    complete_task(0)  # Call the complete_task function with the task index
    assert tasks[0]["completed"] is True #
    complete_task(3)  # Call the complete_task function with the task index
    assert tasks[3]["completed"] is True #


def test_remove_task():
    remove_task(0)  # Call the remove_task function with the task index
    assert len(tasks) == 3

def test_list_all_tasks(capsys):
    list_all_tasks()  # Call the list_all_tasks function
    captured = capsys.readouterr()
    expected_output = "1. Test Task B - Pending\n2. Test Task C - Pending\n3. Test Task D - Completed\n"
    assert captured.out == expected_output

def test_list_pending_tasks(capsys):
    list_pending_tasks()  # Call the list_pending_tasks function
    captured = capsys.readouterr()
    expected_output = "1. Test Task B\n2. Test Task C\n"
    assert captured.out == expected_output

def test_list_completed_tasks(capsys):
    list_completed_tasks()  # Call the list_completed_tasks function
    captured = capsys.readouterr()
    expected_output = "1. Test Task D\n"
    assert captured.out == expected_output
