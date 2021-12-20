import argparse
import os
from os import listdir
from os.path import isfile, join

import numpy as np
from tqdm import tqdm
import imageio


def convert_path_to_npy(*, path='train_64x64', outfile='train_64x64_mitad.npy'):
    assert isinstance(path, str), "Expected a string input for the path"
    assert os.path.exists(path), "Input path doesn't exist"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    files = sorted(files)
    print('Number of valid images is:', len(files))
    imgs = []
    for i in tqdm(range(len(files)//2)):
        img = imageio.imread(join(path, files[i]))
        img = img.astype('uint8')
        assert np.max(img) <= 255
        assert np.min(img) >= 0
        assert img.dtype == 'uint8'
        assert isinstance(img, np.ndarray)
        imgs.append(img)
    resolution_x, resolution_y = img.shape[0], img.shape[1]
    imgs = np.asarray(imgs).astype('uint8')
    assert imgs.shape[1:] == (resolution_x, resolution_y, 3)
    assert np.max(imgs) <= 255
    assert np.min(imgs) >= 0
    print('Total number of images is:', imgs.shape[0])
    print('All assertions done, dumping into npy file')
    np.save(outfile, imgs)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='convert images from directory in npz array')
    ap.add_argument('-o', '--output', type=str, default='train_64x64.npy')
    ap.add_argument('-i', '--input', type=str,
                    default='/home/crhistyan/Desktop/datasets_proyecto/imagenet64/training/images/')
    args = vars(ap.parse_args())

    out_file = args['output']
    input_dir = args['input']
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    convert_path_to_npy(path=input_dir, outfile=out_file)
