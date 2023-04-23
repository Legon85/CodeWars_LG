def to_camel_case(text):
    # 1st method:

    for i in range(1, len(text)-text.count('-') - text.count('_')):
        if text[i] == '-' or text[i] == '_':
            text = text.replace(text[i]+text[i+1], text[i+1].upper())
    print(text)

    # # another method:
    #
    # text = text.replace('_', ' ').replace('-', ' ')
    # words = text.split()
    # print( ''.join([w.capitalize() if w != words[0] else w for w in words ]))

    # # 2nd method:
    #
    # text2 = ''
    # for i in range(len(text)):
    #     if text[i] == '-' or text[i] == '_':
    #         pass
    #     else:
    #         if text[i - 1] == '_' or text[i - 1] == '-':
    #             text2 += text[i].upper()
    #         else:
    #             text2 += text[i]
    #
    # print(text2)
    #
    # # 3rd method:
    #
    # text3 = []
    # for i in range(len(text)):
    #     if text[i] == '-' or text[i] == '_':
    #         pass
    #     else:
    #         text3.append(text[i]) if text[i-1] != '_' or text[i-1] != '-' else text3.append(text[i+1].upper())
    #
    # print(''.join(text3))


to_camel_case("the-stealth-warrior")
to_camel_case("The_Stealth_Warrior")
to_camel_case("A-B-C")