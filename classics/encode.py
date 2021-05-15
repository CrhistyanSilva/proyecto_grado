import argparse
import glob
import os

from PIL import Image
from tqdm import tqdm


def get_images_filenames(dir, extensions):
    imgs_list = []
    for ext in extensions:
        imgs_list += glob.glob(os.path.join(dir, f'*.{ext}'))
    return imgs_list


ap = argparse.ArgumentParser(description='convert images from directory in npz array')
ap.add_argument('format', help='Options: webp, flif')
ap.add_argument('directories', nargs='+', help='Directories with images to process')
ap.add_argument('-d', '--delete', help='if enable delete de output image after process them', action='store_true')
args = vars(ap.parse_args())

algorithm = args['format']
dirs = [os.path.expanduser(dir) for dir in args['directories']]
extensions = ['jpg', 'png', 'jpeg']
extensions += [ext.upper for ext in extensions]
delete_imgs = args['delete']

encode_cmd = None
if algorithm == 'webp':
    encode_cmd = 'cwebp -lossless {input} -o {out}'
elif algorithm == 'flif':
    encode_cmd = 'flif {input} {out}'
else:
    assert False, 'Compression format not available'

for dir in dirs:
    print(f'Processing directory {dir}')
    imgs_list = get_images_filenames(dir, extensions)
    bpd_sum = 0

    output_dir = os.path.join(dir, algorithm)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for img_fn in tqdm(imgs_list):
        img_name = os.path.splitext(os.path.basename(img_fn))[0]
        out_fn = os.path.join(output_dir, f'{img_name}.{algorithm}')
        final_cmd = encode_cmd.format(input=img_fn, out=out_fn)
        error_code = os.system(final_cmd)
        assert error_code == 0, f'Failed to execute: \n{final_cmd}'

        img = Image.open(img_fn)
        w, h = img.size
        encoded_size = os.path.getsize(out_fn)
        bpd_sum += encoded_size / (w * h * 3)

        if delete_imgs:
            os.remove(out_fn)
    final_bpd = bpd_sum / len(imgs_list)
    print(f'Final bpd {final_bpd}')
