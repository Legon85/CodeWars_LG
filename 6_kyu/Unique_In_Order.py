def unique_in_order(sequence):
    # s = []
    # for i in range(len(sequence)):
    #     if i == 0 or sequence[i] != sequence[i-1]:
    #         s.append(sequence[i])
    # return s
    return [sequence[i] for i in range(len(sequence)) if i == 0 or sequence[i] != sequence[i-1]]

print(unique_in_order("AAAABBBCCDAABBB"))
# unique_in_order([])
# unique_in_order(())