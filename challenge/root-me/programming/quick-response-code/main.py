#!/usr/bin/python3 

from PIL import Image, ImageDraw, ImageFilter
import requests, urllib.request, urllib.parse, http.cookiejar, base64, zbarlight

zx_url = "http://zxing.org/w/decode"
rm_url = "http://challenge01.root-me.org/programmation/ch7/"
cj = http.cookiejar.CookieJar()

def get_html():
    global cj, rm_url

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    response = opener.open(rm_url)
    html = response.read().decode("utf-8")

    return html

def save_img(html):
    
    b64 = html.split("base64,")[1].split("\"")[0]
    raw = base64.b64decode(b64)
    filename = "qrcode.png"

    with open(filename, "wb") as f:
        f.write(raw)

    image = Image.open(filename)
    image = image.crop((18, 18, 282, 282))
    d = ImageDraw.Draw(image)

    for i, j in [(0, 0), (200, 0), (0, 200)]:
        d.rectangle((i + 0, j + 0, i + 63, j + 63), fill="black")
        d.rectangle((i + 9, j + 9, i + 54, j + 54), fill="white")
        d.rectangle((i + 18, j + 18, i + 45, j + 45), fill="black")

    image.save(filename)

    return filename

def qr_decode(filename):
    global zx_url

    files = {"f": open(filename, "rb")}
    response = requests.post(zx_url, files=files)

    key = response.text.split("The key is ")[1].split("</pre>")[0]
    return key

def send_flag(key):
    global cj, rm_url

    method = "POST"
    data = urllib.parse.urlencode({'metu': key}).encode("utf-8")

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    request = urllib.request.Request(rm_url, data=data)
    request.add_header("Content-Type", "application/x-www-form-urlencoded")
    request.get_method = lambda: method

    response = opener.open(request)
    html = response.read()

    print(html)

    return html
 
def main():
    html = get_html()
    filename = save_img(html)
    key = qr_decode(filename)
    print(key)
    flag = send_flag(key)
    

if __name__ == "__main__":
    main()
