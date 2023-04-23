# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The
# function should return true if the string is valid, and false if it's invalid.

def valid_parentheses(paren_str):
    # k = 0
    # for i in paren_str:
    #     if i == "(":k += 1
    #     if i == ")":k -= 1
    #     if k < 0:return False
    # return k == 0
    #
    # 2nd method: cool!!!
    while "()" in paren_str:
        paren_str = paren_str.replace("()", "")
    return paren_str == ""


print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses("("))
print(valid_parentheses("(())((()())())" ))
print(valid_parentheses("(()())()"))
print(valid_parentheses("(()(()()()())(()())))(()"))
print()
print(valid_parentheses(")("))
print(valid_parentheses("()()("))
print(valid_parentheses("((())"))
print(valid_parentheses("())(()"))
