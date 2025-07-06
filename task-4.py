def todo_list_app():
    tasks = []
    
    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task(s)")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            # Add multiple tasks
            print("\nEnter tasks (separate by commas or new lines). Press Enter twice to finish.")
            new_tasks = []
            while True:
                task_input = input("> ").strip()
                if not task_input:
                    break
                # Split by commas or keep as is
                if "," in task_input:
                    new_tasks.extend([t.strip() for t in task_input.split(",") if t.strip()])
                else:
                    new_tasks.append(task_input)
            
            if new_tasks:
                tasks.extend(new_tasks)
                print(f"\nAdded {len(new_tasks)} task(s):")
                for task in new_tasks:
                    print(f"- {task}")
            else:
                print("No tasks were added.")
                
        elif choice == '2':
            # View all tasks
            if not tasks:
                print("Your to-do list is empty!")
            else:
                print("\nYour To-Do List:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                    
        elif choice == '3':
            # Remove a task
            if not tasks:
                print("No tasks to remove!")
                continue
                
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
                
            try:
                task_num = input("Enter task number to remove (or multiple numbers separated by commas): ")
                # Handle multiple removals
                to_remove = [int(num.strip()) for num in task_num.split(",") if num.strip().isdigit()]
                to_remove = sorted(set(to_remove), reverse=True)  # Remove duplicates and sort high to low
                
                removed = []
                for num in to_remove:
                    if 1 <= num <= len(tasks):
                        removed.append(tasks.pop(num - 1))
                
                if removed:
                    print("\nRemoved:")
                    for task in reversed(removed):  # Show in original order
                        print(f"- {task}")
                else:
                    print("No valid tasks were removed!")
            except ValueError:
                print("Please enter valid numbers!")
                
        elif choice == '4':
            # Exit
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1-4.")

# Run the app
if __name__ == "__main__":
    todo_list_app()