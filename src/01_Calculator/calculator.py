from operator import add, mul, sub, truediv
from typing import List, Optional, Union

#from typing import List

ops = {"+": add, "-": sub, "*": mul, "/": truediv}


def prefix_evaluate(prefix_evaluation: str) -> int:
    if prefix_evaluation == "":
        return None
    value_stack = []
    prefix_equation = prefix_evaluation.split()
    while prefix_equation:
        el = prefix_equation.pop()
        if el not in ops:
            value_stack.append(int(el))
        else:
            r_val = value_stack.pop()
            l_val = value_stack.pop()
            operation = ops[el]
            value_stack.append(operation(r_val, l_val))

    return value_stack[0]


def to_prefix(equation: str) -> str: 
    oops = set('+-*/') 
    priority = {'+': 1, '-': 1, '*': 2, '/': 2} 
    token_stack = [] 
    prefix_tokens = [] 
 
    for i in reversed(equation.split()): 
        if i not in oops: 
            if i != '(' and i != ')': 
                token_stack.append(i) 
            if i == '(': 
                while prefix_tokens and prefix_tokens[-1]!=')':  
                    token_stack.append(prefix_tokens.pop()) 
                prefix_tokens.pop() 
            if i == ')':  
               prefix_tokens.append(i)    
        if i in oops: 
            while prefix_tokens and prefix_tokens[-1]!=')' and priority[i] <= priority.get(prefix_tokens[-1], 0):  
                token_stack.append(prefix_tokens.pop()) 
            prefix_tokens.append(i) 
    while prefix_tokens: 
        token_stack.append(prefix_tokens.pop()) 
 
    return " ".join(list(reversed(token_stack))) 
         


def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
