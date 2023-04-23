# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)


def make_readable(seconds):
    # lst = [str(seconds // 3600), str((seconds % 3600) // 60), str((seconds % 3600) % 60)]
    # return ":".join([i if int(i) > 9 else '0'+i for i in [str(seconds // 3600), str((seconds % 3600) // 60), str((seconds % 3600) % 60)]])

    # 2nd method
    return f'{(seconds // 3600):02d}:{((seconds % 3600) // 60):02d}:{((seconds % 3600) % 60):02d}'

print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))