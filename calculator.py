tokens = ('NUMBER','PLUS', 'MINUS', 'MUL', 'DIV', 'LPAR', 'RPAR' , 'POWER' , 'UMINUS' , 'ASG' , 'VAR')
t_PLUS     = r'\+'
t_MINUS    = r'\-'
t_MUL    = r'\*'
t_DIV    = r'/'
t_LPAR    = r'\('
t_RPAR    = r'\)'
t_POWER    = r'\^'
t_ASG     = r'\='
t_VAR     = r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_NUMBER(t):
 r'[0-9]+'
 t.value = int(t.value)
 return t
def t_UMINUS(t):
 r'[-][0-9]+'
 t.value = int(t.value)
 return t
t_ignore = " \t"
def t_error(t):
 print("Illegal character '%s'" % t.value[0])
 t.lexer.skip(1)
import ply.lex as lex;lex.lex()
vars={}
def p_S(p):
 'S : E' # S → E
 print('S → E ', p[1])
def p_E_plus_T(p):
 'E : E PLUS T' # E → E + T
 p[0] = p[1] + p[3]
 print('E → E + T :', 'E: ',p[0], ' \t E1: ', p[1], '\t T: ', p[3])
def p_E_MINUS_T(p):
 'E : E MINUS T' # E → E - T
 p[0] = p[1] - p[3]
 print('E → E - T :', 'E: ',p[0], ' \t E1: ', p[1], '\t T: ', p[3])
def p_E_T(p):
 'E : T' # E → T
 p[0]=p[1]
 print('E → T :', p[1])
def p_T_MUL_F(p):
 'T : T MUL F' # T → T * F
 p[0] = p[1] * p[3]
 print('T → T * F :', 'T: ',p[0], ' \t T1: ', p[1], '\t F: ', p[3])
def p_T_DIV_F(p):
 'T : T DIV F' # T → T / F
 if p[3] != 0:  p[0] = p[1] / p[3]
 else: print('Error: Divide by zero '); p[0]=p[1]
 print('T → T / F :', 'T: ',p[0], ' \t T1: ', p[1], '\t F: ', p[3])
def p_T_F(p):
 'T : F' # T → F
 p[0]=p[1]
 print('T → F :', p[1])
def p_F_a(p):
 'F : Z POWER F' # F → Z ^ F
 p[0]=p[1] ** p[3]
 print('F → Z ^ F :', 'F: ',p[0], ' \t Z: ', p[1], '\t F1: ', p[3])
def p_F_Z(p):
 'F : Z' # F → Z
 p[0]=p[1]
 print('F → Z :', p[1])
def p_Z_a(p):
 'Z : NUMBER' # Z → a
 p[0]=p[1]
 print('Z → a :', p[1])
def p_Z_MINUS_a(p):
 'Z : UMINUS ' # Z → -a
 p[0]=-p[1]
 print('Z → -a :', p[0])
def p_Z_lpar_E_rpar(p):
 'Z : LPAR E RPAR' # Z → ( E )
 p[0]=p[2]
 print('Z → (E) :', p[0])
def p_Z_v(p):
 'Z : VAR ' # Z → v
 p[0]=p[1]
 p[0] = vars[p[1]]
 print('Z → v :', p[0])
def p_S_v_ASG_E(p):
  'S : VAR ASG E' # S → v = E
  p[0]=p[3]
  print("Assigning variable", p[1], "to", p[3])
  vars[p[1]] = p[3]

def p_error(p):
 print("Syntax error at '%s'" % p)
import ply.yacc as yacc
parser=yacc.yacc()
while True:
  try:
    s = input('calc > ')
    if s.strip()=='':break
    result=parser.parse(s)
    print("result=",result)
  except: print('unexpected error')