# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
# must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.


def rgb(r, g, b):
    """1st method"""
    lst = []
    for i in [r, g, b]:
        if i > 255:
            lst.append(255)
        elif i < 0:
            lst.append(0)
        else:
            lst.append(i)
    return ''.join([f'{hex(i)[0]+hex(i)[-1].upper()}' if i < 16 else f'{(hex(i)[2:]).upper()}' for i in lst])

    """2nd method"""
    # return ''.join(['%02X' % max(0, min(x, 255)) for x in [r, g, b]])




print(rgb(0, 0, 0)) # -> "000000"
print(rgb(1, 2, 3)) # -> "010203"
print(rgb(255, 255, 255)) # -> "FFFFFF"
print(rgb(254, 253, 252)) # -> "FEFDFC"
print(rgb(-20, 275, 125)) # -> "00FF7D"
print(rgb(-185 ,308 ,12)) # -> '00FF0C'