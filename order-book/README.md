# Order Book Application

A command-line Python application for managing software development task orders.

This application allows users to add programming tasks, assign them to programmers, track workload estimates, mark tasks as finished, and monitor programmer status.

The project was created as part of a Python programming exercise focused on:

- Object-oriented programming
- Lists and sets
- Command-line applications
- Error handling
- User input validation

---

# Features

- Add new programming tasks
- Assign tasks to programmers
- Automatically generate unique task IDs
- List finished tasks
- List unfinished tasks
- Mark tasks as finished
- View all programmers
- View programmer statistics:
  - finished tasks
  - unfinished tasks
  - completed workload hours
  - scheduled workload hours
- Handle invalid user input gracefully


---

# How to Run

Clone the repository:

```bash
git clone https://github.com/hangkimngo/order-book-applicationg.git
cd order-book-application
```

Run the application:

```bash
python3 order_book.py
```

---

# Available Commands

```text
0 exit
1 add order
2 list finished tasks
3 list unfinished tasks
4 mark task as finished
5 programmers
6 status of programmer
```

---

# Example Usage

## Adding Tasks

```text
command: 1
description: program the next facebook
programmer and workload estimate: jonah 1000
added!
```

---

## Listing Unfinished Tasks

```text
command: 3

1: program the next facebook (1000 hours), programmer jonah NOT FINISHED
2: program mobile app for workload accounting (25 hours), programmer eric NOT FINISHED
```

---

## Marking a Task as Finished

```text
command: 4
id: 2
marked as finished
```

---

## Checking Programmer Status

```text
command: 6
programmer: jonah

tasks: finished 1 not finished 1, hours: done 55 scheduled 1000
```

---

# Error Handling

The application validates user input and recovers from invalid commands or malformed input.

Examples of invalid input:

```text
programmer and workload estimate: eric xxx
erroneous input
```

```text
id: XXXX
erroneous input
```

```text
programmer: unknownprogrammer
erroneous input
```

---

# Project Structure

```text
order-book-application/
│
├── order_book.py
└── README.md
```

---

# Main Classes

## `Task`

Represents a single programming task.

Attributes include:

- task description
- programmer name
- workload estimate
- completion status
- unique task ID

---

## `OrderBook`

Manages all tasks and programmers.

Responsibilities include:

- storing tasks
- filtering finished/unfinished tasks
- marking tasks as completed
- generating programmer statistics

---

## `OrderBookApplication`

Handles the command-line user interface and user interaction.

