from itertools import count
from hashlib import md5

def search_md5_hash(prefix, zeros=5):
    """
    >>> search_md5_hash('abcdef')
    609043
    >>> search_md5_hash('pqrstuv')
    1048970
    """
    prefix_h = md5()
    prefix_h.update(prefix.encode('ascii'))
    for i in count(1):
        h = prefix_h.copy()
        h.update(str(i).encode('ascii'))
        d = h.hexdigest()
        if all( c == '0' for c in d[:zeros] ):
            return i

if __name__ == '__main__':
    prefix = open('day04_input').read().strip()
    print(search_md5_hash(prefix, zeros=5))
    print(search_md5_hash(prefix, zeros=6))
