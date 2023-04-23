# def order(sentence):
#         f = {}
#         for i in sentence.split():
#                 for c in i:
#                         if c.isdigit():
#                                 f[c] = ''.join(i)
#         return ' '.join([i[1] for i in sorted(f.items(), key=lambda f: sorted(f))])
#
# print(order("is2 Thi1s T4est 3a"))


# def order(sentence):
#         l = []
#         for i in range(1, 10):
#                 for word in sentence.split():
#                         if str(i) in word:
#                                 l.append(word)
#         print(' '.join(l))
#
#
# order("is2 Thi1s T4est 3a")

# вышеописанное решение можно записать в одну строку:
def order(sentence):
        return ' '.join([word for i in range(1, 10) for word in sentence.split() if str(i) in word])

print(order("is2 Thi1s T4est 3a"))
