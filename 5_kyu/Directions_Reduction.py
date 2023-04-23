# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

# Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

def dirReduc(arr):
    try:
        if len(arr) < 2 or len(set(arr)) <= 1 or  arr.count("NORTH") == arr.count("SOUTH") == arr.count("WEST") == arr.count("EAST"):
            return arr
        else:
            for i, c in enumerate(arr[:-1]):
                if arr[i] == "NORTH" and arr[i+1] == "SOUTH":
                    arr[i] = []
                    arr[i+1]= []
                elif arr[i] == "SOUTH" and arr[i+1] == "NORTH":
                    arr[i] = []
                    arr[i+1]= []
                elif arr[i] == "EAST" and arr[i+1] == "WEST":
                    arr[i] = []
                    arr[i+1]= []
                elif arr[i] == "WEST" and arr[i+1] == "EAST":
                    arr[i] = []
                    arr[i+1]= []
                elif len(arr) < 3: return arr
            arr = [i for i in arr if i]
            return dirReduc(arr)
    except:
        return arr



print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))
print(dirReduc(['NORTH', 'NORTH']))
print(dirReduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH']))
print(dirReduc(["EAST", "NORTH"]))
print(dirReduc(['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH']))

