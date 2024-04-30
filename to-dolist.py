class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                status = " [X]" if task["completed"] else " [ ]"
                print(f"{i}. {task['description']}{status}")

    def add_task(self, description):
        task = {"description": description, "completed": False}
        self.tasks.append(task)
        print(f"Task '{description}' added.")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print(f"Task '{self.tasks[task_index - 1]['description']}' marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task['description']}' deleted.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            todo_list.display_tasks()
        elif choice == "2":
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "5":
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
