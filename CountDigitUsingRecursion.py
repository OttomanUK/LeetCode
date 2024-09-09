def Count(n):
    if n == 0:
        return 0
    return 1 + Count(n//10)


result = Count(35455)
print(result)