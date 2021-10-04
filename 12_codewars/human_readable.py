# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def make_readable(seconds):
    def change_type(NN):
        NN = str(NN)
        if len(NN) == 1:
            NN = '0'+NN
        return NN
    MM = seconds // 60
    SS = seconds % 60

    HH = MM // 60
    MM = MM % 60

    result = change_type(HH) + ":" + change_type(MM) + ":" + change_type(SS)
    
    return result


if __name__ == '__main__':
    print(make_readable(0))
    print(make_readable(5))
    print(make_readable(60))
    print(make_readable(86399))
    print(make_readable(359999))