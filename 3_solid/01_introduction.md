# SOLID Principles

## Introduction

In this chapter, we make a review of Design Patterns. We discuss the Hallmarks of Good Architecture.

What are the hallmarks of a good architecture?

- **Loose Coupling**: weak knowledge association between components.
- **Separation of Concerns**: breaking your architecture into tiers.
- **Law of Demeter (LoD)**.
- **SOLID** **Principles** of **object-oriented programming**.

### Loose Coupling

**Short Definition**: weak knowledge association between components.

Changes to one component **least** affect existence or performance of another component.

### Separation of Concerns

**Short Definition**: breaking your architecture into tiers.

The separation of concerns is achieved using **modularization**, **encapsulation**, and **arrangement** in software layers.

### Law of Demeter (LoD)

**Definition** of **Law of Demeter (Lod)**:
- Each **unit** should have **only limited knowledge** about other units: it should only know about units 'closely' related to itself.
- Each **unit** should only talk to its friends; do not talk to strangers.
- Only talk to your immediate friends.

A given object should assume as little as possible about the structure or properties of anything else. It is also known as **Principle of Least Knowledge**.

### SOLID Principles

**SOLID** is an acronym for a group of five principles in object-oriented programming.

**SOLID** stands for:
- **S**ingle-responsability principle.
- **O**pen-close principle.
- **L**iskov substitution principle.
- **I**nterface segregation principle.
- **D**epedency inversion principle.
