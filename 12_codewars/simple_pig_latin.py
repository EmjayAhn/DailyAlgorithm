# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
import string
def pig_it(text):
    result_list = []
    result = ' '
    for index, word in enumerate(text.split()):
        if word in string.punctuation:
            result_list.append(word)
            continue
        pop_char = word[0]
        word = word[1:]
        word += pop_char
        word += 'ay'
        result_list.append(word)

    result = result.join(result_list)
    return result

if __name__=='__main__':
    print(pig_it('Pig latin is cool'))
    print(pig_it('Hello world !'))