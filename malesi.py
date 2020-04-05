#!/usr/bin/python3
import cv2
import numpy as np
import alpha
import os
import sys
import random

def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)

def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation) for im in im_list]

    return cv2.hconcat(im_list_resize)

def main(filename):
    img_alpha = alpha.init_img()
    img_readline = []
    img_mergerline = []

    cfile = open(filename, 'r')
    maxl_text = 0
    text_tmp = []
    for tline in cfile:
        if len(tline[:-1]) > maxl_text:
            maxl_text = len(tline[:-1])
        text_tmp.append(tline)
    cfile.close()
    file = open(filename, 'r')

    print("[*] Converting to handwriting..")
    temp = []
    fcount = 0
    rand_num = ''

    for text in file:
        img_readline.clear()
        text = text[:-1]

        # Combine all character to a sentence
        img_readline.append(cv2.imread( img_alpha['32' + str(2)] ))
        for x in range(len(text)):
            while True:
                for cycle in range(0,5):
                    for rand in range(0,3):
                        rand_num = str(ord(text[x])) + str(random.randint(0,5))
                temp = img_alpha[rand_num]
                if os.path.isfile(temp):
                    img_readline.append( cv2.imread(temp) )
                    break
                else:
                    fcount += 1

        if len(text) < maxl_text:
            if (maxl_text - len(text)) > 2:
                for i in range(round((maxl_text - len(text))/1.6)):
                    #img_readline.append(cv2.imread( img_alpha['32' + str(random.randint(0,2))] ))
                    img_readline.append(cv2.imread( img_alpha['32' + str(2)] ))
            else:
                for i in range(maxl_text - len(text)):
                    #img_readline.append(cv2.imread( img_alpha['32' + str(random.randint(0,2))] ))
                    img_readline.append(cv2.imread( img_alpha['32' + str(2)] ))

        # Combine the sentence to the paragraph
        temp = img_readline.copy()
        img_mergerline.append(temp)

    print("[+] Done!")
    print('[*] Trial error total', fcount)
    file.close()

    print("[*] Resize to A4 paper\n")
    img_horizontal = []

    for x in range(len(img_mergerline)):
        print("[*] Processing", text_tmp[x], end="")
        im_h = hconcat_resize_min(img_mergerline[x])
        #im_h = np.hstack(img_mergerline[x])
        img_horizontal.append(im_h)
        im_v = vconcat_resize_min(img_horizontal)

    #im_paper[0:im_text.shape[0], 0:im_text.shape[1]] = im_text
    print("\n[+] Done..")

    cv2.imwrite('output/output.jpg', im_v)
    print("[+] output successfully writen")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify the file name location!")
        sys.exit(1)

    main(sys.argv[1])
