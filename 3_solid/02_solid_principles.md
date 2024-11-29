# SOLID Principles

## Introduction

In this chapter, we presents a overview of **SOLID** Principles of object-oriented programming.

## SOLID Principles

**SOLID** is an acronym for a group of five principles in object-oriented programming.

**SOLID** stands for:
- **S**ingle-responsability principle: "There should never be more than one reason for a class to change." Therefore, each class should have only one central responsibility.
- **O**pen-close principle: "Software entities should be open for extension, but closed for modification."
- **L**iskov substitution principle: "Functions that use pointers, or references to base classes, must be able to use objects of derived classes without knowing it".
- **I**nterface segregation principle: "Clients should not be forced to depend upon interfaces that they do not use".
- **D**epedency inversion principle: "Depend upon abstractions, not concretions".

### Single-Responsability Principle

*"There should never be more than a reason for a class to change"*

In other words, a **class** can be responsibilized for example: persistence, conditions, notification, logging, formatting, parsing, error handling. However, a **class** must be deal with just only one task.

### Open-Closed Principle

*"Software entities should be open for extension, but close for modification"*

In a **base class**, as **entity**, we do not modify directly this class (because possible dependencies). However, we can extend **new classes** having the **entity** as **superclass**.

### Liskov Substitution Principle

*"Functions that use pointes, or references to base classes, must be able to use objects of derived classes without knowing it.*

If `ClassA` is a **subclass** of `ClassB`, then we should be able to replace `ClassB` with `ClassA` without interrupting the behavior of the program.

### Interface Segregation Principle

*"Clients should not be forced to depend upon interfaces that they do not use."*

Declaring methods in an interface that the caller does not need pollutes the interface and leads to a "bulky" or "fat" interface.

Example is a **Logging**. A unique method is defined in **Logging Interface**. Specializations must be declared in **interfaces** that extends the **interface base**.

### Dependency Inversion Principle

*"Depend upon abstractions, not concretions."*

As example, imagine an **id generator** for a entity class. In this case, we can just have a interface `IdGenerator` with a method named `next_id()`. Therefore, we do not need know what class implements this method, but we know that the instance must be a class that implements the `next_id()`.

## Summary

To summarize, we will do the following four things in this course:
* Learn about the most fundamental design patterns in the industry.
* Study them in a proper architectural context.
* How they cover the **SOLID** and **good architecture** principles.
* Use them practically in a project.
