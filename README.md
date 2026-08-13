# Study Tracker

**Created by Isabella Wang**

Study Tracker is my third Python project, created in VS Code. It is a simple study-tracking program that helps users keep track of their study tasks and the amount of time they spend studying.

The program stores completed study sessions in a JSON file and provides statistics about study time.

## Features

The program can:

* Let the user enter a study task and the amount of time they want to spend on it
* Start a countdown timer based on the user's input
* Store completed tasks and study times in a JSON file
* Organize study data by date
* Display statistics, including:

  * A summary of today's study
  * Total study time for today
  * Total study time across all recorded days
  * Average study time per day

## Files

### `main.py`

This is the main file of the program. It handles three main parts:

1. **Tasks and Timer** — Gets the task and study time from the user and runs the countdown timer.
2. **Data Storage** — Stores completed study sessions in `storage.json`.
3. **Statistics** — Calculates and displays statistics about the user's study time.

### `storage.json`

This file stores the user's study data.

It starts as an empty dictionary:

```json
{}
```

As the user completes study sessions, the program adds the data to the JSON file and organizes it by date.

For example:

```json
{
    "2026.08.06": {
        "math": 60,
        "coding": 90
    },
    "2026.08.07": {
        "reading": 30
    }
}
```

## How the Program Works

When `main.py` starts, the program displays a welcome message and explains what the Study Tracker does.

### 1. Getting Today's Date

The program uses:

```python
date = time.strftime("%Y.%m.%d")
```

This gets the current date and stores it in the `date` variable.

It then creates:

```python
today_data = {}
```

This dictionary stores the tasks and study times completed today.

The date is later used as a key in the JSON file.

### 2. Entering Tasks

The program uses a `while` loop to allow the user to enter multiple study tasks.

For each task, the user enters:

* The task name
* How many minutes they want to study

The program then starts a countdown timer using the amount of time entered by the user.

Once the timer finishes, the completed task and its study time are recorded.

### 3. Storing the Data

After the user's study sessions are completed, the program opens `storage.json` and updates it with the new data.

The study data is organized by date, with each date containing the tasks completed that day.

### 4. Calculating Statistics

Finally, the program calculates and displays several statistics:

* **Today's study summary**
* **Total study time today**
* **Total study time across all recorded days**
* **Average study time per day**

This allows the user to see both their daily progress and their overall study habits.

## What I Learned

While creating this project, I practiced several Python concepts, including:

* Functions
* Dictionaries
* Loops
* File handling
* JSON
* The `time` module
* User input
* Basic data analysis and calculations

This project also helped me practice organizing a larger Python program and working with data that needs to be saved between program runs.

