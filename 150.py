'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
'''
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        numbers = []
        operators = ["+", "-", "*", "/"]
        for i in tokens:
            if i in operators:
                x, y = int(numbers.pop()), int(numbers.pop())
                numbers.append(
                    x + y
                    if i == "+"
                    else y - x
                    if i == "-"
                    else x * y
                    if i == "*"
                    else int(y / x)
                )
            else:
                numbers.append(i)
        return numbers[0]