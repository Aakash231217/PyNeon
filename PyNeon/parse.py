class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.idx = 0
        self.token = self.tokens[self.idx]
    def factor(self):
        if self.token.type =="INT" or self.token.type =="FLT":
            return self.token
        elif self.token.value =='(':
            self.move()
            expression = self.expression()
            return expression
        elif self.token.type.startswith("VAR"):
            return self.token
    def term(self):
        left_node = self.factor()
        self.move()
        output = left_node
        while self.token.value == "*" or self.token.value == "/":
            operation = self.token
            self.move()
            right_node = self.factor()
            self.move()
            left_node = [left_node, operation, right_node]
        return left_node
    def expression(self):
        left_node = self.term()
        output = left_node
        while self.token.value =="+" or self.token.value == "-":
            operation = self.token
            self.move()
            right_node = self.term()
            left_node = [left_node, operation, right_node]
        return left_node
    def variable(self):
        if self.token.type.startswith("VAR"):
            return self.token
    def statement(self):
        if self.token.type =="DECL":
            #VAriable Assignment
            self.move()
            left_node = self.variable()
            self.move()
            if self.token.value == "=":
                operation = self.token
                self.move()
                right_node = self.expression()
                return [left_node, operation, right_node]
        elif self.token.type == "INT" or self.token.type == "FLT" or self.token.type == "OP":
            #Arithmtic expression
            return self.expression()
            
    def parse(self):
        return self.statement()
    def move(self):
        self.idx+=1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]
            