from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
# Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

def reverseString(string):
    stack = Stack()
    
    for ch in string:
        stack.push(ch)
    
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
        
    return reversed_str

value = reverseString("We will conquere COVID-19")
print(value)

# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

def is_balanced(s):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['} 

    for ch in s:
        if ch in "({[":   
            stack.push(ch)
        elif ch in ")}]":  
            if stack.is_empty():
                return False
            if stack.pop() != pairs[ch]:
                return False
    
    return stack.is_empty()

print(is_balanced("({a+b})"))       
print(is_balanced("))((a+b}{"))      
print(is_balanced("((a+b))"))       
print(is_balanced("))"))             
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))