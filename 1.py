import re


def domain_name(url):
    pattern_1 = re.compile('://(.+?)\.')
    pattern_2 = re.compile('www\.(.+?)\.')
    if len(re.findall(pattern_2, url)) == 0:
        result = re.findall(pattern_1, url)[0]
    else:
        result = re.findall(pattern_2, url)[0]
    return result


if __name__ == '__main__':
    assert domain_name("https://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
