import operator
import binascii
from functools import reduce

# converts list of chars to string
def to_str(h):
    if (len(h) < 1):
        return ""
    return reduce(operator.add, h)

little_endian = lambda x: int(to_str(list(reversed(split_every(format(x, "064b"), 8)))), 2)
word_to_int = lambda x: int(str(binascii.a2b_base64(x)), 2)

# split list for lists of lengths of n
def split_every (list, n):
    return [list[i:i+n] for i in range(0,len(list), n)]

# in bytes
def pad_word(word, size):
    ext_len = size-len(word)%size
    if (ext_len == 1):
        word += chr(0x86)
        return word
    word += to_str([chr(0x06)] + [chr(0x0)]*(ext_len-2) + [chr(0x80)]*(ext_len-abs(ext_len-2)-1))
    return word

def split_at(word, n):
    return [word[:n], word[n:]]

# Bitwise rotation of W with length of w by r bits to left
def rot(W, r, w):
    r = r % w
    b = split_at(format(W, "0"+str(w)+"b"), r)
    return int(b[1] + b[0], base=2)
