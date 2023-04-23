# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the
# form of a phone number. -> "(123) 456-7890"

def create_phone_number(n):
    # # 1st:
    # return f"({''.join([str(i) for i in n[:3]])}) {''.join([str(i) for i in n[3:6]])}-{''.join([str(i) for i in n[6:]])}"

    #2nd:
    s = ''.join([str(i) for i in n])
    return f'({s[0:3]}) {s[3:6]}-{s[6:]}'

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

