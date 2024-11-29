# Dependency Inversion Principle

## Introduction

In this chapter, we presents a overview and a practice of **D**ependency **I**nversion **P**rinciple (**DIP**).

## Definition

*"Depend upon abstractions, not concretions."*

As example, imagine an **id generator** for a entity class. In this case, we can just have a interface `IdGenerator` with a method named `next_id()`. Therefore, we do not need know what class implements this method, but we know that the instance must be a class that implements the `next_id()`.

## Practical Example

Considering the above example:

```python

class EmailService:

    def send_email(self, message: str, receiver: str) -> None:
        print(f"Sending Email: {message} to {receiver}")

class SMSService:

    def send_sms(self, message: str, receiver: str) -> None:
        print(f"Sending SMS: {message} to {receiver}")

class NotificationService:

    def __init__(self):
        self.email_service: EmailService = EmailService()
        self.sms_service: SMSService = SMSService()

    def send_notification(self, message: str, receiver: str, method: str) -> None:
        if method == "email":
            self.email_service.send_email(message, receiver)
        elif method == "sms":
            self.sms_service.send_sms(message, receiver)

```

In this case, the initial code has the `NotificationService` **class** that directly depends on the **concrete classes** `EmailService` and `SMSService`.


This violates the **D**ependency **I**nversion **P**rinciple (**DIP**), which states that high-level modules **should not depend** on low-level modules. Both **should depend** on **abstractions**.

The **direct dependecy** on **concrete classes** makes the `NotificationService` **less flexible** and **harder** to **change** or **extend**, as it's **tightly coupled** to specific implementations of the Email and SMS services.

In this example, we can define different an **Interface** for message service named `IMessageService`, with an **abstract method** named `send` with the following parameters: `message` and `receiver`. Now, we can define the `EmailService` and `SMSService` classes implementing the `IMessageService` **interface**.

```python
from abc import ABC, abstractmethod

class IMessageService(ABC):

    @abstractmethod
    def send(self, message: str, receiver: str) -> None:
        ...

class EmailService(IMessageService):

    def send(self, message: str, receiver: str) -> None:
        print(f"Sending Email: {message} to {receiver}")

class SMSService(IMessageService):

    def send(self, message: str, receiver: str) -> None:
        print(f"Sending SMS: {message} to {receiver}")

class NotificationService:

    def __init__(self, service: IMessageService):
        self.service: IMessageService = service

    def send_notification(self, message: str, receiver: str) -> None:
        self.service.send(message, receiver)

```

In the refactored solution, we introduced an **abstract class** `IMessageService`** with an **abstract method** `send()`. Both `EmailService` and `SMSService` now implement the `IMesssageService` **interface**.

The `NotificationService` **class** now **depends on** the **abstraction** `IMessageService` rather than the **concrete classes** `EmailService` and `SMSService`.

This **adheres** to the **D**ependency **I**njection **P**rinciple (**DIP**) because both high-level and low-level classes depend on **abstractions** rather than **concrete implementations**, making the code **more flexible** and **easier** to **change** or **extend**.
