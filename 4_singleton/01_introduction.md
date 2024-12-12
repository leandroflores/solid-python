# Singleton

## Introduction

**Singleton** is a **creational design pattern** that ensures that a class has only one instance and provides an **easy** global access to that instance.

The pattern does not stipulate what to do with a **Singleton**.

The main tenets of this pattern are?
- **Ensure** that the **class** has only a **single instance**.
- Provide **easy global access** to this **instance**.
- Control how it is **instantiated**.
- Any **critical region** must be entered **serially**.

All clients have **global access** to a **single instance**.

## Practical Examples

Practical examples of using **Singleton** is loggers, caching, thread pools, database connections, and configuration access.

**Singleton** is one of the famous **G**ang **o**f **F**our (**GoF**) patterns and its motivation is stated as follows:

"It's important for some classes to have exactly one instance."

**Singleton** is often used with the following **GoF** patterns: **Abstract Factory**, **Builder**, **Prototype**, **Facade**, and **State**.

## Use Cases

**Singleton** is recommended when you want to **control access** to a **shared resource**.

Use the **Singleton** pattern with **restraint** and do not let it **degenerate** into **just** a **global access** for **everything**.

**Global access** hides **dependencies** and might make it harder to read such code, so make sure that you have a good reason to use this pattern.

The main question is: "Do you violate the **S**ingle **R**esponsability **P**rinciple (**SRP**)?". If **YES**, then reconsider using it.

## Design

When designing a **Singleton**, consider **lazy construction** which means that the **class instance** should **only** be **created** when it is first needed.

In some cases, we might consider **eager loading** if, for example, we need the **singleton** to be always ready and loaded fast.

**Thready-Safety** needs to be considered in languages that **allow** multi-threaded access to ensure that access is properly controlled and locked, so that the state of the singleton (if it has one) is always **deterministic**.

Python support multi-threaded programming we will need take **special care** when creating **multi-threaded singletons**. We will need to **lock** the **critical section**.
