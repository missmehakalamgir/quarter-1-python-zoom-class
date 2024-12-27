# Zoom Class 1: Python Class Covering Basic Topics

# Topic 1: Basic Syntax
print("Hello World")  # Ye ek simple Python statement hai jo "Hello World" print karega.

# Topic 2: Comments
print("mehak alamgir")  # Ye ek output statement hai.
# Ye ek comment hai. Comments ko program execute nahi karta.
'''
Ye ek multiple-line comment ka example hai.
Is tarah ke comments ka use documentation ke liye hota hai.
'''

# Topic 3: Variables
# Variables ka use data store karne ke liye hota hai.
# numbers => integers
# string => text data

# Example:
x = 5  # Integer type variable
y = "mehak alamgir"  # String type variable

print(x)  # Ye integer variable ko print karega.
print(y)  # Ye string variable ko print karega.

# Topic 4: Local Variable and Global Variable

# Local variable sirf function ke andar kaam karta hai.
# Global variable program ke har jagah accessible hota hai.

x = "python is a programming language"  # Global variable
print(x)

# Multiple variables
x = "python"
y = "is"
z = "awesome"
print(x, y, z)  # Ye ek line me multiple variables ko print karega.

# Variable sun (sum) integer
x = 5
y = "Mehak"
# print(x + y)  # Ye error dega kyun ke integer aur string ko direct concatenate nahi kar sakte.

# Global variables
awesome = "x"

def abc():
    # Global variable ka use function ke andar ho sakta hai.
    print("is " + awesome)  
    print("python is " + awesome)
    print("hooria is " + awesome)

abc()

# Topic 5: Data Types
# Python ke data types:
# integer (numbers), string (text), boolean (True/False)

x = "5"  # String type
print(type(x))  # Ye variable ke data type ko print karega.

# Topic 6: List
# List ek ordered collection hai jo multiple items ko store kar sakti hai.
x = list(("asad", "hooria", "noman"))  # List banane ka example
print(x)  # Ye list ko print karega.

# Topic 7: F-String
# F-String ka use string me variables embed karne ke liye hota hai.

x = "awesome"
print(f"python is {x}. Always take my zoom class cause I teach {x} python")  # F-string ka example

# Ek aur example
name: str = "Alice"  # String variable with type hint
age: int = 27  # Integer variable with type hint
print(f"My name is {name}, and I am {age} years old. {name} is a hardworking girl.")  # Roman Urdu comments ke saath f-string
