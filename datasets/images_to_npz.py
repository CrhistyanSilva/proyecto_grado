import argparse
import os
import glob
import cv2
import numpy as np

ap = argparse.ArgumentParser(description='convert images from directory in npz array')
ap.add_argument('image_folder', help='Images directory')
ap.add_argument('extension', help='Images exntesion')
args = vars(ap.parse_args())

image_folder = args['image_folder']
ext = args['extension']

array_of_images = []
image_files = glob.glob(os.path.join(image_folder, 'image_376*.' + ext))

for filename in image_files:
    print(f'Processing {filename}')
    img = cv2.imread(filename)
    # img = img.astype('float32')
    # img /= 255

    array_of_images.append(img)
    
all_images = np.array(array_of_images)
print(all_images.shape)    
np.savez("imgnet_32x32.npz", trainx=all_images, testx=all_images)


