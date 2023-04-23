# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the
# other elements.

def move_zeros(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]

    # 2nd method:
    # return [i for i in lst if i != 0] + [0] * lst.count(0)

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros([0, 0]))
print(move_zeros([0]))
print(move_zeros([]))
