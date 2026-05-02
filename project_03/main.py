import json
from pathlib import Path

file_name = Path(__file__).parent / "todo_list.json"

def load_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        init_data = {"tasks": []}
        try:
            with open(file_name, "w") as file:
                json.dump(init_data, file, indent=4)
                return init_data
        except PermissionError:
            print("An error occurred when trying to create file.")
            return None

def save_data(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file, indent=4)
    except PermissionError:
        print("An error occurred when trying to save file.")

def add_task(tasks):
    task = input("Write new task here: ")
    last_index = tasks["tasks"][-1]["index"]
    tasks["tasks"].append({"index": last_index + 1, "description": task, "status": False})
    try:
        save_data(tasks)
        print("------------------------------")
        print(f"Task num {last_index + 1} saved.")
        print("------------------------------")
    except PermissionError:
        print("An error occurred when trying to save file.")

def print_tasks(tasks):
    task_list = tasks["tasks"]
    print("------------------------------")
    for task in task_list:
        status = "[Completed \u2714]" if task["status"] else "[Pending...]"
        print(f"{task["index"]}. {task["description"]} | {status}")
    print("------------------------------")

def mark_completed(tasks, task_index):
    try:
        task_list = tasks["tasks"]
        task_num = int(task_index)
        for task in task_list:
            if task["index"] == task_num:
                task["status"] = True
                save_data(tasks)
                print("------------------------------")
                print(f"Task {task_num} is completed.")
                print("------------------------------")
                break
        else:
            print("\nTask with that number does not exist.\n")
    except (ValueError, TypeError):
        print("\nEnter a number of desired task\n")

def delete_task(tasks, task_index):
    try:
        task_list = tasks["tasks"]
        task_num = int(task_index)
        for task in task_list:
            if task["index"] == task_num:
                task_list.remove(task)
                save_data(tasks)
                print("------------------------------")
                print(f"Task {task_num} is deleted.")
                print("------------------------------")
                break
        else:
            print("\nTask with that number does not exist.\n")
    except (ValueError, TypeError):
        print("\nEnter a number of desired task\n")

def main():
    tasks = load_data()
    print("This is a To-Do app. ", end="")
    while True:
        print("You can:")
        print("1) See saved tasks")
        print("2) Add new task")
        print("3) Pick a task and mark completed")
        print("4) Pick a task and delete")
        print("If you want to quit type q.")
        answer = input("What would you like to do? ")
        if answer == "1":
            print_tasks(tasks)
        elif answer == "2":
            add_task(tasks)
        elif answer == "3":
            task_index = input("What task would you like to mark completed? ")
            mark_completed(tasks, task_index)
        elif answer == "4":
            task_index = input("What task would you like to delete? ")
            delete_task(tasks, task_index)
        elif answer == "q":
            print("Thank you. Goodbye!")
            break

if __name__ == "__main__":
    main()
