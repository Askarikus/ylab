import re


def domain_name(url):
    pattern_1 = re.compile('://(.+?)\.')
    pattern_2 = re.compile('www\.(.+?)\.')
    if len(re.findall(pattern_2, url)) == 0:
        if url.startswith('http'):
            result = re.findall(pattern_1, url)[0]
        else:
            result = url.split('.')[0]
    else:
        result = re.findall(pattern_2, url)[0]
    return result


if __name__ == '__main__':
    print(domain_name("www.xakep.ru"))
    assert domain_name("https://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
    assert domain_name("http://github.com/carbonfive/raygun") == "github"
    assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
    assert domain_name("https://www.cnet.com") == "cnet"
    assert domain_name("https://ru.stackoverflow.com/questions/") == "ru"
    assert domain_name("icann.org") == "icann"
