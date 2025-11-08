# Practice 9: OOPS Part 2

## 📌 Overview  
This notebook continues from Part 1 and explores more advanced Object-Oriented Programming concepts in Python — like **inheritance**, **method overriding**, and **superclass interaction**.  
You’ll learn how classes can build on each other to make your code modular and maintainable.

## 🧾 What’s Inside  
- **Inheritance Basics** — how one class can inherit attributes and methods from another.  
- **Parent (Base) and Child (Derived) Classes** — reusing and extending functionality.  
- **Method Overriding** — redefining inherited methods for specialized behavior.  
- **`super()` Function** — calling parent class constructors or methods inside a child class.  
- **Practical Exercises** — showing how inheritance reduces repetition and keeps logic clean.  

### Example Topics You Might See  
- Creating a base class `Person` and a subclass `Student` or `Employee`.  
- Using `super().__init__()` to initialize inherited attributes.  
- Demonstrating polymorphism (different classes with same method names behaving differently).  
- Adding methods unique to subclasses while still reusing parent functionality.

## 🎯 Learning Goals  
By the end of this notebook, you should be able to:
- Understand and apply **inheritance** in Python classes.  
- Use `super()` effectively to reuse parent logic.  
- Differentiate between **method overloading** and **overriding**.  
- Design class hierarchies that mirror real-world relationships (like `Vehicle → Car → ElectricCar`).  
- Appreciate how inheritance improves code organization and reduces duplication.

## 🧑‍💻 How to Use  
1. Open the notebook and run each cell to see inheritance and method interactions in action.  
2. Try modifying examples:
   - Add your own subclass and override a method.  
   - Experiment with `super()` to see how constructors get called.  
   - Create multiple levels of inheritance (e.g., `Animal → Mammal → Dog`).  
3. Write a small project — for example:
   - A `Shape` base class with `Circle`, `Rectangle`, and `Triangle` subclasses implementing an `area()` method.  

## 🔍 Why This Matters  
Inheritance is one of the **core principles** of OOP.  
It helps you:
- Avoid rewriting the same code in multiple places.  
- Build relationships between objects that naturally extend each other.  
- Keep large applications organized and scalable.

## 📚 What Comes Next  
Once you’ve mastered inheritance:
- Explore **Encapsulation** (private/protected attributes).  
- Learn about **Polymorphism** and **Abstract Classes** using the `abc` module.  
- Build a small OOP-based project that connects multiple classes together.

---

*Understanding inheritance and method overriding is a key step from writing scripts to designing full software systems.*  
