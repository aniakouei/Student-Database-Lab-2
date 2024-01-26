#Initialize a list of dictionaries to store student information
#Function to print names along with their position in the list
#Function to create a new student dictionary that asks for name, hometown and favorite food and adds to dictionary
#function to print student info as the user to input whether they want to know the hometown or favorite food and place an if statement with conditions based on input
#create function to be able to get student by name as well as number
#create a loop and if user input==add create a new student with function to create new student dictionary
#if user input==view then list the names of the students and call the print student function
#if statement to be able to call get student by name function
#if user input==quit end main loop and print goodbye message

students = [
    {"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
    {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
    {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}]
def list_names(students):
    for i in range(len(students)):
        print(f"{i + 1}. {students[i]['name']}")

def get_new_student():
    new_student = {}
    new_student["name"] = input("Enter the name of the new student: ")
    new_student["hometown"] = input("Enter the hometown of the new student: ")
    new_student["favorite_food"] = input("Enter the favorite food of the new student: ")
    return new_student

def print_student_info(student):
    print(f"Selected student: {student['name']}")
    info_choice = input("Type 'hometown' to see hometown or 'favorite food' to see favorite food: ")

    if info_choice == 'hometown':
        print(f"{student['name']}'s hometown is {student['hometown']}")
    elif info_choice == 'favorite food':
        print(f"{student['name']}'s favorite food is {student['favorite_food']}")
    else:
        print("Invalid choice.")
def get_student_by_name(students, name):
    for student in students:
        if student['name'].lower() == name.lower():
            return student


while True:
    user_input = input("Type 'add' to create a new student, 'view' to look at existing students, or 'quit' to exit: ")

    if user_input == "add":
        new_student = get_new_student()
        students.append(new_student)
        print("Student added successfully!")

    elif user_input == "view":
        list_names(students)
        student_choice = input("Enter the index or name of the student you want to select: ")

        if student_choice.isdigit():
            index = int(student_choice) - 1
            if 0 <= index < len(students):
                selected_student = students[index]
                print_student_info(selected_student)
            else:
                print("Invalid index.")
        else:
            selected_student = get_student_by_name(students, student_choice)
            if selected_student:
                print_student_info(selected_student)
            else:
                print("Student not found.")

    elif user_input == "quit":
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please enter 'add', 'view', or 'quit'.")
