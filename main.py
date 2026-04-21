#---------------------------------------------------------------------
#-------------------------Module 6 Assignment-------------------------
#---------------------------------------------------------------------


#---------------------------------------------------------------------
#----------------------Title: Simple Task Tracker---------------------
#---------------------------------------------------------------------

class TaskManager:
    """a simple Python class where users can manage their daily tasks."""
    def  __init__(self):
        self.tasks = []

    def add_task(self):
        """adds a task to the tasks list."""
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        self.tasks.append({"title": title, "description": description})
        print("Task added successfully!")

    def view_tasks(self):
        """prints all the tasks in the tasks list."""
        lines= "="*24
        print(f"\n{lines}\n"+" Task List ".center(24, "=")+f"\n{lines}")

        if not self.tasks:
            print("Task list is empty.".center(24, " "))

        for idx,task in enumerate(self.tasks,start=1):
            print("\n"+f" Task {idx} ".center(24, "-"))
            print(f"Title: {task['title']} \nDescription: {task['description']}")

    def delete_task(self):
        """deletes a task from the tasks list."""
        if not self.tasks:
            print("\nTask list is empty!\nPlease add a task first.")

        else:
            self.view_tasks()

            try:
                idx = int(input("\nEnter Task number to delete. (example: 1): "))
                del self.tasks[idx-1]
                print(f"Task {idx} deleted successfully!")
            except ValueError:
                print("Please enter a number.")
            except IndexError:
                print("Task not found.")


#-----------------------------Menu System-----------------------------
def menu_options():
    print("\n"+" Task Tracker ".center(24, "="))
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def menu_system(manager):
    while True:
        menu_options()
        try:
            choice = int(input("\nEnter choice: "))
            if choice == 1:
                manager.add_task()
            elif choice == 2:
                manager.view_tasks()
            elif choice == 3:
                manager.delete_task()
            elif choice == 4:
                print("Exit")
                break
            elif choice > 4:
                print("\nInvalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("\nInvalid choice. Please enter a number between 1 and 4.")


def main():
    manager = TaskManager()
    menu_system(manager)

if __name__ == "__main__":
    main()


