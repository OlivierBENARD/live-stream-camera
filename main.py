import cv2 # computer vision lib
import numpy as np
import click # command line interface
from time import sleep
from functions import *

def dev():

    c = cv2.VideoCapture(0)
    _, img = c.read()

    # operations on the img (np.matrix)
    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 1) # remove RGB vector and only consider 0 to 255 values
    img = reduce_gray_scale(img, 16)
    cv2.imshow('e2',img) # must be launch from Windows PowerShell to detect the device
    convert_to_char(img)

    while True:
        if cv2.waitKey(100)==27:
            break
            
    cv2.destroyAllWindows()

def prod():

    c = cv2.VideoCapture(0)

    while True:
        _, img = c.read()
        img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 1)
        img = reduce_gray_scale(img, 16)
        cv2.imshow('e2',img) # must be launch from Windows PowerShell to detect the device
        convert_to_char(img)

        if cv2.waitKey(100)==27: # if 'echap' is hit
            break

    cv2.destroyAllWindows()

class Config(object):

    run = None

    def __init__(self, config='dev'):
        if config == 'prod':
            self.run = prod()
        else:
            self.run = dev()

@click.command()
@click.option('--mode', default='dev', type=click.Choice(['dev', 'prod'], case_sensitive=False), required=True, show_default=True, help='select mode')
def main(mode):
    Config(mode).run

if __name__ == '__main__':
    main()
