from tokens import Integer, Float, Operation, Declarations, Variable
class Lexer:
    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    operations = "+-/*()="
    stopwords = [" "]
    declarations = ["open"]
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
            elif self.char in Lexer.stopwords:
                self.move()
                continue
            elif self.char in Lexer.letters:
                word = self.extract_word()
                if word in Lexer.declarations:
                    self.token = Declarations(word)
                else:
                    self.token = Variable (word)
            self.tokens.append(self.token)
        return self.tokens
    def extract_number(self):
        number = ""
        isFloat = False
        while(self.char in Lexer.digits or self.char ==".") and (self.idx < len(self.text)):
            if self.char ==".":
                isFloat=True
            number+=self.char
            self.move()
        return Integer(number) if not isFloat else Float(number)
    def extract_word(self):
        word = ""
        while self.char in Lexer.letters and self.idx < len(self.text):
            word+=self.char
            self.move()
        return word
    def move(self):
        self.idx+=1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]

class Token:
    def __init__(self,type,value):
        self.type = type
        self.value = value
    def __repr__(self):
        return self.value
