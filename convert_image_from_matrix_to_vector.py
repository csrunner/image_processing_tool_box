# -*- coding:utf-8 -*-
__author__ = 'shichao'

import cv2
import numpy as np

def two_dim2one_dim(img):
    [dimx,dimy,dimc] = img.shape
    vec = np.zeros((dimc*dimx*dimy,1))
    counter = 0
    for i in range(dimx):
        for j in range(dimy):
            vec[counter] = img[i,j,0]
            vec[counter+1] = img[i,j,1]
            vec[counter+2] = img[i,j,2]
            counter += 1
    return vec

def one_dim2two_dim(vec,dimx,dimy):
    img = np.zeros((dimx,dimy,3))
    counter = 0
    for i in range(dimx):
        for j in range(dimy):
            img[i,j,0] = vec[counter+0]
            img[i,j,1] = vec[counter+1]
            img[i,j,2] = vec[counter+2]
            counter += 1
    return img

def main():
    path = '/Users/shichao/Downloads/1.jpg'
    img = cv2.imread(path)
    print(type(img))
    dimx,dimy,_ = img.shape
    vec = two_dim2one_dim(img)
    converted_img = one_dim2two_dim(vec,dimx,dimy)
    print(type(converted_img))
    cv2.imwrite('/Users/shichao/Downloads/convert_1.jpg',converted_img)

if __name__ == '__main__':
    main()
