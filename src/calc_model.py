import re

class CalcModel:

    def __init__(self):
        self.result = ""

    def findNegatives(self, expr):
        return re.sub("^\-|(?<=[+\-\/\*\(])-(?=\(|\d)", "!", expr)

    def splitExpr(self, expr):
        return re.findall("\d+\.\d+|\d+|[+\-\/\*\()!]", expr)

    def higher_precedence(self, opA, opB):
        prec_dict = {"(": 0, ")": 0, "-": 1, "+": 1, "*": 2, "/": 2, "!": 3}
        return prec_dict[opA] >= prec_dict[opB]
        
    def isNumber(self, str):
        return re.search("\d+\.\d+|\d+", str) is not None

    def convertToRPN(self, tokens):
        rpn_expr = ""
        stack = []
        for token in tokens:
            if self.isNumber(token):
                rpn_expr += "{0} ".format(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                top = stack[-1] if stack else None
                while top is not None and top != '(':
                    rpn_expr += "{0} ".format(stack.pop())
                    top = stack[-1] if stack else None
                stack.pop()
            else:
                top = stack[-1] if stack else None
                while top is not None and self.higher_precedence(top, token):
                    rpn_expr += "{0} ".format(stack.pop())
                    top = stack[-1] if stack else None
                stack.append(token)
        top = stack[-1] if stack else None
        while top is not None:
            rpn_expr += "{0} ".format(stack.pop())
            top = stack[-1] if stack else None
        
        return rpn_expr
        
    def evaluateRPN(self, expr):
        tokens = expr.strip().split(" ")
        stack = []
        for token in tokens:
            if self.isNumber(token):
                stack.append(float(token))
            else:
                if token == "+":
                    right, left = stack.pop(), stack.pop()
                    stack.append(left + right)
                elif token == "-":
                    right, left = stack.pop(), stack.pop()
                    stack.append(left - right)
                elif token == "*":
                    right, left = stack.pop(), stack.pop()
                    stack.append(left * right)
                elif token == "/":
                    right, left = stack.pop(), stack.pop()
                    stack.append(left / right)
                else: #negative
                    stack.append(-stack.pop())
        
        return stack[0]
                    
    def evaluate(self, expression):
        cleaned_expr = self.findNegatives(expression.replace(" ", ""))
        split_expr = self.splitExpr(cleaned_expr)
        rpn_expr = self.convertToRPN(split_expr)
        self.result = str(self.evaluateRPN(rpn_expr))
        return self.result
