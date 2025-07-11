--- Employee Details ---
Name: Alice
ID: 101
Salary: $75000
Role: Developer
Programming Language: Python
Alice is writing code in Python.

--- Employee Details ---
Name: Bob
ID: 102
Salary: $85000
Role: Team Leader
Team Size: 5
Bob is managing a team of 5 developers.

--- Employee Details ---
Name: Charlie
ID: 103
Salary: $100000
Role: Manager
Department: Technology
Charlie is planning and reviewing projects in Technology department.




########### ABSTRACTION ###############

Abstraction in Python, a core principle of Object-Oriented Programming (OOP), focuses on simplifying complex systems by hiding unnecessary implementation details and exposing only the essential features or functionalities to the user. This allows users to interact with objects at a higher level, without needing to understand the intricate internal workings. 
Key aspects of abstraction in Python:
Hiding Complexity:
Abstraction aims to reduce complexity by presenting a simplified view of an object or system. Users interact with a clear interface, without needing to know the underlying code or mechanisms.
Abstract Base Classes (ABCs):
Python achieves abstraction primarily through the abc module, which allows the creation of Abstract Base Classes. ABCs are classes that cannot be instantiated directly and are designed to be inherited by other classes.
Abstract Methods:
Within an ABC, you can define abstract methods using the @abstractmethod decorator. These methods are declared but have no implementation in the abstract class itself. Subclasses inheriting from the ABC are then required to provide concrete implementations for these abstract methods. This enforces a consistent interface across related classes.
Enforcing Structure:
By defining abstract methods in an ABC, you ensure that any concrete subclass adheres to a specific structure and implements certain functionalities, promoting code consistency and maintainability.