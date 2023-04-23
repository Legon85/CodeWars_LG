def tribonacci(signature, n):
        for i in range(3, n): signature.append(sum(signature[-3:]))
        return signature[:n]


print(tribonacci([1, 1, 1], 10))
# -> [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print(tribonacci([3, 2, 1], 10))
# -> [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])
print(tribonacci([300, 200, 100], 0))
# ->[]
print(tribonacci([1, 1, 1], 1))
# -> [1]
print(tribonacci([147, 567, 100], 2))
# -> [147, 567]

