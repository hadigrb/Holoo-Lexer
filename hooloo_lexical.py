input_file = open('.\input.txt','r')
data = input_file.read()
input_file.close()

output_file = open('.\output.txt','w')


class DFA:
    def __init__(self,states,alphabet,delta,start,final,name,keys_list):
        self.states = states
        self.alphabet = alphabet
        self.delta = delta
        self.start = start
        self.final = final
        self.name = name
        self.currentState = start 
        self.keys_list = keys_list

    def get_transition(self,state,symbol):
        if (state,symbol) in self.delta:
            return self.delta[(state,symbol)]
        else: 
            return set()

        
    def execute(self,currentState, char):
        
            currentState = self.get_transition(currentState, char)

            if currentState == self.final:
                return True,  currentState
            else:
                return False, currentState
    
   
            
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o","p", "q", "r", "s",
 "t", "u", "v", "w", "x", "y", "z", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T",
"U","V","W","X","Y","Z"]

digits = ['1', '2', '3', '4',
 '5', '6', '7', '8', '9', '0']


signs = ['+','-']


name_id = 'id'
id_delta = {}

#fill id_delta
for l in letters:
    id_delta[('1',l)] = '2'
for d in digits + letters:
    id_delta[('2',d)] = '2'

keys_list_id = list(id_delta.keys())
T_id = DFA(set(['1','2']),set(letters+digits),id_delta,'1','2',name_id,keys_list_id)

#define = token
name_ass = '='
ass_delta = {
    ('1','=') : '2',
}
keys_list_ass = list(ass_delta.keys())
T_ass = DFA(set(['1','2']),set(['=']),ass_delta,'1','2',name_ass,keys_list_ass)


#define ( token
name_p1 = '('
p1_delta = {
    ('1','(') : '2',
}
keys_list_p1 = list(p1_delta.keys())
T_p1 = DFA(set(['1','2']),set(['(']),p1_delta,'1','2',name_p1,keys_list_p1)

#define ) token
name_p2 = ')'
p2_delta = {
    ('1',')') : '2',
}
keys_list_p2 = list(p2_delta.keys())
T_p2 = DFA(set(['1','2']),set([')']),p2_delta,'1','2',name_p2,keys_list_p2)

#define , token
name_cm = ','
cm_delta = {
    ('1',',') : '2',
}
keys_list_cm = list(cm_delta.keys())
T_cm = DFA(set(['1','2']),set([',']),cm_delta,'1','2',name_cm,keys_list_cm)

#define let token
name_let = 'let'
let_delta = {
    ('1','l') : '2',
    ('2','e') : '3',
    ('3','t') : '4',
}
keys_list_let = list(let_delta.keys())
T_let = DFA(set(['1','2','3','4']),set(['l','e','t']),let_delta,'1','4',name_let,keys_list_let)

#define in token
name_in = 'in'
in_delta = {
    ('1','i') : '2',
    ('2','n') : '3',
}
keys_list_in = list(in_delta.keys())
T_in = DFA(set(['1','2','3']),set(['i','n']),in_delta,'1','3',name_in,keys_list_in)

#define end token
name_end = 'end'
end_delta = {
    ('1','e') : '2',
    ('2','n') : '3',
    ('3','d') : '4',
}
keys_list_end = list(end_delta.keys())
T_end = DFA(set(['1','2','3','4']),set(['e','n','d']),end_delta,'1','4',name_end,keys_list_end)

#define print token
name_print = 'print'
print_delta = {
    ('1','p') : '2',
    ('2','r') : '3',
    ('3','i') : '4',
    ('4','n') : '5',
    ('5','t') : '6',
}
keys_list_print = list(print_delta.keys())
T_print = DFA(set(['1','2','3','4','5','6']),set(['p','r','i','n','t']),print_delta,'1','6',name_print,keys_list_print)

#define ; token
name_sm = ';'
sm_delta = {
    ('1',';') : '2',
}
keys_list_sm = list(sm_delta.keys())
T_sm = DFA(set(['1','2']),set([';']),sm_delta,'1','2',name_sm,keys_list_sm)

#define if token
name_if = 'if'
if_delta = {
    ('1','i') : '2',
    ('2','f') : '3',
}
keys_list_if = list(if_delta.keys())
T_if = DFA(set(['1','2','3']),set(['i','f']),if_delta,'1','3',name_if,keys_list_if)

#define else token
name_else = 'else'
else_delta = {
    ('1','e') : '2',
    ('2','l') : '3',
    ('3','s') : '4',
    ('4','e') : '5',
}
keys_list_else = list(else_delta.keys())
T_else = DFA(set(['1','2','3','4','5']),set(['e','l','s','e']),else_delta,'1','5',name_else,keys_list_else)

#define while token
name_while = 'while'
while_delta = {
    ('1','w') : '2',
    ('2','h') : '3',
    ('3','i') : '4',
    ('4','l') : '5',
    ('5','e') : '6',
}
keys_list_while = list(while_delta.keys())
T_while = DFA(set(['1','2','3','4','5','6']),set(['w','h','i','l','e']),while_delta,'1','6',name_while,keys_list_while)

#define do token
name_do = 'do'
do_delta = {
    ('1','d') : '2',
    ('2','o') : '3',
}
keys_list_do = list(do_delta.keys())
T_do = DFA(set(['1','2','3']),set(['d','o']),do_delta,'1','3',name_do,keys_list_do)

#define { token
name_a1 = '{'
a1_delta = {
    ('1','{') : '2',
}
keys_list_a1 = list(a1_delta.keys())
T_a1 = DFA(set(['1','2']),set(['{']),a1_delta,'1','2',name_a1,keys_list_a1)

#define } token
name_a2 = '}'
a2_delta = {
    ('1','}') : '2',
}
keys_list_a2 = list(a2_delta.keys())
T_a2 = DFA(set(['1','2']),set(['}']),a2_delta,'1','2',name_a2,keys_list_a2)

#define and token
name_and = 'and'
and_delta = {
    ('1','a') : '2',
    ('2','n') : '3',
    ('3','d') : '4',
}
keys_list_and = list(and_delta.keys())
T_and = DFA(set(['1','2','3','4']),set(['a','n','d']),and_delta,'1','4',name_and,keys_list_and)

#define or token
name_or = 'or'
or_delta = {
    ('1','o') : '2',
    ('2','r') : '3',
}
keys_list_or = list(or_delta.keys())
T_or = DFA(set(['1','2','3']),set(['o','r']),or_delta,'1','3',name_or,keys_list_or)

#define not token
name_not = 'not'
not_delta = {
    ('1','n') : '2',
    ('2','o') : '3',
    ('3','t') : '4',
}
keys_list_not = list(not_delta.keys())
T_not = DFA(set(['1','2','3','4']),set(['n','o','t']),not_delta,'1','4',name_not,keys_list_not)

#define == token
name_eq = '=='
eq_delta = {
    ('1','=') : '2',
    ('2','=') : '3',
}
keys_list_eq = list(eq_delta.keys())
T_eq = DFA(set(['1','2','3']),set(['=']),eq_delta,'1','3',name_eq,keys_list_eq)

#define <> token
name_x = '<>'
x_delta = {
    ('1','<') : '2',
    ('2','>') : '3',
}
keys_list_x = list(x_delta.keys())
T_x = DFA(set(['1','2','3']),set(['<','>']),x_delta,'1','3',name_x,keys_list_x)

#define > token
name_b = '>'
b_delta = {
    ('1','>') : '2',
}
keys_list_b = list(b_delta.keys())
T_b = DFA(set(['1','2']),set(['>']),b_delta,'1','2',name_b,keys_list_b)

#define >= token
name_be = '>='
be_delta = {
    ('1','>') : '2',
    ('2','=') : '3',
}
keys_list_be = list(be_delta.keys())
T_be = DFA(set(['1','2','3']),set(['>','=']),be_delta,'1','3',name_be,keys_list_be)

#define < token
name_s = '<'
s_delta = {
    ('1','<') : '2',
}
keys_list_s = list(s_delta.keys())
T_s = DFA(set(['1','2']),set(['<']),s_delta,'1','2',name_s,keys_list_s)

#define <= token
name_se = '<='
se_delta = {
    ('1','<') : '2',
    ('2','=') : '3',
}
keys_list_se = list(se_delta.keys())
T_se = DFA(set(['1','2','3']),set(['<','=']),se_delta,'1','3',name_se,keys_list_se)

#define + token
name_sum = '+'
sum_delta = {
    ('1','+') : '2',
}
keys_list_sum = list(sum_delta.keys())
T_sum = DFA(set(['1','2']),set(['+']),sum_delta,'1','2',name_sum,keys_list_sum)

#define - token
name_min = '-'
min_delta = {
    ('1','-') : '2',
}
keys_list_min = list(min_delta.keys())
T_min = DFA(set(['1','2']),set(['-']),min_delta,'1','2',name_min,keys_list_min)

#define * token
name_mul = '*'
mul_delta = {
    ('1','*') : '2',
}
keys_list_mul = list(mul_delta.keys())
T_mul = DFA(set(['1','2']),set(['*']),mul_delta,'1','2',name_mul,keys_list_mul)

#define / token
name_div = '/'
div_delta = {
    ('1','/') : '2',
}
keys_list_div = list(div_delta.keys())
T_div = DFA(set(['1','2']),set(['/']),div_delta,'1','2',name_div,keys_list_div)

#define ** token
name_pow = '**'
pow_delta = {
    ('1','*') : '2',
    ('2','*') : '3',
}
keys_list_pow = list(pow_delta.keys())
T_pow = DFA(set(['1','2','3']),set(['*']),pow_delta,'1','3',name_pow,keys_list_pow)

#define whitespace token
name_w = 'white'
w_delta = {
    ('1',' ') : '2',
    ('2',' ') : '2',
}
keys_list_w = list(w_delta.keys())
T_white = DFA(set(['1','2']),set([' ']),w_delta,'1','2',name_w,keys_list_w)

#define integer token
name_int = 'num'
int_delta ={}

#fill int_delta
# for sign in signs:
#     int_delta[('1',sign)] = '2'

for digit in digits:
    int_delta[('2',digit)] = '3'

for digit in digits:
    int_delta[('1',digit)] = '3'

for digit in digits:
    int_delta[('3',digit)] = '3'

keys_list_int = list(int_delta.keys())
T_int = DFA(set(['1','2','3']),set(signs+digits),int_delta,'1','3',name_int,keys_list_int)

#define float token
name_float = 'fnum'
float_delta = {}

#fill float_delta

# for sign in signs:
#     float_delta[('1',sign)] = '2'


for digit in digits:
    float_delta[('1',digit)] = '3'

for digit in digits:
    float_delta[('2',digit)] = '3'

float_delta[('3','.')] = '4'


for digit in digits:
    float_delta[('5',digit)] = '4'

for digit in digits:
    float_delta[('4',digit)] = '4'

for digit in digits:
    float_delta[('3',digit)] = '3'

for digit in digits:
    float_delta[('4',digit)] = '4'

keys_list_float = list(float_delta.keys())

T_float = DFA(set(['1','2','3','4']),set(signs+digits+['.']),float_delta,'1','4',name_float,keys_list_float)

#define elmi token
name_elmi = 'enum'
elmi_delta = {}

#fill elmi delta
# for sign in signs:
#     elmi_delta[('1',sign)] = '2'

for digit in digits:
    elmi_delta[('2',digit)] = '3'

for digit in digits:
    elmi_delta[('3',digit)] = '3'


for digit in digits:
    elmi_delta[('1',digit)] = '3'

elmi_delta[('3','.')] = '4'

for digit in digits:
    elmi_delta[('4',digit)] = '5'

for digit in digits:
    elmi_delta[('5',digit)] = '5'

elmi_delta[('5','e')] = '6'

for sign in signs:
    elmi_delta[('6',sign)] = '7'

for digit in digits:
    elmi_delta[('6',digit)] = '8'

# for digit in digits:
#     elmi_delta[('7',digit)] = '7'

for digit in digits:
    elmi_delta[('7',digit)] = '8'

for digit in digits:
    elmi_delta[('8',digit)] = '8'

keys_list_elmi = list(elmi_delta.keys())

T_elmi = DFA(set(['1','2','3','4','5','6','7','8']),set(digits+signs+['e']+['.']),elmi_delta,'1','8',name_elmi,keys_list_elmi)

tokens_list = [T_elmi,T_float,T_int,T_id,T_ass,T_p1,T_p2,T_cm,T_let,T_in,T_end,T_print,T_sm,T_if,T_else,T_while,T_do,T_a1,T_a2,T_and,T_or,T_not,T_eq,T_x,T_b,T_be,T_s,T_se,T_sum,T_min,T_mul,T_div,T_pow,T_white]     

keywords = ['let','in','end','print','if','else','while','do','and','or','not']

def maximal_munch(input_string):
    input_string += ' '
    token_name = ''
    maximaMunch = ''
    while len(input_string) != 0:

        a = len(maximaMunch)
        input_string = input_string[a:]

        if token_name in ["num", "enum", "fnum"] and input_string[0:1] in letters:
            print("error, %s can not come after a num" %input_string[0:1])
            i = 0
            while input_string[i:i + 1] in letters:
                i += 1

            maximaMunch = input_string[0:i]

            valid_DFA = []
            accepted_dfa = {}
            token_name = ''
        
        else:
            
            valid_DFA = []
            accepted_dfa = {}
            token_name = ''

            for ctoken in tokens_list:
                if ('1' ,input_string[0:1]) in ctoken.keys_list:
                    valid_DFA.append(ctoken)        
                
            for vtoken in valid_DFA:
                count = 0
                walked = ''
                current = '1'
                length = 0
                isFinal = False

                for char in input_string:
                    if (current, char) in vtoken.delta:
                        isFinal, current = vtoken.execute(current, char)
                        count += 1
                        walked += char
                    else:
                        if isFinal == True:
                            accepted_dfa[vtoken.name] = (count, walked)
                        break
            
            for atoken in accepted_dfa:
                if accepted_dfa[atoken][0] > length:
                    length = accepted_dfa[atoken][0]
                    maximaMunch = accepted_dfa[atoken][1]
                    token_name = atoken
                elif accepted_dfa[atoken][0] == length:
                    if atoken == 'id':
                        pass
                    else:
                        length = accepted_dfa[atoken][0]
                    maximaMunch = accepted_dfa[atoken][1]
                    token_name = atoken
                        
            if token_name != 'white' and  token_name != '':
                if token_name == 'id':
                    output_file.write(f'[id({maximaMunch})]\n')
                elif token_name in keywords:
                    output_file.write(f'[{maximaMunch}(keyword)]\n')
                elif token_name == 'enum' or token_name =='fnum' or token_name == 'num':
                    if input_string[length:length+1] not in letters: 
                        output_file.write(f'[{maximaMunch}(num)]\n') 
                else:
                    output_file.write(f'[{maximaMunch}]\n')
            
            if len(valid_DFA) == 0 and input_string[0:1] != '':
                maximaMunch = input_string[0:1]


maximal_munch(data)
             maximaMunch = input_string[0:1]


maximal_munch(data)
