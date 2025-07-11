from abc import ABC, abstractmethod # for abstraction

# 1. CLASS and OBJECT + ENCAPSULATION + ABSTRACTION
class Employee(ABC):
def __init__(self, name, emp_id, salary):
self.__name = name # private attribute
self.__emp_id = emp_id # private attribute
self.__salary = salary # private attribute

# Public getter and setter (Encapsulation)
def get_name(self):
return self.__name

def set_name(self, name):
self.__name = name

def get_emp_id(self):
return self.__emp_id

def get_salary(self):
return self.__salary

def set_salary(self, salary):
if salary > 0:
self.__salary = salary
else:
print("Invalid salary")

# Abstract Method (Abstraction)
@abstractmethod
def work(self):
pass

# Common method (can be overridden)
def display_details(self):
print(f"Name: {self.__name}")
print(f"ID: {self.__emp_id}")
print(f"Salary: ${self.__salary}")


# 2. INHERITANCE + POLYMORPHISM
class Developer(Employee):
def __init__(self, name, emp_id, salary, programming_language):
super().__init__(name, emp_id, salary)
self.programming_language = programming_language

def work(self): # Polymorphism
print(f"{self.get_name()} is writing code in {self.programming_language}.")

def display_details(self): # Method Overriding (Polymorphism)
super().display_details()
print(f"Role: Developer")
print(f"Programming Language: {self.programming_language}")


class TeamLeader(Employee):
def __init__(self, name, emp_id, salary, team_size):
super().__init__(name, emp_id, salary)
self.team_size = team_size

def work(self): # Polymorphism
print(f"{self.get_name()} is managing a team of {self.team_size} developers.")

def display_details(self): # Method Overriding
super().display_details()
print(f"Role: Team Leader")
print(f"Team Size: {self.team_size}")


class Manager(Employee):
def __init__(self, name, emp_id, salary, department):
super().__init__(name, emp_id, salary)
self.department = department

def work(self): # Polymorphism
print(f"{self.get_name()} is planning and reviewing projects in {self.department} department.")

def display_details(self): # Method Overriding
super().display_details()
print(f"Role: Manager")
print(f"Department: {self.department}")


# -------------------------------
# 3. CREATING OBJECTS (Class & Object concept)
# -------------------------------

dev = Developer("Alice", 101, 75000, "Python")
lead = TeamLeader("Bob", 102, 85000, 5)
mgr = Manager("Charlie", 103, 100000, "Technology")

# -------------------------------
# 4. POLYMORPHISM IN ACTION
# -------------------------------

employees = [dev, lead, mgr]

for emp in employees:
print("\n--- Employee Details ---")
emp.display_details()
emp.work()