# Interface Separation Principle

## Introduction

In this chapter, we presents a overview and a practice of **I**nterface **S**eparation **P**rinciple (**ISP**).

## Definition

*"Clients should not be forced to depend upon interfaces that they do not use."*

Declaring methods in an interface that the caller does not need pollutes the interface and leads to a "bulky" or "fat" interface.

## Practical Example

Considering the above example:

```python
from abc import ABC, abstractmethod

class MultiFunctionDevice:

    @abstractmethod
    def copy(self) -> None:
        ...

    @abstractmethod
    def fax(self) -> None:
        ...

    @abstractmethod
    def print(self) -> None:
        ...

    @abstractmethod
    def scan(self) -> None:
        ...

class Copier(MultiFunctionDevice):

    def copy(self) -> None:
        print("Copying ...")

class Fax(MultiFunctionDevice):

    def fax(self) -> None:
        print("Faxing ...")

class Printer(MultiFunctionDevice):

    def print(self) -> None:
        print("Printing ...")

class Scanner(MultiFunctionDevice):

    def scan(self) -> None:
        print("Scanning ...")

```

In this case, the initial code has a single `MultiFunctionDevice` **interface** with the methods for copying (`copy()`), faxing (`fax()`), printing (`print()`), and scanning (`scan()`).

Each class (`Copier`, `Fax`, `Printer`, and `Scanner`) implementing this **interface** must provide implementations for all methods, even those that are not relevante to its funcionality.

This violates the **I**nterface **S**eparation **P**rinciple (**ISP**), which states that **clients** should not be **forced** to depend on interfaces they do not use.

Having a **large interface** with unrelated methods makes the code **harder** to **maintain**, **understand**, and **extend**.

In this example, we can define different **interfaces** for each **abstract method**. We can have the following **interfaces**: `ICopier`, `IFax`, `IPrinter`, and `IScanner`. Each **interface** contains your own respective **abstract method**.

```python
from abc import ABC, abstractmethod

class ICopier(ABC):

    @abstractmethod
    def copy(self) -> None:
        ...

class IFax(ABC):

    @abstractmethod
    def fax(self) -> None:
        ...

class IPrinter(ABC):

    @abstractmethod
    def print(self) -> None:
        ...

class IScanner(ABC):

    @abstractmethod
    def scan(self) -> None:
        ...

class Copier(Copy):

    def copy(self) -> None:
        print("Copying ...")

class Fax(Copy):

    def fax(self) -> None:
        print("Faxing ...")

class Printer(Copy):

    def print(self) -> None:
        print("Printing ...")

class Scanner(Copy):

    def scan(self) -> None:
        print("Scanning ...")
```

In the refactored solution, we breaks the single `MultiFunctionDevice` **interface** into four **smaller** and more **specific** interfaces: `ICopier`, `IFax`, `IPrinter`, and `IScanner`.

Each class (`Copier`, `Fax`, `Printer`, and `Scanner`) now only needs to implement the methods relevant to its functionality.

This **adheres** to the **I**nterface **S**egregation **P**rinciple (**ISP**) because the interfaces are now **more focused**, making the code **more maintainable** and **easier** to **understand**.
