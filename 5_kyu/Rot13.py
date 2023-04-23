# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the
# alphabet. ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
# characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet
# should be shifted, like in the original Rot13 "implementation".
# Please note that using encode is considered cheating.

# def rot13(message):
#     lst = []
#     for i in message:
#         if i.isalpha():
#             if 77 < ord(i) < 91 :
#                 lst.append(chr((65-13)+(ord(i) - 65)))
#             elif ord(i) <= 77:
#                 lst.append(chr(ord(i) + 13))
#             elif 109 < ord(i) < 123 :
#                 lst.append(chr((97-13)+(ord(i) - 97)))
#             elif 96 < ord(i) <= 109:
#                 lst.append(chr(ord(i) + 13))
#         else:
#             lst.append(i)
#     return ''.join(lst)


# 2nd method:
def rot13(message):
    result = ''
    for i in message:
        if (ord(i) >= ord('A') and ord(i) <= ord('M')) or (ord(i) >= ord('a') and ord(i) <= ord('m')):
            result += chr(ord(i) + 13)
        elif (ord(i) >= ord('N') and ord(i) <= ord('Z')) or (ord(i) >= ord('n') and ord(i) <= ord('z')):
            result += chr(ord(i) - 13)
        else:
            result += i
    return result




print(rot13('test')) # 'grfg'
print(rot13('Test')) # 'Grfg'
print(rot13('aA bB zZ 1234 *!?%')) # 'nN oO mM 1234 *!?%'
print(rot13('Codewars'))
print(rot13('n'))