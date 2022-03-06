from sys import stdin

st = stdin.readline().rstrip()
bomb_st = list(stdin.readline().rstrip())
'''
while True:
    if bomb_st not in st:
        break
    st = st.replace(bomb_st, "")
'''

n = len(bomb_st)
stk = []
for char in st:
    stk.append(char)
    if stk[-n:] == bomb_st:
        del stk[-n:]        # pop()보다 빠르네
print("".join(stk) if stk else "FRULA")
