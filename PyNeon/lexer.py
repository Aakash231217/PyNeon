class Lexer:
    digits = "0123456789"
    operations = "+-/*"
    def __init__(self, text):
        self.text = text
        self.idx = 0
        self.tokens = []
        self.char = self.text[self.idx]
        self.token = None
        
    def tokenize(self):
        while self.idx < len(self.text):
            if self.char in Lexer.digits:
                self.token = self.extract_number()
            elif self.char in Lexer.operations:
                self.token = Operation(self.char)
                self.move()
            self.tokens.append(self.token)
        return self.tokens
    def extract_number(self):
        number = ""
        isFloat = False
        while(self.char in Lexer.digits) and (self.idx < len(self.text)):
            number+=self.char
            self.move()
        return Integer(number) if not isFloat else Float(number)
    def move(self):
        self.idx+=1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]

class Token:
    def __init__(self,type,value):
        self.type = type
        self.value = value
class Integer(Token):
    def __init__(self,value):
        super().__init__("INT",value)

class Float(Token):
    def __init___(self,value):
        super().__init__("FLT",value)
        
class Operation(Token):
    def __init__(self,value):
        super().__init__("OP",value)