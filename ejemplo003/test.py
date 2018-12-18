import pytesseract
import sys
import argparse

try:
    import Image
except ImportError:
    from PIL import Image
from subprocess import check_output


def resolve(path):
	print("Resolviendo la Imagen")
	check_output(['convert', path, '-resample', '600', path])
	return pytesseract.image_to_string(Image.open(path))

if __name__=="__main__":
	argparser = argparse.ArgumentParser ()
	argparser.add_argument('path',help = 'Captcha file path')
	args = argparser.parse_args()
	path = args.path
        print('Resolviendo el Captcha')
	captcha_text = resolve(path)
        print('Extracted Text : '+captcha_text)
