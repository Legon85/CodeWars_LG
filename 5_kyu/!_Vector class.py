# Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

# a = Vector([1, 2, 3])
# b = Vector([3, 4, 5])
# c = Vector([5, 6, 7, 8])

# a.add(b)      # should return a new Vector([4, 6, 8])
# a.subtract(b) # should return a new Vector([-2, -2, -2])
# a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
# a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
# a.add(c)      # raises an exception

from math import sqrt

# class Vector:
#     def __init__(self, coords):
#         self.coords = coords
#
#     def __str__(self):
#         return f"({','.join((str(i) for i in self.coords))})"
#         # return str(tuple(self.coords))
#
#     def checker(self, b):
#         if len(self.coords) == len(b.coords):
#             return True
#         return "'The lenghts of vectors should be equal'"
#
#     def add(self, *args):
#         if Vector.checker(self, b):
#             for i,c in enumerate(self.coords):
#                 self.coords[i] += b.coords[i]
#             return Vector(self.coords)
#
#     def subtract(self, *args):
#         if Vector.checker(self, b):
#             for i,c in enumerate (self.coords):
#                 self.coords[i] -= b.coords[i]
#             return Vector(self.coords)
#
#
#     def dot(self, *args):
#         if Vector.checker(self, b):
#             for i,c in enumerate (self.coords):
#                 self.coords[i] *= b.coords[i]
#             return sum(self.coords)
#
#
#     def norm(self):
#         return sqrt(sum(el**2 for el in self.coords))
#
#
#     def equals(self, *args):
#         if Vector.checker(self, b):
#             return self.coords == b.coords
#
#
#
#
# a = Vector([1, 2, 3])
# b = Vector([3, 4, 5])
#
# # print(a.__dict__)
# # print(a.coords)
#
# # print(a)
# # print(a.add(b))
# # print(a.subtract(b))
# # print(a.dot(b))
# print(a.norm())



# class Vector:
#     def __init__(self, coords):
#         self.coords = coords
#
#     def __str__(self):
#         return f"({','.join((str(i) for i in self.coords))})"
#         # return str(tuple(self.coords))
#
#     def checker(self, v):
#         if len(self.coords) == len(v.coords):
#             return True
#         return "'The lenghts of vectors should be equal'"
#
#     def add(self, v):
#         if Vector.checker(self, v):
#             for i, c in enumerate(self.coords):
#                 self.coords[i] += v.coords[i]
#             return Vector(self.coords)
#
#     def subtract(self, v):
#         if Vector.checker(self, v):
#             for i, c in enumerate(self.coords):
#                 self.coords[i] -= v.coords[i]
#             return Vector(self.coords)
#
#     def dot(self, v):
#         if Vector.checker(self, v):
#             for i, c in enumerate(self.coords):
#                 self.coords[i] *= v.coords[i]
#             return sum(self.coords)
#
#     def norm(self):
#         return sqrt(sum(el ** 2 for el in self.coords))
#
#     def equals(self, v):
#         if Vector.checker(self, v):
#             return self.coords == v.coords
#
#
#
# a = Vector([1, 2, 3])
# b = Vector([3, 4, 5])
#
# # print(a.__dict__)
# # print(a.coords)
#
# # print(a)
# # print(a.add(b))
# print(a.subtract(b))
# # print(a.dot(b))
# # print(a.norm())


class Vector:
    def __init__(self, coords):
        self.coords = coords

    def __str__(self):
#         return f"({','.join((str(i) for i in self.coords))})"
        return str(tuple(self.coords)).replace(" ", "")

    def checker(self, v):
        if len(self.coords) == len(v.coords):
            return True
        return "'The lenghts of vectors should be equal'"

    def add(self, v):
        if Vector.checker(self, v):
            for i, c in enumerate(self.coords):
                self.coords[i] += v.coords[i]
            return Vector(self.coords)

    def subtract(self, v):
        if Vector.checker(self, v):
            for i, c in enumerate(self.coords):
                self.coords[i] -= v.coords[i]
            return Vector(self.coords)
#         if Vector.checker(self, v):
#             coords = []
#             for i in range(len(self.coords)):
#                 coords.append(self.coords[i] - v.coords[i])
#             return Vector(coords)


    def dot(self, v):
        if Vector.checker(self, v):
            for i, c in enumerate(self.coords):
                self.coords[i] *= v.coords[i]
            return sum(self.coords)

    def norm(self):
        # for i, c in enumerate(self.coords):
        #     self.coords[i] = self.coords[i] ** 2
        # return (sum(self.coords))**0.5
        # return (sum(el ** 2 for el in self.coords))**0.5
        return (self.coords[0] ** 2 + self.coords[1] ** 2 + self.coords[2] ** 2) ** 0.5

    def equals(self, v):
        if Vector.checker(self, v):
            return self.coords == v.coords


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])


# print(a)
# print(a.add(b))
# print(a.subtract(b))
# print(a.dot(b))
print(a.norm())

