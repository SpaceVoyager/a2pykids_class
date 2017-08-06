b = [2173, 84238, -1, 1000]

def mymax(a):
    if len(a) == 1:
        return a[0]
    else:
        max_in_tail = mymax(a[1:])
        if a[0] < max_in_tail:
            return max_in_tail
        else:
            return a[0]

print mymax(b)