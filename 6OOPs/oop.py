# class Maths:
    
#     def add(self,a,b):
#         return a +b
    
#     def sub(self,a,b):
#         return a -b
    
#     def testSub(self):
#         return self.sub(20,10)
    
# m = Maths()
# print(m.add(12,14))
# print(m.sub(16,11))
# print(m.testSub())


# class Student:
#     def __init__(self,s):
#         self.name = s
    
#     def hello(self):
#         print("Hello ")
#         print(self.name)
        
# t = Student("Saurav")
# t.hello()

'''
### 🧠 **Understanding the Code:**

```python
class Student:
    def __init__(self, s):
        self.name = s  # 'name' is set as an instance variable
    
    def hello(self):
        print("Hello ")
        print(self.name)  # Accessing the 'name' attribute from the instance

t = Student("Saurav")  # Creating an instance of Student with "Saurav"
t.hello()              # Calling the 'hello' method
```

### ✅ **What’s Happening:**
1. **Class Definition (`Student`)**:
   - You define a class named `Student`.

2. **Initializer (`__init__`)**:
   - The `__init__` method is called automatically when you create a new object.
   - It sets an instance attribute `name` to the value of `s`.

3. **Method (`hello`)**:
   - The `hello` method prints "Hello" and then prints the value of `self.name`.

4. **Creating an Object**:
   - `t = Student("Saurav")` creates an instance of `Student` and passes `"Saurav"` to the `__init__` method.
   - This sets `t.name` to `"Saurav"`.

5. **Calling the Method**:
   - `t.hello()` calls the `hello` method, which prints:
     ```
     Hello 
     Saurav
     ```

### 🚩 **Why No Error?**
- `self.name` is created in the `__init__` method, so by the time you call `hello`, the object already has the `name` attribute.
- If you tried to access `self.name` without initializing it, you'd get an error — but since it’s set in the constructor, everything works smoothly.

For example, if you forgot to set `self.name`:
```python
class Student:
    def hello(self):
        print(self.name)  # ERROR: name isn't defined!

t = Student()
t.hello()
```

This would raise:
```
AttributeError: 'Student' object has no attribute 'name'
```

'''



## Write a class to calculate area ractangle.
# class Ractangle():
#     def __init__(self,l,w):
#         self.length = l
#         self.width = w
        
#     def ractangel_area(self):
#         return self.length * self.width 
# r = Ractangle(10,20)
# print(r.ractangel_area())


## Write a class to calculate area and primeter of circle
# class Circle():
#     def __init__(self,r):
#         self.radius = r
#     def area(self):
#         return 3.14*self.radius**2
#     def perimeter(self):
#         return 2*3.14*self.radius

# NewCircle = Circle(3)
# print("Area of circle: ",NewCircle.area())
# print("Perimeter of circle: ",NewCircle.perimeter())

## Method overriding
# class counter:
#     def __init__(self):
#         self.value = 0
#     def increment(self):
#         self.value += 1
        
# class customCounter(counter):
#     def __init__(self,size):
#         counter.__init__(self)
#         self.stepSize = size
#     def increment(self):
#         self.value += self.stepSize
#         return self.value
    
# cc = customCounter(4)
# print(cc.increment())
        
## inheritance
# class Vehicle:
#     def __init__(self,name,max_speed,mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# School_Bus = Bus("Volvo",120,15)
# print(f"Vechicle name is {School_Bus.name}")
# print(f"Vechicle maximum speed is {School_Bus.max_speed}")
# print(f"Vechicle mileage is {School_Bus.mileage}")
    