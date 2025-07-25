Task = input("enter task description : ")

Time_Bound = input("is the task time-bound? (yes or no): ")
Priority = input("enter task priority (high/medium/low): ")
match Priority : 
    case "high" :
        if Time_Bound == "yes" :
            print(f"Reminder: {Task} is a high priority task that requires immediate attention today!")
        elif Time_Bound == "no" :
            print(f"Reminder: {Task} is a high priority task. Consider completing it when you have free time.")
    case "medium" :
        if Time_Bound == "yes" :
            print(f"Reminder: {Task} is a medium priority that task requires immediate attention today!")
        elif Time_Bound == "no" :
            print(f"Reminder: {Task} is a medium priority task. Consider completing it when you have free time.")
    case "low" :
        if Time_Bound == "yes" :
            print(f"Reminder: {Task} is a low priority task that requires immediate attention today!")
        elif Time_Bound == "no" :
            print(f"Reminder: {Task} is a low priority task. Consider completing it when you have free time.")