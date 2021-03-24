import os
import numpy as np
import pickle
import lasagne
import cv2

# Note that this will work with Python3
def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo)
    return dict


def load_databatch(data_folder, idx, img_size=32):
    data_file = os.path.join(data_folder, 'train_data_batch_')

    d = unpickle(data_file + str(idx))
    x = d['data']
    y = d['labels']
    mean_image = d['mean']

    # x = x/np.float32(255)
    # mean_image = mean_image/np.float32(255)

    # Labels are indexed from 1, shift it so that indexes start at 0
    y = [i-1 for i in y]
    data_size = x.shape[0]

    # x -= mean_image

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
        Y_train=Y_train.astype('int32'),
        mean=mean_image)

for i in range(1, 11):
    print(f'Processing: file {i}')
    samples = load_databatch('./', i)['X_train']

    num_samples = samples.shape[0]
    print(f'Number of samples {num_samples}'
    for j in range(num_samples):
        img = samples[j, :, :, :]

        red = img[:,:,2].copy()
        blue = img[:,:,0].copy()

        img[:,:,0] = red
        img[:,:,2] = blue

        cv2.imwrite(f"image_{i}_{'{:06}'.format(j)}.png", img)
    print('finish')

