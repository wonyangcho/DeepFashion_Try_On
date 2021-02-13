import numpy as np
import cv2
from matplotlib import pyplot as plt
import argparse
import time

def main(args):

   

    print(f"source: {args.source}")
    print(f"dest: {args.target}")


    image = cv2.imread(args.source)
    mask = np.zeros(image.shape[:2], dtype="uint8")
    rect = (1, 1, mask.shape[1], mask.shape[0])
    fgModel = np.zeros((1, 65), dtype="float")
    bgModel = np.zeros((1, 65), dtype="float")
    start = time.time()
    (mask, bgModel, fgModel) = cv2.grabCut(image, mask, rect, bgModel,
                                        fgModel, iterCount=10, mode=cv2.GC_INIT_WITH_RECT)
    outputMask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD),0, 1)
    outputMask = (outputMask * 255).astype("uint8")

    cv2.imwrite(args.target, outputMask)

    fig = plt.figure()
    rows = 1
    cols = 2
    
    ax1 = fig.add_subplot(rows, cols, 1)
    ax1.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    ax1.set_title('Jumok community')
    ax1.axis("off")
    
    ax2 = fig.add_subplot(rows, cols, 2)
    ax2.imshow(cv2.cvtColor(outputMask, cv2.COLOR_BGR2RGB))
    ax2.set_title('Withered trees')
    ax2.axis("off")
    
    plt.show()


def get_arguments():
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--target', '-t', required=True, help='destination full path name')
    parser.add_argument('--source', '-s', required=True, help='source full path name')

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    args = get_arguments()
    main(args)