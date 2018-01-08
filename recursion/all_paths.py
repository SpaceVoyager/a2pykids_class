# prints all possible paths through a r x c grid
# from upper left corner to lower right corner
# when only eastward and southward moves are allowed
def print_paths(r, c, current_path):
    if r==0 and c==0:
        print current_path
        return
    if r == 0 and c >0:
        for i in range(c):
            current_path += 'E'
        print current_path
        return
    if c == 0 and r >0:
        for i in range(r):
            current_path += 'S'
        print current_path
        return
    print_paths(r, c-1, current_path + 'E')
    print_paths(r-1, c, current_path + 'S')

# print_paths(2,2, '')

# returns a list of strings representing all possible paths through
# a r x c grid from upper left corner to lower right corner when only
# eastward and southward moves are allowed
def find_all_paths(r, c):
    if r==0 and c==0:
        return []
    if r == 0 and c >0:
        path = ''
        for i in range(c):
            path += 'E '
        return [path]
    if c == 0 and r >0:
        path = ''
        for i in range(r):
            path += 'S '
        return [path]
    subsolution1 = find_all_paths(r, c-1)
    subsolution2 = find_all_paths(r-1, c)
    mysolution = []
    for s in subsolution1:
        mysolution.append('E ' + s)
    for s in subsolution2:
        mysolution.append('S ' + s)
    return mysolution


def print_paths2(r, c, current_path):
    if r==0 and c==0:
        print current_path
        return
    if c > 0:
        print_paths2(r, c-1, current_path + 'E')
    if r > 0:
        print_paths2(r-1, c, current_path + 'S')


def print_paths3(r, c, current_path):
    if r==0 and c==0:
        print current_path
        return
    if c > 0:
        current_path.append('E')
        print_paths3(r, c-1, current_path)
        current_path.pop()
    if r > 0:
        current_path.append('S')
        print_paths3(r-1, c, current_path)
        current_path.pop()


print_paths2(2, 2, '')
print_paths3(2, 2, [])

'''
print 'there are ' + str(len(all_paths)) + ' possible paths:'
for p in all_paths:
    print p
'''