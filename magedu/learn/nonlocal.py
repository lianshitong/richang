c = 1
def foo():
    global c
    c = 1
    def inner():
        global c
        c += 1
        return c
    return inner
print(foo())