# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list
# of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]


def max_sequence(arr):
    lst = []
    if len(arr) == 0:
        return 0
    elif sum(arr) < 0:
        for d in arr:
            if d > 0 in arr:
                for c in range(len(arr)):
                    pivot = arr[c]
                    left = [i for i in arr[:c]]
                    right = [i for i in arr[c + 1:]]
                    while left or right:
                        # print(left, pivot, right)
                        lst.append(sum(left) + pivot + sum(right))
                        if left and right:
                            left.pop(0)
                            right.pop(-1)
                        else:
                            if right:
                                right.pop(-1)
                            else:
                                left.pop(0)
                return max(lst), lst
            else:
                return 0
    else:
        for c in range(len(arr)):
            pivot = arr[c]
            left = [i for i in arr[:c]]
            right = [i for i in arr[c + 1:]]
            while left or right:
                # print(left, pivot, right)
                lst.append(sum(left) + pivot + sum(right))
                if left and right:
                    left.pop(0)
                    right.pop(-1)
                else:
                    if right:
                        right.pop(-1)
                    else:
                        left.pop(0)
        return max(lst), lst

    #     for j in range(len(left)):
    #         lst.append(sum(left[-j:]) + pivot)
    #     for c in range(len(right)+1):
    #         lst.append(pivot + sum(right[:c]))

    # for i in range(len(arr)):
    #     for j in range(i+1,len(arr)):
    #         lst.append(arr[i] + sum(arr[i+1:j+1]))
    # for c in range(len(arr)):
    #     for k in range(c+1,len(arr)):
    #         lst.append(arr[::-1][c] + sum(arr[::-1][c + 1:k + 1]))
    # return max(lst)
    # for i in range(len(arr)):
    #     pivot = arr[i]
    #     for j in range(i+1,len(arr)):
    #         right = arr[i+1:j+1]
    #         left = arr - right
    #         print(left, pivot, right)


print(max_sequence([]))
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]))
print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))
