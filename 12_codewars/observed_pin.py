# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python
import itertools
def get_pins(observed):
    key_dict = {'1': ['1', '2', '4'],
                '2': ['1', '2', '3', '5'],
                '3': ['2', '3', '6'],
                '4': ['1', '4', '5', '7'],
                '5': ['2', '4', '5', '6', '8'],
                '6': ['3', '5', '6', '9'],
                '7': ['4', '7', '8'],
                '8': ['5', '7', '8', '9', '0'],
                '9': ['6', '8', '9'],
                '0': ['8', '0']
    }
    
    iter_input = [key_dict[word] for word in observed]
    combination_list = list(itertools.product(*iter_input))
    result = [''.join(combination) for combination in combination_list]
    

    return result
if __name__=='__main__':
    print(get_pins('8'))
    print(get_pins('11'))
    print(get_pins('369'))
    