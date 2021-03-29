string = input("Enter a string \n")
brackets = input("Enter possible brackets \n")

open_brackets = ['(', '[', '{', '<']
close_brackets = [')', ']', '}', '>']
stack = []
for i in string:
    if i in open_brackets:
        stack.append(i)
    elif i in close_brackets:
        stack.pop()


