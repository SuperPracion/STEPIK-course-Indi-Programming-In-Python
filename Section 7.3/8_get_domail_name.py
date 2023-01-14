import re


def get_domain_name(url):
    return re.findall("(https|http|www)(:|\.)(//)?(www)?\.?([a-zA-Z-]*)", url)[-1][-1]

print(get_domain_name("http://google.com"))
print(get_domain_name("http://google.co.jp"))
print(get_domain_name("www.xakep.ru"))
print(get_domain_name("https://youtube.com"))
print(get_domain_name("http://www.lenovo.com"))
print(get_domain_name("http://www.zombie-bites.com"))
