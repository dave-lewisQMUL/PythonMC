__author__ = 'Dave'

from random import randint
from particles import *

def get_rndm(min_,max_):
    return randint(min_,max_)

if __name__=="__main__":
    up1 = up_q(10)
    print up1
