from itertools import chain
try:
    from itertools import zip_longest  # Python 3
except ImportError:
    from itertools import izip_longest as zip_longest  # Python 2

for i in range(10000000):
    s1 = 'ABCDEFH' + str(i)
    s2 = '123456789' + str(i)
    result = ''.join(chain(*zip_longest(s1, s2, fillvalue='')))  # the one-liner
    if i == 0: print(result)
