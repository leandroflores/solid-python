# Single Responsability Principle

## Introduction

In this chapter, we presents a overview and a practice of **S**ingle **R**esponsability **P**rinciple (**SRP**).

## Definition

*"There should never be more than a reason for a class to change"*

In other words, a **class** can be responsibilized for only one taks. For example: persistence, conditions, notification, logging, formatting, parsing, error handling. Therefore, a **class** must be deal with only one of this tasks.

## Practical Example

Considering the above example:

```python

class ToDoList:

    def __init__(self):
        self.tasks: list[str] = []

    def add_task(self, task: str) -> None:
        self.tasks.append(task)

    def delete_task(self, task: str) -> None:
        self.tasks.remove(task)

    def display_tasks(self) -> None:
        for task in self.tasks:
            print(task)

    def input_task(self) -> None:
        task: str = input("Enter a task: ")
        self.add_task(task)

    def remove_task(self) -> None:
        task: str = input("Enter the task to remove: ")
        self.delete_task(task)

```

In this case, the `ToDoList` class has multiple responsabilities: **managing tasks**, **handling user input**, and **displaying tasks**.

The `ToDoList` **class** violates the **Single Responsability Principle**, which states that a class should have only one reason to change.

A **class** having **multiple responsabilities** makes the code **harder** to **maintain**, **understand**, and **extend**, as changes in one area might impact other areas.

In this example, we can separate the `ToDoList` in three classes: `TaskManager`, `TaskPresenter`, and `TaskInput`.

```python

class TaskManager:

    def __init__(self) -> None:
        self.tasks: list[str] = []

    def add_task(self, task: str) -> None:
        self.tasks.append(task)

    def delete_task(self, task: str) -> None:
        self.tasks.remove(task)

class TaskPresenter:

    @staticmethod
    def display_tasks(tasks: list[str]) -> None:
        for task in tasks:
            print(task)

class TaskInput:

    @staticmethod
    def input_task() -> str:
        return input("Enter a task: ")

    @staticmethod
    def remove_task() -> str:
        return input("Enter the task to remove: ")

```

Now, we have three separated classes:
* `TaskManager`: handles the **storage** and **management** of **tasks**.
* `TaskPresenter`: displays **tasks**.
* `TaskInput`: handles **user input** for **adding** or **removing tasks**.

This **adheres** to the **S**ingle **R**esponsability **P**rinciple as each class now has a **single responsability**, making the code **more maintainable** and **easier** to **understand**.
