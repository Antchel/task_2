def brackets_validation():
    brackets = input("Enter possible brackets \n")
    open_brackets = ['(', '[', '{', '<']
    possible_brackets = []
    false_brackets = []
    close_brackets = []
    for i in brackets:
        if i in open_brackets:
            possible_brackets.append(i)
            if ord(i) == ord('('):
                close_brackets.append(chr(ord(i) + 1))
            else:
                close_brackets.append(chr(ord(i) + 2))
        else:
            false_brackets.append(i)
    if len(possible_brackets) == 0:
        print("Possible brackets hadn't founded")
        exit(1)
    if len(false_brackets):
        print("NOTIFICATION! The next bracket(s) is(are) incorrect and was(were) removed", *false_brackets)
    return possible_brackets, close_brackets


string = input("Enter a string \n")

op_brackets, cl_brackets = brackets_validation()

stack = []
print(cl_brackets)
for element, i in enumerate(string):
    if i in op_brackets:
        stack.append(i)
    elif i in cl_brackets:
        if cl_brackets.index(i) == op_brackets[cl_brackets.index(i)]:
            stack.pop()
        else:
            print(i)
            print(element)
            exit(5)
