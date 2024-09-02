"""
Khristin Schenk
SDEV-220 | Sept. 2nd, 2024

Module 2 Lab - Case Study: if...else and while

How it works:
Running this script will continuously process input until "ZZZ" is entered as the last name, after which it will terminate.
"""

while True:
    # Collecting student's last name
    last_name = input("Enter student's last name (type 'ZZZ' to exit): ")
    if last_name.upper() == 'ZZZ':
        break

    # Collecting student's first name
    first_name = input("Enter student's first name: ")

    # Full name concatenation
    full_name = f"{first_name} {last_name}"

    # Accepting and validating the GPA input
    try:
        gpa = float(input("Enter student's GPA: "))
    except ValueError:
        print("Invalid input for GPA. Please enter a valid numeric value.")
        continue

    # Checking if the student qualifies for the Dean's List or Honor Roll
    if gpa >= 3.5:
        print(f"{full_name} has made the Dean's List.")
    if gpa >= 3.25:
        print(f"{full_name} has made the Honor Roll.")