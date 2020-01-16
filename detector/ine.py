import cv2
import match
import argparse

def locate(image):
    """ Detects the bounding box of an id

    Parameters
    ----------
    image: list
        image of an id in grayscale.
    """
    match.id_border(image)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
        help = "Path to the id image")
    args = vars(ap.parse_args())
    
    image = cv2.imread(args["image"], 0)
    assert image is not None, "Path " + args["image"] + " is not a valid path"
    
    locate(image)