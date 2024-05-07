# Functional Programming Solution
# Implementing a function to flatten and sort an array of integers in ascending order.

def flatten_and_sort(arr):
    """
    Flattens the array and sorts it in ascending order.
    
    Args:
        arr (list): The input list of integers.
    
    Returns:
        list: The flattened and sorted list of integers.
    """
    flattened = [item for sublist in arr for item in sublist]
    return sorted(flattened)

# Thought Prompt Answers (commented out)
"""
How does this solution ensure data immutability?
- This solution does not modify the original input array. It creates a new list with the flattened and sorted values.

Is this solution a pure function? Why or why not?
- Yes, this function is pure because it only relies on its input arguments and produces the same output for the same input every time.

Is this solution a higher order function? Why or why not?
- No, this function is not a higher order function because it does not take another function as an argument or return a function as its output.

Would it have been easier to solve this problem using a different programming style?
- This problem could potentially be solved using imperative programming, but functional programming offers a concise and elegant solution.

Why in particular is functional programming a helpful paradigm when solving this problem?
- Functional programming encourages immutability and the use of pure functions, which helps in writing clean and maintainable code for tasks like sorting and transforming data.
"""

# Object-Oriented Programming Solution
# Implementing classes for organizing podracer inventory.

class Podracer:
    """
    A class representing a general Podracer.
    """
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
    def repair(self):
        """
        Updates the condition of the podracer to "repaired".
        """
        self.condition = "repaired"

class AnakinsPod(Podracer):
    """
    A class representing Anakin's Podracer.
    """
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def boost(self):
        """
        Multiplies max_speed by 2.
        """
        self.max_speed *= 2

class SebulbasPod(Podracer):
    """
    A class representing Sebulba's Podracer.
    """
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def flame_jet(self, other_pod):
        """
        Updates the condition of another podracer to "trashed".
        """
        other_pod.condition = "trashed"

# Thought Prompt Answers (commented out)
"""
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
- Encapsulation: Each class encapsulates its data and behavior within its own scope.
- Inheritance: The AnakinsPod and SebulbasPod classes inherit attributes and methods from the Podracer class.
- Polymorphism: The flame_jet method in the SebulbasPod class demonstrates polymorphism by accepting different types of Podracer objects.

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
- Object-oriented programming is well-suited for modeling real-world entities like Podracers. It provides a clear structure and facilitates code reuse through inheritance.

How in particular did Object Oriented Programming assist in the solving of this problem?
- OOP allowed us to create modular and reusable code by defining classes for different types of Podracers. Inheritance helped in sharing common attributes and methods among related classes.
"""

# Reflections (commented out)
"""
Is one of these coding paradigms "better" than the other? Why or why not?
- The superiority of one paradigm over the other depends on the specific requirements of the problem and the preferences of the developer. Functional programming excels in tasks involving data transformation and processing, while OOP is well-suited for modeling complex systems and interactions between objects.

Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why?
- It depends on personal preference and the nature of the project. Some developers may find functional programming more appealing for its simplicity and emphasis on immutability, while others may prefer OOP for its structured approach to modeling real-world entities.

Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming?
- Functional programming is suitable for tasks like data processing, sorting, and filtering, where immutability and pure functions are beneficial. On the other hand, OOP is ideal for modeling complex systems with interconnected objects, encapsulating behavior and data within classes, and facilitating code reuse through inheritance.

Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?
- The difficulty of understanding each paradigm varies from person to person. Some may find functional programming more challenging due to its focus on higher-order functions and recursion, while others may struggle with the concepts of inheritance and polymorphism in OOP. To deepen understanding, it's essential to practice writing code in both paradigms, study real-world examples, and seek guidance from experienced developers or resources like documentation and tutorials.
"""
