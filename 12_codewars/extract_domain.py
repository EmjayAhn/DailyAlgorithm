# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
import re
def domain_name(url):
    # eliminate = ://
    pattern = re.compile('https?://')
    if pattern.search(url):
        p_match = pattern.search(url)
        url = url.replace(url[p_match.span()[0]:p_match.span()[1]], '')
    # eliminate = www
    pattern = re.compile('www')
    if pattern.search(url):
        p_match = pattern.search(url)
        url = url.replace(url[p_match.span()[0]: p_match.span()[1]+1], '')
        
    # eliminate = .com, .co
    pattern = re.compile('\.')
    if pattern.search(url):
        p_match = pattern.search(url)
        url = url.replace(url[p_match.span()[0]:], '')

    return url
if __name__=='__main__':
    print(domain_name("http://google.com"))
    print(domain_name("http://google.co.jp"))
    print(domain_name("www.xakep.ru"))
    print(domain_name("https://youtube.com"))
    print(domain_name("http://github.com/carbonfive/raygun"))
    print(domain_name("codewars.com"))
    print(domain_name("www.codewars.com/kata"))