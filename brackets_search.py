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
        print("Possible brackets hadn't founded\n True, None, None\n")
        exit(1)
    if len(false_brackets):
        print("NOTIFICATION! The next bracket(s) is(are) incorrect and was(were) removed", *false_brackets)
    return list(possible_brackets), list(close_brackets)


string = input("Enter a string \n")

op_brackets, cl_brackets = brackets_validation()

stack = {}
info = [True, None, None]

for element, i in enumerate(string):
    if i in op_brackets:
        stack.update({element: i})
    elif i in cl_brackets:
        if 0 == len(stack):
            info[0] = False
            break
        if cl_brackets.index(i) == op_brackets.index(list(stack.values())[-1]):
            stack.popitem()
        else:
            info = [False, {i: element}, {stack[list(stack)[-1]]: list(stack)[-1] }]
            break
if 0 != len(stack) and True == info[0]:
    info = [False, None, {list(stack)[-1]: stack[list(stack)[-1]]}]

print(info[0], info[1], info[2], sep=', ')
