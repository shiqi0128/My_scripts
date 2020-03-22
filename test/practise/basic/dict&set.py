d = {
    'michael': 95,
    'bob': 85,
    'tracy': 75
}

print('michael:', d['michael'])
print('bob:', d['bob'])
print('tracy:', d['tracy'])
# print(d[0])
d.pop('bob')
print(d)
d.get('michael', 0)
print(d)

s1 = set([1, 2, 2, 3, 3])
s2 = set([1, 5])
print(s1 & s2)
print(s1 | s2)
# s.add(4)
# print(s)
# s.remove(4)
# print(s)

d = {
    'bella': 55
}
print('bella=', d['bella'])

a = [3, 2, 7, 0, 8, 6]
a.sort(reverse = True)
print('a =', a)

a = '123'
a.replace('1', 'A')
print(a)