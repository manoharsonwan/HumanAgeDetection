# Copyright (c) 2019 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

import os
import edcc
import urllib.request
import numpy as np
import cv2
import urllib.parse
from PIL import Image
import requests
from io import BytesIO
import random
 ##############################
 # for git hub update 
 ###########################
 
file_path = "/home/qwickbit/Documents/Palm_API/EDCC-Palmprint-Recognition/palmprint_data"
#upload_img = os.path.join(file_path, "a_01.bmp")
#TEST_A_02_PALMPRINT_IMAGE = os.path.join(TEST_PALMPRINT_DATA_DIR, "a_02.bmp")
stored_img = os.path.join(file_path, "palm_img_IMG_1100.jpg")
#TEST_B_02_PALMPRINT_IMAGE = os.path.join(TEST_PALMPRINT_DATA_DIR, "b_02.bmp")


def downloader(pathe = None):
    file_name = random.randrange(1,10000)
    file_dir = "/home/qwickbit/Documents/Palm_API/url_downloader/"
    full_file_name = file_dir  + str(file_name) + '.jpg'
    urllib.request.urlretrieve(pathe,full_file_name)
    return full_file_name
  



# def url_to_img(pathe =None):
#     resp = urllib.request.urlopen(pathe)
#     image = np.asarray(bytearray(resp.read()), dtype="uint8")
#     image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#     print("image", image)
#     return image
def palm_recogniser(pathe = None):
    print(pathe)
    upload_img = downloader(pathe)
    
    print("upload_img", upload_img)
# if __name__ == "__main__":
    config = edcc.EncoderConfig(29, 5, 5, 10)
    encoder = edcc.create_encoder(config)
    one_palmprint_code = encoder.encode_using_file(upload_img)
    another_palmprint_code = encoder.encode_using_file(stored_img)
    similarity_score = one_palmprint_code.compare_to(another_palmprint_code)
    #print("similarity_score:", similarity_score)
    print(
        "{} <-> {} similarity score:{}".format(
            upload_img, stored_img, similarity_score
        )
    )
    return similarity_score
#palm_recogniser(pathe)    





#########################################\
#localhot IP:- http://10.0.0.185:8081/api/Hello
###########################################