def decode_morse(morse_code):
    morse_dict = {".-": "A",
              "-...": "B",
              "-.-.": "C",
              "-..": "D",
              ".": "E",
              "..-.": "F",
              "--.": "G",
              "....": "H",
              "..": "I",
              ".---": "J",
              "-.-": "K",
              ".-..": "L",
              "--": "M",
              "-.": "N",
              "---": "O",
              ".--.": "P",
              "--.-": "Q",
              ".-.": "R",
              "...": "S",
              "-": "T",
              "..-": "U",
              "...-": "V",
              ".--": "W",
              "-..-": "X",
              "-.--": "Y",
              "--..": "Z",
              "-----": "0",
              ".----": "1",
              "..---": "2",
              "...--": "3",
              "....-": "4",
              ".....": "5",
              "-....": "6",
              "--...": "7",
              "---..": "8",
              "----.": "9"}
    # for key in morse_dict.keys():
    #     print(key, end='/')
    # print()
    # for i in morse_code.split('   '):
    #     for d in i.split(' '):
    #         if d in morse_dict:
    #             print(morse_dict[d])
    print((' ').join([str([morse_dict[d] for d in i.split(' ')]) for i in morse_code.split('   ')]))
    print((' ').join([('').join([morse_dict[d] for d in i.split(' ')]) for i in morse_code.split('   ')]).strip())

decode_morse('.... . -.--   .--- ..- -.. .')
decode_morse('. .')