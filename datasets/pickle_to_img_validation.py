import os
import numpy as np
import pickle
import lasagne
import cv2
import tqdm
import argparse

# Note that this will work with Python3
def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo)
    return dict


def load_databatch(data_file, img_size=64):

    d = unpickle(data_file)
    x = d['data']
    y = d['labels']

    # Labels are indexed from 1, shift it so that indexes start at 0
    y = [i-1 for i in y]
    data_size = x.shape[0]

    img_size2 = img_size * img_size

    x = np.dstack((x[:, :img_size2], x[:, img_size2:2*img_size2], x[:, 2*img_size2:]))
    x = x.reshape((x.shape[0], img_size, img_size, 3))

    # create mirrored images
    X_train = x[0:data_size, :, :, :]
    Y_train = y[0:data_size]
    X_train_flip = X_train[:, :, :, ::-1]
    Y_train_flip = Y_train
    X_train = np.concatenate((X_train, X_train_flip), axis=0)
    Y_train = np.concatenate((Y_train, Y_train_flip), axis=0)

    return dict(
        X_train=lasagne.utils.floatX(X_train),
        Y_train=Y_train.astype('int32')
        )

ap = argparse.ArgumentParser(description='Extract images from pickle filename')
ap.add_argument('pickle_filename', help='Pickle filename to extract the images')
ap.add_argument('--size', default=32, help='Images size assuming square images')
args = vars(ap.parse_args())

pickle_fn = args['pickle_filename']
img_size = args['size']

assert os.path.isfile(pickle_fn), 'Pickle filename not found'

print(f'Processing pickle file')
output_dir = os.path.dirname(pickle_fn)
samples = load_databatch(pickle_fn)['X_train']

print(f'Writing images in {output_dir}')
for j in tqdm.tqdm(range(samples.shape[0])):
    img = samples[j, :, :, :]

    red = img[:,:,2].copy()
    blue = img[:,:,0].copy()

    img[:,:,0] = red
    img[:,:,2] = blue

    output_fn = os.path.join(output_dir, f"image_{'{:06}'.format(j)}.png")
    cv2.imwrite(output_fn, img)
print('finish')

