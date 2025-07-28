from datetime import datetime, timedelta
def display_current_datetime ():
    time_now = datetime.now()
    #print("Current date and time:", time_now.strftime("%Y-%m-%d %H:%M:%S"))
    return time_now
def calculate_future_date():
    future_date = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=future_date)
   #print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

current_date = display_current_datetime()
print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")
#display_current_datetime(current_date)
#print(current_date)


future_date = calculate_future_date()
print(f"Future date: {future_date.strftime("%Y-%m-%d")}")






     