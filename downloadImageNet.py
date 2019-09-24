

import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    suit_images_link ='http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03885669'
   
    suit_image_urls = urllib.request.urlopen(suit_images_link).read().decode()
    pic_num = 1
    
    if not os.path.exists('suit'):
        os.makedirs('suit')
        
    for i in suit_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "suit/"+str(pic_num)+".jpg")
            img = cv2.imread("suit/"+str(pic_num)+".jpg")
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (900, 900))
            cv2.imwrite("suit/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))  
store_raw_images()

