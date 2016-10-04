#!/usr/bin/python3 

from PIL import Image
import sys, os, shutil, numpy

def bin2int(l):
    s = len(l)
    v = 0
    for i in range(s):
        v += l[i] * 2 ** (s - i - 1)

    return v


class QR():

    def __init__(self, filename):

        if not "qr" in os.listdir("."):
            os.mkdir("qr")

        self.files = {"input": "qr/run/input.png"}
        shutil.copyfile(filename, self.files["input"])

        self.patterns = {"finder": "qr/pattern/finder.gif",
            0: "qr/pattern/0.gif",
            1: "qr/pattern/1.gif",
            2: "qr/pattern/2.gif",
            3: "qr/pattern/3.gif",
            4: "qr/pattern/4.gif",
            5: "qr/pattern/5.gif",
            6: "qr/pattern/6.gif",
            7: "qr/pattern/7.gif"}

    def width(self):

        if hasattr(self, '_width'):
            return self._width

        self._width = self.scanned().width
        self._version = (self._width - 17) // 4

        return self._width

    def version(self):

        if hasattr(self, '_version'):
            return self._version

        self.width()

        return self._version

    def decode(self):
        print(self.validate_finders())
        print(self.validate_timing())
        print(self.error_correction_level())
        print(self.unmasked())

    def validate_finders(self):

        scanned = self.scanned()

        width = self.width()
        corner_shift = width - 7
        corners = ((0, 0), (corner_shift, 0), (0, corner_shift))

        finder = Image.open(self.patterns["finder"]).convert("1")

        for i, j in corners:
            for x in range(7):
                for y in range(7):
                    if finder.getpixel((x, y)) != scanned.getpixel((x + i, y + j)) * 255:
                        return False

        return True

    def validate_timing(self):
        
        scanned = self.scanned()
        w = self.width()

        i, j = 8, 6
        y = j
        for x in range(i, w - 8):
            if scanned.getpixel((x, y)) != x % 2:
                return False

        i, j = 6, 8
        x = i
        for y in range(j, w - 8):
            if scanned.getpixel((x, y)) != y % 2:
                return False

        return True

    def error_correction_level(self):
        
        scanned = self.scanned()
        w = self.width()

        first = (scanned.getpixel((0, 8)), scanned.getpixel((1, 8)))
        second = (scanned.getpixel((8, w - 1)), scanned.getpixel((8, w - 2)))

        if first != second:
            return False

        levels = ["L", "M", "Q", "H"]
        level = levels[bin2int(first)]

        return level

    def data_mask(self):
        pass


    def unmasked(self):
        scanned = self.scanned()
        mask = self.mask()


    def mask(self):

        if hasattr(self, '_mask'):
            return self._mask

        scanned = self.scanned()
        w = self.width()

        first = [scanned.getpixel((2, 8)), scanned.getpixel((3, 8)), scanned.getpixel((4, 8))]
        second = [scanned.getpixel((8, w - 3)), scanned.getpixel((8, w - 4)), scanned.getpixel((8, w - 5))]

        if first != second:
            return False
       
        first[0] = 1 - first[0]
        first[2] = 1 - first[2]

        mask = bin2int(first)

        self._mask = Image.open(self.patterns[mask])
        return self._mask

    def scanned(self):

        if hasattr(self, '_scanned'):
            return self._scanned

        image = Image.open(self.files["input"])
        image = image.convert("1")

        x = 0
        while not image.getpixel((x, 0)):
            x += 1

        pixel_width = x / 7
        new_width = round(7 * image.width / x)
        new_size = (new_width, new_width)
        new_image = Image.new("1", new_size)

        for i in range(new_width):
            x = round(pixel_width / 2 + i * pixel_width)

            for j in range(new_width):
                y = round(pixel_width / 2 + j * pixel_width)

                if image.getpixel((x, y)):
                    new_image.putpixel((i, j), 1)
        
        self.files["scanned"] = "qr/run/scanned.gif"
        new_image.save(self.files["scanned"])

        self._scanned = new_image

        return new_image



def main(argv):

    execname = argv[0]
    
    if len(argv) < 2:
        print("Usage: {} <file>".format(execname))
        exit()

    filename = argv[1]

    qr = QR(filename)
    qr.decode()


if __name__ == "__main__":
    main(sys.argv)
