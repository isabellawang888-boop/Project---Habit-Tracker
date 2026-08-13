import time
import json
def main():
    # Welcoming message
    print('Welcome to the study tracker program! This will help you track your study time and tasks.')
    time.sleep(1)
    print('You will get a detailed statistic of your study after you finish all the task you have today.')
    time.sleep(1)
    print('Now, let\'s get started!')

    date = time.strftime("%Y.%m.%d")  # Get today's date in YYYY.MM.DD format
    today_data = {}

    # While loop:
    while True:
        # Ask user the task they want to do and the time, then start a timer.
        task_name = input('Now, please input the task name you want to do now, enters one task only:  ')
        time.sleep(1)
        # Validate integer input for minutes
        while True:
            try:
                task_time = int(input('Now, please input the time you want to spend on this task, in minutes: '))
                if task_time <= 0:
                    print('Please enter a positive number of minutes.')
                    continue
                break
            except ValueError:
                print('Please enter a valid integer for minutes.')

        task_time_remaining = task_time   # Store the original task time for later use
        # Timer
        while task_time_remaining > 0:
            print(f'You have {task_time_remaining} minutes left for this task: {task_name}')
            time.sleep(60)  # Wait for 1 minute
            task_time_remaining -= 1

        print(f'Congratulation! You have finished task: {task_name} in {task_time} minutes.')
        today_data[task_name] = task_time # Update the today_data dict with the finished task
        time.sleep(1)
        user_choice = input('Do you have more task, (yes/no)?:  ')
        if user_choice.lower() == 'no':
            break  # Exit the while loop if user has no more task
    
    # While loop ends when user has no more task, update the dict to storage.json 
    try:
        with open("storage.json", "r") as f:
            storage = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        storage = {}

    # Merge today's tasks with existing entries for the date (if any)
    if date in storage and isinstance(storage[date], dict):
        storage[date].update(today_data)
    else:
        storage[date] = today_data

    with open("storage.json", "w") as f:
        json.dump(storage, f, indent=4)

    time.sleep(1)
    # Print the statistic of the study time and task for today

    # Summary
    print(f'Here is the statistic for {date}:')
    time.sleep(1)
    for task_name, task_time in today_data.items():
        print(f'Task: {task_name}, Time spent: {task_time} minutes')
        time.sleep(1)
    # Total study time today
    total_study_time = sum(today_data.values())
    print(f'This is your total study time for today: {total_study_time} minutes')
    time.sleep(1)
    # Total study time from all days
    # Compute total study time across all stored days
    total_study_time_from_past = 0
    for day_tasks in storage.values():
        if isinstance(day_tasks, dict):
            total_study_time_from_past += sum(day_tasks.values())

    if storage:
        dates_sorted = sorted(storage.keys())
        start_date, end_date = dates_sorted[0], dates_sorted[-1]
    else:
        start_date = end_date = date

    print(f'This is your total study time from {start_date} to {end_date}: {total_study_time_from_past} minutes')
    time.sleep(1)
    # Average study time per day
    average_study_time_per_day = (total_study_time_from_past / len(storage)) if len(storage) > 0 else 0
    print(f'This is your average study time per day: {average_study_time_per_day} minutes')
    

    # Program ends now
    print('Thank you for using my Study Tracker app!')
    print('Have a good day')

if __name__ == "__main__":
    main()
