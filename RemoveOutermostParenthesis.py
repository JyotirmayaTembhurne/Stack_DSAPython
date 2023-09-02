s = "(()())(())"
op = "()()()"
s = list(s)
indices = list()
length = len(s)
count = 0
string = str()
for i in range(length):
    if s[i] == "(":
        count += 1
    if s[i] == "(" and count == 1:
        indices.append(i)
    if s[i] == ")":
        count -= 1
    if s[i] == ")" and count == 0:
        indices.append(i)
print(indices)
for i in range(length):
    if i not in indices:
        string += s[i]
print(string)
