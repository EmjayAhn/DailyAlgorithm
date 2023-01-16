# https://school.programmers.co.kr/learn/courses/30/lessons/120838
# programmers, 코딩테스트 입문

def solution(letter):
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
        }

    letter_morse = letter.split(' ')
    answer = ''.join(list(map(lambda item: morse[item], letter_morse)))

    return answer

if __name__=="__main__":
    test_set = [
        ".... . .-.. .-.. ---",
        ".--. -.-- - .... --- -."
    ]
    for test in test_set:
        print(solution(test))