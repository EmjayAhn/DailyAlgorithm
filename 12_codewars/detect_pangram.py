# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
import string

def is_pangram(s):
    lower_s = s.lower()
    for character in string.ascii_lowercase:
        if character not in lower_s:
            return False
    return True

if __name__ == '__main__':
    pangram = "The quick, brown fox jumps over the lazy dog!"
    print(is_pangram(pangram))
