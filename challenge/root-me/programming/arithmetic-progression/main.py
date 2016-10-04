#!/usr/bin/python3 

import urllib.request, http.cookiejar

cj = None

def get_html():
    global cj

    cj = http.cookiejar.CookieJar()
    url = "http://challenge01.root-me.org/programmation/ch1/"
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    response = opener.open(url)
    html = response.read().decode("utf-8")

    return html

def extract_parameters(html):
    
    inc = int(html.split("[")[1].split(" ")[1])

    n_mul_sign = html.split("[")[1].split(" ")[5]
    n_mul_int = int(html.split("[")[2].split(" ")[3])
    
    n_mul = n_mul_int
    if n_mul_sign == "-":
        n_mul *= -1

    n0 = int(html.split("<sub>0</sub>")[1].split("<br />")[0].split(" ")[2])
    
    n_max = int(html.split("<sub>")[4].split("</sub>")[0])

    return n0, inc, n_mul, n_max

def arithmetic_progression(n0, inc, n_mul, n_max):

    n = 0
    ncurrent = n0

    while n < n_max:
        if n < 10:
            print(ncurrent)
        nplus = inc + ncurrent + n_mul * n
        n += 1
        ncurrent = nplus

    print(n, ncurrent)
    return ncurrent

def put_html(result):
    global cj

    url = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result={}".format(result)

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    request = urllib.request.Request(url)
    response = opener.open(request)
    html = response.read().decode("utf-8")

    return html

html = get_html()
print(html)
n0, inc, n_mul, n_max = extract_parameters(html)
print(n0, inc, n_mul, n_max)
result = arithmetic_progression(n0, inc, n_mul, n_max)
print(result)
response = put_html(result)
print(response)
