#!/usr/bin/python3

import urllib, http.cookiejar, base64, numpy, hashlib, time, sys, os, string, math, random
from PIL import Image, ImageFilter

md5 = hashlib.new("md5")
def md5_get():
    global md5

    md5.update(str(time.time()).encode("utf-8"))
    return md5.hexdigest()[:8]

class Letter():

    def __init__(self):
        self.px = list()
        self.rect = None

    @staticmethod
    def create_from_px(letters_px):
        letters = []
        letters_px.sort()

        for x, y in letters_px:

            letter = Letter()
            letter.add((x, y))
            letters_px.remove((x, y))

            for w, z in letter.px:
                for i, j in numpy.ndindex((3, 9)):
                    neigh = (w - 1 + i, z - 4 + j)
                    if neigh == (w, z):
                        continue
                    if neigh in letters_px:
                       letter.add(neigh)
                       letters_px.remove(neigh)

            if letter.surface() >= 30:
                letters += [letter]

        return letters

    def add(self, px):
        if px not in self.px:
            self.px += [px]

    @staticmethod
    def create_from_image(image):
        letter = Letter()
        for x in range(image.width):
            for y in range(image.height):
                if not image.getpixel((x, y)):
                    letter.add((x, y))

        return letter

    def save(self):
        image = Image.new("P", self.get_size(), 255)
        x0, y0 = self.get_topleft()

        for x, y in self.px:
            image.putpixel((x - x0, y - y0), 0)

        image.save("output/cuts/unsorted/{}.gif".format(md5_get()))

    def magnitude(self):
        return math.sqrt(len(self.px))

    def surface(self):
        return self.get_width() * self.get_height()

    def get_rect(self):

        if self.rect != None:
            return self.rect

        self.px.sort()
        x_min = self.px[0][0]
        x_max = self.px[-1][0]

        self.px.sort(key=lambda x: x[1])
        y_min = self.px[0][1]
        y_max = self.px[-1][1]

        self.rect = (x_min, y_min, x_max - x_min + 1, y_max - y_min + 1)
        return self.rect

    def get_size(self):
        return self.get_rect()[2:]

    def get_width(self):
        return self.get_rect()[2]

    def get_height(self):
        return self.get_rect()[3]

    def get_aspect_ratio(self):
        return self.get_width() / self.get_height()

    def similar_ar(self, other):
        ratio = self.get_aspect_ratio() / other.get_aspect_ratio()
        r = 0.1

        if abs(ratio - 1) > r:
            return False

        return True

    def get_topleft(self):
        return self.get_rect()[:2]

    def __str__(self):
        return "Letter: {}".format(self.px)

    def __repr__(self):
        return self.__str__()


class Crackcha():

    main_dir = "output/captcha"
    samples_dir = "output/cuts/sorted"

    def __init__(self, file_name):
        os.rename(file_name, "{}/original.png".format(Crackcha.main_dir))
        self.cut_letters()

    @staticmethod
    def create_from_root_me(preload_samples = False):

        if preload_samples:
            sample_images, sample_letters  = Crackcha.load_samples()

        cj = http.cookiejar.CookieJar()
        url = "http://challenge01.root-me.org/programmation/ch8/"
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

        response = opener.open(url)
        html = response.read().decode("utf-8")

        img_base64 = ""
        for line in html.split(">"):
            if "img src=" in line:
                img_base64 = line.split("\"")[1].split("base64")[1][1:]
                break

        img_raw = base64.b64decode(img_base64)
        with open("output/captcha/original.png", "wb") as f:
            f.write(img_raw)

        crackcha = Crackcha("output/captcha/original.png")

        if preload_samples:
            crackcha.sample_images = sample_images
            crackcha.sample_letters = sample_letters

        return crackcha, cj

    def cut_letters(self):

        image = Image.open("{}/original.png".format(Crackcha.main_dir))
        image.convert("P")
        
        colors = list(reversed(sorted(image.getcolors())))[:3]
        background_c, text_c, noise_c  = [color[1] for color in colors]

        mask =  Image.new("P", image.size, 255)
        letters_px = list()

        for x in range(image.size[0]):
            for y in range(image.size[1]):

                diff = sum([(image.getpixel((x, y))[i] - text_c[i]) ** 2 for i in range(3)]) / 3
                if diff > 1000:
                    continue

                mask.putpixel((x, y), 0)
                letters_px += [(x, y)]

        mask.save("{}/mask.gif".format(Crackcha.main_dir))

        self.letters = Letter.create_from_px(letters_px)
        if len(self.letters) > 30:
            print("Too many letters: processing failed")
            exit()

    @staticmethod
    def load_samples():

        sample_images = {}
        sample_letters = {}

        for d in os.listdir(Crackcha.samples_dir):

            directory = Crackcha.samples_dir + "/" + d
            samples = os.listdir(directory)
            random.shuffle(samples)

            d_sample_images = []
            d_sample_letters = []

            if len(samples) > 10:
                samples = samples[:10]
            
            for sample in samples:
                d_sample_image = Image.open(directory + "/" + sample)
                d_sample_images += [d_sample_image]
                d_sample_letters += [Letter.create_from_image(d_sample_image)]

            sample_images[d] = d_sample_images
            sample_letters[d] = d_sample_letters


        return sample_images, sample_letters

    def train(self):
        [letter.save() for letter in self.letters]
        
    def crack(self, cj):
        directories = os.listdir(Crackcha.samples_dir)

        for letter in self.letters:

            matches = list()
            for d in directories:
                matches += [(self.match(letter, d), d)]

            matches.sort()
            letter.match = matches[-1][1]
            
        self.solution = "".join([letter.match for letter in self.letters])
        print(self.solution)

        self.respond_root_me(cj)

    def match(self, letter, directory):
        means = []

        for sample_letter in self.sample_letters[directory]:

            delta_x = sample_letter.get_width() - letter.get_width()
            delta_y = sample_letter.get_height() - letter.get_height()
            translate_x = delta_x // 2 - letter.get_topleft()[0]
            translate_y = delta_y // 2 - letter.get_topleft()[1]

            mean = 0

            for x, y in letter.px:
                if (x + translate_x, y + translate_y) in sample_letter.px:
                    mean += 1

            mean /= letter.magnitude() * sample_letter.magnitude()
            means += [mean]

        if len(means) == 0:
            return 0

        mean = sum(means) / len(means)

        return mean

    def respond_root_me(self, cj):
        url = "http://challenge01.root-me.org/programmation/ch8/"
        method = "POST"
        data = urllib.parse.urlencode({"cametu": self.solution}).encode("utf-8")
        print(data)

        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        request = urllib.request.Request(url, data = data)
        request.add_header("Content-Type","application/x-www-form-urlencoded")
        request.get_method = lambda: method

        response = opener.open(request)
        html = response.read().decode("utf-8")

        para = html.split("<p>")[1].split("</p>")[0]
        print(para)
        if not "retente" in html:
            print(html)


def main():

    if len(sys.argv) < 2 or sys.argv[1] == "train":
        crackcha, cj = Crackcha.create_from_root_me()
        crackcha.train()

    elif sys.argv[1] == "crack":

        crackcha, cj = Crackcha.create_from_root_me(preload_samples = True)
        crackcha.crack(cj)



if __name__ == "__main__":
    main()
