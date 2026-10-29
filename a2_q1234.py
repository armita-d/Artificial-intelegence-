# CSC421 ASSIGNMENT 2 - QUESTION 1

def evaluate(s):
    pass

# examples
e1_1 = "& Z O"
e1_2 = "| O O"
e1_3 = "| Z Z"
e1_4 = "& U U"
e1_5 = "& U Z"

res_e1_1 = evaluate(e1_1)
res_e1_2 = evaluate(e1_2)
res_e1_3 = evaluate(e1_3)


print(f'{e1_1} = {res_e1_1}')
print(f'{e1_2} = {res_e1_1}')
print(f'{e1_3} = {res_e1_3}')


# CSC421 ASSIGNMENT 2 - QUESTION 2

d = {'foo': "Z", 'b': "O"}
print(d)
e2_1 = '& Z O'
e2_2 = '& foo O'
e2_3 = '& foo b'

def evaluate_with_bindings(s,d):
    pass


res_e2_1 = evaluate_with_bindings(e2_1,d)
res_e2_2 = evaluate_with_bindings(e2_2,d)
res_e2_3 = evaluate_with_bindings(e2_3,d)

print(f'{e2_1} = {res_e2_1}')
print(f'{e2_2} = {res_e2_2}')
print(f'{e2_3} = {res_e2_3}')


# CSC421 ASSIGNMENT 2 - QUESTIONS 3,4

def prefix_eval(input_str, d):
    pass

d = {'a': 'O', 'b': 'Z', 'c': 'U'}
e3_1 = "& a | Z O"
e3_2 = "& O | O b"
e3_3 = "| O & ~ b b"
e3_4 = "& ~ a & O O"
e3_5 = "| O & ~ b c"
e3_6 = "& ~ a & c O"
e3_7 = "& & c c & c c"

print(d)
for e in [e3_1,e3_2,e3_3,e3_4,e3_5,e3_6, e3_7]:
    print("%s \t = %s" % (e, prefix_eval(e,d)))

# EXPECTED OUTPUT
# & Z O = Z
# | O O = Z
#| Z Z = Z
# {'foo': 'Z', 'b': 'O'}
# & Z O = Z
# & foo O = Z
# & foo b = Z
# {'a': 'O', 'b': 'Z', 'c': 'U'}
# & a | Z O        = O
# & O | O b        = O
# | O & ~ b b      = O
# & ~ a & O O      = Z
# | O & ~ b c      = O
# & ~ a & c O      = Z
# & & c c & c c    = U
    




