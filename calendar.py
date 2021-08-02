### this calender will update the info of the user and the user can delete the date/time and update the events in the calender###
from time import sleep, strftime
first_name="Louis"
welcome="welcome to calender, "
def welcome():
  print str(welcome) + first_name
  print "Calender starting..."
  sleep(1)
  print "Today is: "+ strftime("%A %B %d,%Y")
  print "Current time is: "+strftime("%H:%M:%S")
  sleep(1)
  print "What would you like to do?"

calendar={}
def start_calendar():
  welcome()
  start=True
  while start:
    user_choice=raw_input("A to add, U to Update, V to View, D to Delete, X to Exit. please enter: ")
    user_choice=user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print" The calendar is empty."
      else:
        print calendar
    elif user_choice =="U":
      date=raw_input("What date?: ")
      update=raw_input("Enter the update: ")
      calendar[date]=update # need to check the repeaty
      print "update is successful"
      print calendar
    elif user_choice =="A":
      event=raw_input("Enter event: ")
      date=raw_input("Enter date(MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")): #take care of the invalid year
        print "Invalid date."
        try_again=raw_input("Try Again? Y for yes, N for No: ")
        if try_again == "Y":
          continue #will strat thr loop from the beginning again
        else:
          start=False # to exit the loop and quit the program
      else:
        calendar[date]=event
    elif user_choice =="D":
      if len(calendar.keys()) < 1:
        print "The calendar is empty."
      else:
        event="What event?: "
        for date in calendar.keys():
          if event== calendar[date]:
            del calendar[date]
            print "The event is successfully deleted"
          else:
            print "no event is found. "
    elif user_choice =="X":
      start= False
    else:
      print "Invalid command is entered."
      start = False

start_calendar()
