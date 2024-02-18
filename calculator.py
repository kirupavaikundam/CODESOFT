import os
import json

def load_tasks():
    # Function to load tasks from the tasks.json file
    if os.path.exists('tasks.json'):  # Check if the file exists
        with open('tasks.json', 'r') as file:  # Open the file in read mode
            tasks = json.load(file)  # Load tasks from the file
        return tasks  # Return the loaded tasks
    else:
        return []  # Return an empty list if the file doesn't exist

def save_tasks(tasks):
    # Function to save tasks to the tasks.json file
    with open('tasks.json', 'w') as file:  # Open the file in write mode
        json.dump(tasks, file)  # Write tasks to the file in JSON format

def show_tasks():
    # Function to display the tasks
    tasks = load_tasks()  # Load tasks
    if not tasks:
        print("No tasks found.")  # If no tasks found, print a message
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")  # Display each task with its index

def add_task(task):
    # Function to add a task
    tasks = load_tasks()  # Load tasks
    tasks.append(task)  # Add new task
    save_tasks(tasks)  # Save tasks to file
    print(f"Task '{task}' added successfully.")

def remove_task(index):
    # Function to remove a task
    tasks = load_tasks()  # Load tasks
    if 1 <= index <= len(tasks):  # Check if the index is valid
        removed_task = tasks.pop(index - 1)  # Remove the task
        save_tasks(tasks)  # Save tasks to file
        print(f"Task '{removed_task}' removed successfully.")
    else:
        print("Invalid task index.")  # If index is invalid, print a message

def main():
    # Main function to run the To-Do List application
    while True:
        print("\n1. Show Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")  # Get user's choice

        if choice == '1':
            show_tasks()  # Display tasks
        elif choice == '2':
            task = input("Enter the task: ")  # Get new task from user
            add_task(task)  # Add the task
        elif choice == '3':
            index = int(input("Enter the task index to remove: "))  # Get index of task to remove
            remove_task(index)  # Remove the task
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")  # Exit the application
            break
        else:
            print("Invalid choice. Please enter a valid option.")  # If choice is invalid, print a message

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
