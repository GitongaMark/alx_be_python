
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Try to address it soon."
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that should be done soon."
        else:
            reminder += ". Consider completing it in due time."
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " that you should consider doing soon."
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered."

print(f"\nReminder: {reminder}")