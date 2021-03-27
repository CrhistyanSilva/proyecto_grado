
import argparse
import os
import glob
import cv2
import numpy as np

ap = argparse.ArgumentParser(description='convert images from directory in npz array')
ap.add_argument('npz_filename', help='Npz filename')
ap.add_argument('extension', help='Images exntesion')
args = vars(ap.parse_args())

filename = args['npz_filename']
ext = args['extension']

images = np.load(filename)['arr_0']

for i in range(images.shape[0]):
    image = images[i, :, :, :]
    cv2.imwrite(f'image_{i}.{ext}', image)

# np.savez("all_images.npz", array_of_images)

