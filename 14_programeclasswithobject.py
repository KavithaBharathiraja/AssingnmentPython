#14.Create a class named 'Programming'. While creating an object of the class, if nothing is passed to it, then the message "I love programming languages" should be printed. If some String is passed to it, then in place of "programming languages" the name of that String variable should be printed.

class Programming:
# Constructor with a default parameter
     def __init__(self, language="programming languages"):
            print(f"I love {language}")

# Creating an object without passing any arguments
obj1 = Programming()

# Creating an object and passing a string argument
obj2 = Programming("python")


