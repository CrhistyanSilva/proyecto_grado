import argparse
import glob
import multiprocessing as mp
import os
import sys
from functools import partial

from PIL import Image


def get_images_filenames(dir, extensions):
    imgs_list = []
    for ext in extensions:
        imgs_list += glob.glob(os.path.join(dir, f'*.{ext}'))
    return imgs_list


def compress(encode_cmd, img_fn):
    img_name = os.path.splitext(os.path.basename(img_fn))[0]
    ext = {
        'flif': 'flif',
        'webp': 'webp',
        'jpeg': 'jls'
    }
    out_fn = os.path.join(output_dir, f'{img_name}.{ext[algorithm]}')

    if os.path.exists(out_fn):
        os.remove(out_fn)

    final_cmd = encode_cmd.format(input=img_fn, out=out_fn)
    error_code = os.system(final_cmd)
    assert error_code == 0, f'Failed to execute: \n{final_cmd}'

    img = Image.open(img_fn)
    w, h = img.size
    encoded_size = os.path.getsize(out_fn) * 8

    if delete_imgs:
        os.remove(out_fn)

    return encoded_size / (w * h * 3)


ap = argparse.ArgumentParser(description='convert images from directory in npz array')
ap.add_argument('format', help='Options: webp, flif')
ap.add_argument('directories', nargs='+', help='Directories with images to process')
ap.add_argument('-d', '--delete', help='if enable delete de output image after process them', action='store_true')
ap.add_argument('-c', '--num_cores', help='number of cors tu run in parallel', default=4, type=int)
args = vars(ap.parse_args())

algorithm = args['format']
dirs = [os.path.expanduser(dir) for dir in args['directories']]
for dir in dirs:
    assert os.path.isdir(dir), f'Directory {dir} not found'
extensions = ['jpg', 'png', 'jpeg']
extensions += [ext.upper() for ext in extensions]
delete_imgs = args['delete']
num_cors = args['num_cores']

encode_cmd = None
if algorithm == 'webp':
    encode_cmd = "cwebp -lossless '{input}' -o '{out}'"
elif algorithm == 'flif':
    encode_cmd = "flif '{input}' '{out}'"
elif algorithm == 'jpeg':
    encode_cmd = "convert -compress LosslessJPEG '{input}' '{out}'"
else:
    assert False, 'Compression format not available'

# Suppress command output
encode_cmd += ' >/dev/null 2>&1'
print(f'Algorithm: {algorithm}')

for dir in dirs:
    print(f'Processing directory {dir}')
    imgs_list = get_images_filenames(dir, extensions)
    bpd_sum = 0

    output_dir = os.path.join(dir, algorithm)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Run compression in parallel
    bpd_sum = 0
    func = partial(compress, encode_cmd)
    with mp.Pool(processes=num_cors) as pool:
        for i, res in enumerate(pool.imap_unordered(func, imgs_list, 1)):
            sys.stderr.write('\rdonde {0:%}'.format((i + 1) / len(imgs_list)))
            bpd_sum += res
    print()

    final_bpd = bpd_sum / len(imgs_list)
    print(f'Final bpd {final_bpd}')
