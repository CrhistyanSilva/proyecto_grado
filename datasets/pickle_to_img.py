import argparse
import os
import pickle

import cv2
import lasagne
import numpy as np
import tqdm


# Note that this will work with Python3
def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo)
    return dict


def load_databatch(data_folder, idx, img_size=64):
    data_file = os.path.join(data_folder, 'train_data_batch_')

    d = unpickle(data_file + str(idx))
    x = d['data']
    y = d['labels']
    mean_image = d['mean']

    # Labels are indexed from 1, shift it so that indexes start at 0
    y = [i - 1 for i in y]
    data_size = x.shape[0]

    img_size2 = img_size * img_size

    x = np.dstack((x[:, :img_size2], x[:, img_size2:2 * img_size2], x[:, 2 * img_size2:]))
    x = x.reshape((x.shape[0], img_size, img_size, 3))

    X_train = np.array(x[0:data_size, :, :, :])
    Y_train = np.array(y[0:data_size])

    return dict(
        X_train=lasagne.utils.floatX(X_train),
        Y_train=Y_train.astype('int32'),
        mean=mean_image)


ap = argparse.ArgumentParser(description='convert images from directory in npz array')
ap.add_argument('-o', '--output', type=str,
                default='/home/crhistyan/Desktop/datasets_proyecto/imagenet64/training/images/')
ap.add_argument('-i', '--input_dir', type=str,
                default='/home/crhistyan/Desktop/datasets_proyecto/imagenet64/training/pickles')
ap.add_argument('-s', '--img_size', type=int, default=64)
args = vars(ap.parse_args())

input_dir = args['input_dir']
out_dir = args['output']
img_size = args['img_size']

assert os.path.exists(input_dir)
os.makedirs(out_dir, exist_ok=True)

for i in range(1, 11):
    print(f'Processing: file {i}')

    samples = load_databatch(input_dir, i, img_size=img_size)['X_train']

    num_samples = samples.shape[0]
    print(f'Number of samples {num_samples}')
    for j in tqdm.tqdm(range(num_samples)):
        img = samples[j, :, :, :]

        red = img[:, :, 2].copy()
        blue = img[:, :, 0].copy()

        img[:, :, 0] = red
        img[:, :, 2] = blue

        out_fn = os.path.join(out_dir, f"image_{'{:02}'.format(i)}_{'{:09}'.format(j)}.png")
        cv2.imwrite(out_fn, img)
    print('finish')
