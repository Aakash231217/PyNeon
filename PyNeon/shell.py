from lexer import Lexer
while True:
    text = input("PyNeon: ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    
    print(tokens)
    