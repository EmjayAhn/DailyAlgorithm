# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
import math

def isvalid(s):
    char_dict = {}
    count_dict = {}
    for character in s:
        try:
            char_dict[character] += 1
        except:
            char_dict[character] = 1
    for item in char_dict.items():
        try:
            count_dict[item[1]] += 1
        except:
            count_dict[item[1]] = 1
    if len(count_dict) == 1:
        return 'YES'
    else:
        sorted_count = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
        if (sorted_count[-1][1] == 1):
            return 'YES'
    return 'NO'
# test code
test_case = ['ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd', 'aabbc', 'a', 'aabbcd', 'aabbccddeefghi', 'abcdefghhgfedecba']
test_result = ['YES', 'YES','YES', 'NO', 'NO', 'YES']
for index, case in enumerate(test_case):
    # print(isvalid(case))
    print(isvalid(case)==test_result[index])
    print(test_result[index])
