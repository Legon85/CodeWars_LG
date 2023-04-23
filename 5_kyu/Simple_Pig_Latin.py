# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.

def pig_it(text):
    # for i in text.split():
    #     print(i)
        # print(i[1:]+i[0]+'ay')
    return ' '.join([i[1:]+i[0]+'ay' if i.isalpha() else i for i in text.split()])




print(pig_it('Pig latin is cool'))
print(pig_it('This is my string'))
print(pig_it("O tempora o mores !"))