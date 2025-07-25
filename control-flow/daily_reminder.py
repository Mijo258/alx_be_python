task = input("enter task description : ")
priority = input("enter task priority (high/medium/low): ")
time_bound = input("is the task time-bound? (yes or no): ")
match priority : 
    case "high" :
        if time_bound == "yes" :
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound == "no" :
            print(f"Reminder: {task} is a high priority task. Consider completing it when you have free time.")
    case "medium" :
        if time_bound == "yes" :
            print(f"Reminder: {task} is a medium priority that task requires immediate attention today!")
        elif time_bound == "no" :
            print(f"Reminder: {task} is a medium priority task. Consider completing it when you have free time.")
    case "low" :
        if time_bound == "yes" :
            print(f"Reminder: {task} is a low priority task that requires immediate attention today!")
        elif time_bound == "no" :
            print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")