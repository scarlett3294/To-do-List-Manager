import csv
# Define an empty list to store tasks
tasks = []

# Main function to handle user input and program flow
def main():
    while True:
        print("\nTo-do List Manager")
        print()
        print("1. Add task")
        print("2. Complete task")
        print("3. Remove task")
        print("4. List all tasks and status")
        print("5. List pending tasks")
        print("6. List completed tasks")
        print("7. Export tasks to CSV")
        print("8. Quit To-do List Manager")
        print()
        choice = input("Enter id of your choice: ")
        print()

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            if tasks:
                list_all_tasks()
                print()
                while True:
                    task_index = input("Enter the task number to mark as completed/ (Enter 0 to go back to Menu): ")
                    if task_index != "0":
                        try:
                            task_index = int(task_index)
                            task_index -= 1
                            if task_index >= 0 and task_index < len(tasks):
                                complete_task(task_index)
                                break
                            else:
                                print("Try again with a valid task number")
                        except ValueError:
                            print("Try again with a valid task number")
                    else:
                        break
            else:
                print("No tasks.")
        elif choice == "3":
            if tasks:
                list_all_tasks()
                print()
                while True:
                    task_index = input("Enter the task number to remove/ (Enter 0 to go back to Menu): ")
                    if task_index != "0":
                        try:
                            task_index = int(task_index)
                            task_index -= 1
                            if task_index >= 0 and task_index < len(tasks):
                                remove_task(task_index)
                                break
                            else:
                                print("Try again with a valid task number")
                        except ValueError:
                            print("Try again with a valid task number")
                    else:
                        break
            else:
                print("No tasks.")
        elif choice == "4":
            list_all_tasks()
        elif choice == "5":
            list_pending_tasks()
        elif choice == "6":
            list_completed_tasks()
        elif choice == "7":
            export_to_csv()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")


# Function to add a task
def add_task(task):
    tasks.append({"description": task, "completed": False})

# Function to change the status of a task
def complete_task(index):
    if tasks[index]["completed"] == False:
        tasks[index]["completed"] = True
        print(f"Task {index + 1} marked as completed.")
    else:
        print(f"Task {index + 1} is already completed.")

# Function to remove a task
def remove_task(index):
    if tasks[index]["completed"] == False:
        answer = input("This task is still pending. Are you sure you want to remove it? (yes/no): ").lower()
        if answer == "yes":
            del tasks[index]
        else:
            print("Cancelled.")
    else:
        del tasks[index]

# Function to list all tasks and their status
def list_all_tasks():
    if tasks:
        for i, task in enumerate(tasks):
            description = task["description"]
            completed = task["completed"]
            print(f"{i + 1}. {description} - {'Completed' if completed else 'Pending'}")
    else:
        print("No tasks.")


# Function to list pending tasks
def list_pending_tasks():
    pending_tasks = [task for task in tasks if not task["completed"]]
    if pending_tasks:
        for i, task in enumerate(pending_tasks):
            description = task["description"]
            print(f"{i + 1}. {description}")
    else:
        print("No pending tasks.")

# Function to list completed tasks
def list_completed_tasks():
    completed_tasks = [task for task in tasks if task["completed"]]
    if completed_tasks:
        for i, task in enumerate(completed_tasks):
            description = task["description"]
            print(f"{i + 1}. {description}")
    else:
        print("No completed tasks.")

# Function to generate a CSV file with tasks and statuses
def export_to_csv():
    if tasks:
        with open("tasks.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task Description", "Status"])
            for task in tasks:
                description = task["description"]
                completed = "Completed" if task["completed"] else "Pending"
                writer.writerow([description, completed])
        print("Tasks exported to tasks.csv")
    else:
        print("No tasks to export.")

if __name__ == "__main__":
    main()
