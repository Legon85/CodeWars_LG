def spin_words(sentence):
    # 1st method:
    # return ' '.join([''.join(list(reversed(i))) if len(i) > 5 else i for i in sentence.split()])
    # 2nd method:
    return ' '.join([i[::-1] if len(i) < 4 else i for i in sentence.split()])


print(spin_words("Hey fellow warriors"))