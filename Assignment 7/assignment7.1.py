def chop(a):
    if len(a) >= 2:
        a.pop(0)
        a.pop(-1)

def middle(b):
    if len(b) >= 3:
        return b[1:-1]
    else:
        return[]

a = [1,2,3,4]

print("My list before call chop function =>",a)
chop(a)
print("My list after call chop function =>",a)

a = [1,2,3,4]
print(f"My list before call middle function =>{a}")
new = middle(a)
print("My list after call middle function =>",a)
print("new list after call middle function =>",new)
