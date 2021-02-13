
import sys
import argparse
import os


from PIL import Image

def main(args):

    IMG_W = 192
    IMG_H = 256
    
    with Image.open(args.source) as image:
        resize_image = image.resize((IMG_W, IMG_H),Image.LANCZOS)

    resize_image.save(args.target)

def get_arguments():
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--target', '-t', required=True, help='destination full path name')
    parser.add_argument('--source', '-s', required=True, help='source full path name')

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    args = get_arguments()
    main(args)