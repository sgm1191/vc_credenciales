import numpy as np
import cv2
from matplotlib import pyplot as plt
import argparse
import imutils

def template_in(image, template):
    """Finds the bounding box of a template in an image
    
    Parameters
    ----------
        image : list 
            image in grayscale, i.e. 2-D list
        template : str
            path of the image which is going to be used as a template
    """
    
    img_escudo = cv2.imread(template, 0)
    assert img_escudo is not None, "Template image path of escudo nacional is not valid"
    w, h = img_escudo.shape[::-1]

    res = cv2.matchTemplate(image, img_escudo, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(image,top_left, bottom_right, 255, 2)

    cv2.imshow("Outline", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def escudo_in(image):
    """Finds the bounding box of the escudo nacional in an image
    
    Parameters
    ----------
        image : list 
            image in grayscale, i.e. 2-D list
    """    
    template_in(image, "templates/escudo_aguila.PNG")

def stripe_in(image):
    """Finds the bounding box of the stripe in an image
    
    Parameters
    ----------
        image : list 
            image in grayscale, i.e. 2-D list
    """    
    template_in(image, "templates/franja_anaranjada.PNG")

def mexico_map_in(image):
    """Finds the bounding box of the escudo nacional in an image
    
    Parameters
    ----------
        image : list 
            image in grayscale, i.e. 2-D list
    """    
    template_in(image, "templates/mapa_republica_mexicana.PNG")

def id_border(image):
    gray = cv2.GaussianBlur(image, (3, 3), 0)
    ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    
    conts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    conts = imutils.grab_contours(conts)
    conts = sorted(conts, key=cv2.contourArea, reverse=True)[:5]

    max_perim = 0
    max_perim_app = None
    for c in conts:
        perim = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02*perim, True)

        if perim > max_perim:
            max_perim = perim
            max_perim_app = approx

        #if len(approx) == 4:
        #    screenCnt = approx
            #contours.append(approx)
        #    break
    cv2.drawContours(image, [max_perim_app], -1, (255,0,0), 2)
    cv2.imshow("Outline", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
        help = "Path to the image to query the template")
    ap.add_argument("-t", "--template", required=True,
        help = "Path of the image template")
    args = vars(ap.parse_args())
    
    image = cv2.imread(args["image"], 0)
    assert image is not None, "Path " + args["image"] + " is not a valid path"
    
    template_in(image, args["template"])
