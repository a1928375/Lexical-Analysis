import ply.lex as lex

tokens = ('PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
          'IDENT', 'STRING', 'NUMBER') 

def t_PLUS(token):
    
    r"\+"
    
    return token
    

def t_MINUS(token):
    
    r"\-"
    
    return token

def t_TIMES(token):
    
    r"\*"
    
    return token

def t_DIVIDE(token):
    
    r"\/"
    
    return token

#       IDENT           my_variable  Caps_Are_OK    
def t_IDENT(token):
    
    r"[a-zA-Z][a-zA-Z_]*"
    
    return token

#       STRING          'yes'  "also this"  
def t_STRING_sin(token):
    
    r"'[^']*'"
    token.value = token.value[1:-1]
    token.type = "STRING"
    
    return token
    
#       STRING          'yes'  "also this"  
def t_STRING_dou(token):
    
    r'"[^"]*"'
    token.value = token.value[1:-1]
    token.type = "STRING"
    
    return token
    
#       NUMBER          123  123_456_789
def t_NUMBER(token):
    
    r"[0-9][0-9_]*"
    
    tem = ""
    
    for i in range(len(token.value)):
        
        if token.value[i] != "_":
            
            tem = tem + token.value[i]
        
    token.value = int(tem)
    
    return token


t_ignore = ' \t\v\r'

def t_error(t):
  print "Lexer: unexpected character " + t.value[0]
  t.lexer.skip(1) 

# We have included some testing code to help you check your work. Since this is the final exam, you will definitely want to add your own tests.
lexer = lex.lex() 

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [(tok.type,tok.value)]
  return result

question1 = " +   -   /   * " 
answer1 = [('PLUS', '+'), ('MINUS', '-'), ('DIVIDE', '/'), ('TIMES', '*')]

print (test_lexer(question1) == answer1)

question2 = """ 'string "nested" \' "inverse 'nested'" """
answer2 = [('STRING', 'string "nested" '), ('STRING', "inverse 'nested'")]
print (test_lexer(question2) == answer2)

question3 = """ 12_34 5_6_7_8 0______1 1234 """
answer3 = [('NUMBER', 1234), ('NUMBER', 5678), ('NUMBER', 1), ('NUMBER', 1234)]
print (test_lexer(question3) == answer3)

question4 = """ 'he'llo w0rld 33k """
answer4 = [('STRING', 'he'), ('IDENT', 'llo'), ('IDENT', 'w'), ('NUMBER',
0), ('IDENT', 'rld'), ('NUMBER', 33), ('IDENT', 'k')]
print (test_lexer(question4) == answer4)
