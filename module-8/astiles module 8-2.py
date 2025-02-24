"""
Name: Andrew Stiles
Date: 2-23-2025
Assignment: Module 8.2 Assignment
Purpose: JSON Practice - Load, Modify, and Save JSON Data
Citation: N/A
"""

import json
import os
import time

# Define file path
filename = "student.json"

# Function to load student data from JSON file
def load_students():
    # Load student data from student.json file.
    try:
        with open(filename, "r") as file:
            students = json.load(file)
        return students
    except FileNotFoundError:
        print("Error: student.json file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: JSON file is not formatted correctly.")
        return []

# Function to print student list
def print_students(students, message):
    # Prints student list with a message
    print(f"\n{message}")
    for student in students:
        print(f"{student['F_Name']} {student['L_Name']} - ID: {student['Student_ID']} - Email: {student['Email']}")

# Function to append new student data
def add_student(students):
    # Appends a new student entry to the list.
    new_student = {
        "F_Name": "Andrew",
        "L_Name": "Stiles",
        "Student_ID": 999999,
        "Email": "astiles@live.com" 
    }
    students.append(new_student)
    return students

# Function to write updated student data back to JSON
def save_students(students):
    # Writes updated student list back to student.json.
    try:
        with open(filename, "w") as file:
            json.dump(students, file, indent=4)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

# Function to check if the file has changed
def check_file_updated(last_modified):
    # Check if the JSON file has been modified
    time.sleep(2)  # Simulate delay to detect file change
    new_modified = os.path.getmtime(filename)
    return new_modified > last_modified

# --- Main Program Execution ---
students = load_students()

# Display Original Student List
print_students(students, "Original Student List:")

# Append New Student Data
students = add_student(students)

# Display Updated Student List
print_students(students, "Updated Student List:")

# Notify User that File Will Update
print("\nUpdating student.json file...")

# Get last modified time BEFORE saving
last_modified = os.path.getmtime(filename) if os.path.exists(filename) else 0

# Save the updated student list
if save_students(students):
    print("Student data successfully written to student.json.")

# Check if file was updated correctly
if check_file_updated(last_modified):
    print("\nFile modification detected! The student.json file has been updated.")
else:
    print("\nFile update failure detected! student.json may not have been updated correctly.")

# Final printout before closing
print_students(students, "Final Student List Before Exit:")
