#!/usr/bin/python3
def init_img():
    img_alpha = {'000':'dummy'}

    # load dataset of uppercase
    for x in range(65, 91, 1):
        for y in range(0, 6, 1):
            img_alpha[str(x) + str(y)] = ('dataset/' + str(x)+ str(y) + '.png')

    #load dataset of lowercase
    for x in range(97, 123, 1):
        for y in range(0, 6, 1):
            img_alpha[str(x) + str(y)] = ('dataset/' + str(x)+ str(y) + '.png')

    #load dataset for number
    for x in range(48, 58, 1):
        for y in range(0, 6, 1):
            img_alpha[str(x) + str(y)] = ('dataset/' + str(x)+ str(y) + '.png')

    #load dataset for symbol
    for x in range(30, 48, 1):
        for y in range(0, 6, 1):
            img_alpha[str(x) + str(y)] = ('dataset/' + str(x)+ str(y) + '.png')

    print("[+] Initialize dataset done..")
    return img_alpha
