# daily_reminder.py

# Ask the user to enter a task description
task = input("Enter your task: ")

# Ask for the task's priority level
priority = input("Priority (high/medium/low): ").lower()

# Ask whether the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to determine the message based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# If the task is time-bound, add an extra message
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Otherwise, encourage to do it later
elif priority in ["medium", "low"]:
    reminder += ". Consider completing it when you have free time."

# Print the final customized reminder
print()
print(reminder)

