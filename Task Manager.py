class Task:
    def __init__ (self, name, priority):
        self.name = name
        self.priority = priority

    def __str__(self):
        return "Task: " + str(self.name) + "  Priority: " + str(self.priority)

class TaskManager:

    def __init__(self):
        self.tasks = []
        self.undo_stack = []

    def add_tasks(self, name, priority):
        task = Task(name, priority)
        self.tasks.append(task)
        self.sort_tasks()
        self.undo_stack.append(("add", task))
        print("New Task Added: " + str(task))

    def sort_tasks(self):
        self.tasks.sort(key=lambda task: task.priority)

    def completed_task(self):
        if not self.tasks:
            print("Task List is Empty.")
            return
        else:
            task = self.tasks.pop(0)
            self.undo.append('complete', task)
            print("Completed Task: , "+ str(task))

    def view_tasks(self):
        if not self.tasks:
            print("Task List is Empty")
        else:
            print("Tasks by Priority: ")
            count = 1
            for task in self.tasks:
                print(str(count) + ". " + str(task))
                count += 1

    def remove_first(self):
        if not self.tasks:
            print("Task List is Empty")
        else:
            task = self.tasks.pop(0)
            self.undo_stack.append(('remove', task, 'first'))
            print("Removed From Beginning: " + str(task))

    def remove_end(self):
        if not self.tasks:
            print("Task List is Empty")
        else:
            task = self.tasks.pop()
            self.undo_stack.append(('remove', task, 'end'))
            print("Removed From Beginning: " + str(task))

    def undo(self):
        if not self.undo_stack:
            print("Nothing to Undo.")
            return
        action = self.undo_stack.pop()

        if action[0] == 'add':
            task = action[1]
            self.tasks = [t for t in self.tasks if t != task]
            print("Undo Add: " + str(task))
        elif action[0] == 'complete':
            task = action[1]
            self.tasks.append(task)
            self.sort_by_priority()
            print("Undo Complete: " + str(task))
        elif action[0] == 'remove':
            task = action[1]
            direction = action[2]
            if direction == 'front':
                self.tasks.insert(0, task)
            else:
                self.tasks.append(task)
            self.sort_by_priority()
            print("Undo Remove from " + direction + ": " + str(task))

def main():
    list= TaskManager()
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Highest Priority Task")
        print("4. Remove from Front")
        print("5. Remove from Back")
        print("6. Undo Last Action")
        print("7. Exit")

        choice = input("Choose an Option: ")

        if choice == '1':
            name = input("Enter Task Name: ")
            try:
                priority = int(input("Enter Priority (1 = highest): "))
                list.add_tasks(name, priority)
            except ValueError:
                print("Invalid priority.")
        elif choice == '2':
            list.view_tasks()
        elif choice == '3':
            list.completed_task()
        elif choice == '4':
            list.remove_first()
        elif choice == '5':
            list.remove_end()
        elif choice == '6':
            list.undo()
        elif choice == '7':
            print("Quit Task Manager.")
            break
        else:
            print("Invalid Option.")


if __name__ == "__main__":
    main()
            

            
        

        
