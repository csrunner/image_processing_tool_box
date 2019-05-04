# -*- coding:utf-8 -*-
__author__ = 'shichao'
import numpy as np
import cv2

def crop_image(img):
    row = 3
    col = 3

    [dimx, dimy, dimc] = img.shape
    cropped_img = img[:dimx / row, :dimy / col, :]

    return cropped_img


def crop_merge_image(img_seq):
    '''
    crop_image crop the raw image in the sequence frame by frame and gather the 4 corners into a new one
    :param img_seq:
    :return:
    '''
    row = 3
    col = 3
    METHOD1 = False
    METHOD2 = True



    if len(img_seq.shape)==4:
        [dimx,dimy,dimc,dimt] = img_seq.shape
        print(img_seq.shape)
        cropped_img = np.zeros([2*dimx/row,2*dimy/col,dimc,dimt])
        for i in range(dimt):
            if METHOD1:
                cropped_img[:dimx/row,:dimy/col,:,i] = img_seq[:dimx/row,:dimy/col,:,i]
                cropped_img[:dimx/row,(2*dimy/col-dimy/col):,:,i] = img_seq[:dimx/row,(dimy-dimy/col):,:,i]
                cropped_img[(2*dimx/row-dimx/row):,:dimy/col,:,i] = img_seq[(dimx-dimx/row):,:dimy/col,:,i]
                cropped_img[(2*dimx/row-dimx/row):,(2*dimy/col-dimy/col):,:,i] = img_seq[(dimx-dimx/row):,(dimy-dimy/col):,:,i]
            if METHOD2:
                cropped_img[:dimx/row,:dimy/col,:,i]  = img_seq[:dimx/row,:dimy/col,:,i]
                cropped_img[:dimx/row,:-dimy/col,:,i] = img_seq[:dimx/row,:-dimy/col,:,i]
                cropped_img[:-dimx/row,:dimy/col,:,i] = img_seq[:-dimx/row,:dimy/col,:,i]
                cropped_img[:-dimx/row,:-dimy/col,:,i] = img_seq[:-dimx/row,:-dimy/col,:,i]
        return cropped_img

    elif len(img_seq.shape)==3:
        [dimx,dimy,dimt] = img_seq.shape
        print(img_seq.shape)
        cropped_img = np.zeros([2*dimx/row,2*dimy/col,dimt])
        for i in range(dimt):
            if METHOD1:
                cropped_img[:dimx/row,:dimy/col,i] = img_seq[:dimx/row,:dimy/col,i]
                cropped_img[:dimx/row,(2*dimy/col-dimy/col):,i] = img_seq[:dimx/row,(dimy-dimy/col):,i]
                cropped_img[(2*dimx/row-dimx/row):,:dimy/col,i] = img_seq[(dimx-dimx/row):,:dimy/col,i]
                cropped_img[(2*dimx/row-dimx/row):,(2*dimy/col-dimy/col):,i] = img_seq[(dimx-dimx/row):,(dimy-dimy/col):,i]
            if METHOD2:
                cropped_img[:dimx/row,:dimy/col,i]  = img_seq[:dimx/row,:dimy/col,i]
                cropped_img[:dimx/row,-dimy/col:,i] = img_seq[:dimx/row,-dimy/col:,i]
                cropped_img[-dimx/row:,:dimy/col,i] = img_seq[-dimx/row:,:dimy/col,i]
                cropped_img[-dimx/row:,-dimy/col:,i] = img_seq[-dimx/row:,-dimy/col:,i]
        return cropped_img
    
    
def main():
    path = '/Users/shichao/Downloads/1.jpg'
    img = cv2.imread(path)
    cropped_img = crop_image(img)
    cv2.imwrite('/Users/shichao/Downloads/1_cropped.jpg',cropped_img)

if __name__ == "__main__":
    main()
