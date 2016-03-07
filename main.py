#!/usr/bin/python
# coding=UTF-8
from PIL import Image

import sys

def print_usage():
    print 'Usage: python main.py (file name) [optional: step size]'

def get_character(R,G,B):
	luminosity = (0.2126*R + 0.7152*G + 0.0722*B)
	if luminosity > 200:
                return ' '
        if luminosity > 175:
		return '░'
	elif luminosity > 150:
		return '▒'
	elif luminosity > 100:
		return '▓'
	elif luminosity > 50:
		return '▓'
	elif luminosity >= 0:
		return '█'

def get_rgb_of_pixel(pixels,i, j):
    r,g,b = pixels[i][j]
    return (r,g,b)


def main():
    arguments = sys.argv
    if len(arguments) > 3:
        print_usage()
        return

    step_length = 10
    if len(arguments) == 3:
        step_length = int(arguments[2])

    image_file_name = arguments[1]
    im = Image.open(image_file_name).convert("RGB")
    pixels = list(im.getdata())
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
    with open("someText.txt","w") as f:
            for i in xrange(0, height, step_length):
                    for j in xrange(0, width, step_length):
                            print "i: {}\nj: {}\n\n".format(i,j)
                            r,g,b = get_rgb_of_pixel(pixels,i,j)
                            f.write(get_character(r,g,b))
                    f.write('\n')

if __name__ == '__main__':
    main()
