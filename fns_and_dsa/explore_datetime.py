import datetime 
def display_current_datetime (time_now):
    time_now = datetime.datetime.now()
    print("Current date and time:", time_now.strftime("%Y-%m-%d %H:%M:%S"))
    return time_now
def calculate_future_date(future_date):
    future_date = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + datetime.timedelta(days=future_date)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

current_date = display_current_datetime(time_now=None)
#display_current_datetime(current_date)
#print(current_date)

future_date = None
calculate_future_date(future_date)







     