from functools import reduce


# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list
# of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]

def max_sequence(arr):
    lst = []
    if len(arr) == 0: return 0
    elif len(arr) > 0:
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                lst.append(sum(arr[:i]))
                lst.append(sum(arr[i:j + 1]))
                lst.append(sum(arr[i:]))
        if max(lst) > 0: return max(lst)
        else: return 0


print(max_sequence([]))
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]))
print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))
