# https://www.codewars.com/kata/587731fda577b3d1b0001196/train/python
def camel_case(string):
    result = ''
    for word in list(string.split()):
        camel_word = word[0].upper() + word[1:]
        result += camel_word
    
    return result
    


if __name__=='__main__':
    print(camel_case("hello case"))
    print(camel_case("camel case word"))
