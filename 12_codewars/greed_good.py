# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python

def score(dice):
    dice_dict = {}
    for roll in dice:
        if roll not in dice_dict:
            dice_dict[roll] = 1
        else:
            dice_dict[roll] += 1

    #calculating
    total_score = 0
    for key, value in zip(dice_dict.keys(), dice_dict.values()):
        if value >= 3 and (key >= 2 and key <=6) and key != 5:
            total_score += (key * 100)
        elif value >= 3 and key == 1:
            total_score += 1000 + (value%3)*100
        elif value >=3 and key == 5:
            total_score += 500 + (value%3)*50
        elif key == 1:
            total_score += 100 * value
        elif key == 5:
            total_score += 50 * value
    return total_score
        


if __name__=='__main__':
    print(score([2, 3, 4, 6, 2]))
    print(score([4, 4, 4, 3, 3]))
    print(score([2, 4, 4, 5, 4]))