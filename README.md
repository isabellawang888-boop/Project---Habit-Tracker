# Project---Habit-Tracker
Habit Tracker is a Python application designed to help users build and maintain daily habits by tracking completion, streaks, and progress over time.

Hi, this is my third project I created on VScode, this program is a easy study tracker. This program is design for the user to keep track of their study time and study task and have a statistic about the average/total study time in a specific range of days.

This program can:
    - Let user input their task name, and the time of the task they want to spend on
    - Start a countdown timer(the timer start with the time that user input)
    - Stores the data of user's completed task and time in a json file and organized by date, 
    - Print out a statistc of:
        - Summary of todays study
        - Total study time today
        - Total study time from all days in json file
        - Average study time per day

Files:

  main.py: For the main.py, it has three different section: task(timer), put the data into storage.json, the statistic(calculations).
  storage.json: Only have a curly bracket inside - {}, but the main.py import the json file and put data inside.


Detailed explanation of how the program work:
    
Right after the program(file main.py) runs, it prints a few welcoming message. A brief explanation of what this program is. After the welcoming message, I write  --> date = time.strftime("%Y.%m.%d"), and --> today_data = {}, this is to get today's date, this date will be the key of the value(today's data) in the json file. Meanwhile the todays data(the dictionary I created) stores the study tasks and time.
A While Loop at line 20 will run forever until the user have no more task to do, in the loop: It ask the user to input their task and time spend on the task, then starts the timer. 
At line 45, I wrote the code for opening the storage.json file. Naming it as f, put the data of today's study in.
Finally, the program will perform soem caluclation about Summary of todays study, total study time today, Total study time from all days in json file, Average study time per day. 
