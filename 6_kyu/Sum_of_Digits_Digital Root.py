def digital_root(n):
    # 1st:
    # return sum([int(i) for i in str(n)]) if len(str(sum([int(i) for i in str(n)]))) == 1 else digital_root(sum([int(i) for i in str(n)]))
    # 2nd: болле логичный
    return n if n < 10 else digital_root(sum([int(i) for i in str(n)]))


print(digital_root(16))
print(digital_root(132189))
print(digital_root(493193))