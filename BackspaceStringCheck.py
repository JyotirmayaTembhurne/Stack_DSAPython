s = "a##c"
t = "#a#c"
s_stack = list()
t_stack = list()

for char in s:
    if len(s_stack) != 0 and char == "#":
        s_stack.pop()
    else:
        s_stack.append(char)
for char in t:
    if len(t_stack) != 0 and char == "#":
        t_stack.pop()
    elif char != "#":
        t_stack.append(char)
print(s_stack, t_stack)
print(s_stack == t_stack)
