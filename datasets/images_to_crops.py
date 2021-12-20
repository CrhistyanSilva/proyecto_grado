import os
import glob
import argparse
import cv2
import tqdm


def main():
    ap = argparse.ArgumentParser(description='Crop images on squares, default is 64x64')
    ap.add_argument('input', help='Input directory')
    ap.add_argument('output', help='Output directory')
    ap.add_argument('-s', '--size', type=int, default=64, help='Size of the output square images, default is 64')
    args = vars(ap.parse_args())

    input_dir = args['input']
    output_dir = args['output']
    size = args['size']

    assert os.path.isdir(input_dir), 'Input directory does not exist'
    os.makedirs(output_dir, exist_ok=True)

    # Read input images with all extensions
    input_imgs = []
    extensions = ['jpg', 'jpeg', 'png']
    extensions += [x.upper() for x in extensions]
    for extension in extensions:
        input_imgs += glob.glob(os.path.join(input_dir, f'*.{extension}'))
    sorted(input_imgs)

    # Write crops for each image
    for img_fn in tqdm.tqdm(input_imgs, desc='cropping'):
        img = cv2.imread(img_fn)

        basename = os.path.basename(img_fn)
        name, ext = os.path.splitext(basename)

        for i in range(0, img.shape[0], size):
            for j in range(0, img.shape[1], size):
                if i + size < img.shape[0] and j + size < img.shape[1]:
                    crop = img[i:i + size, j:j + size, :]
                    new_name = name + f'-{i + j:03}' + ext
                    out_fn = os.path.join(output_dir, new_name)
                    cv2.imwrite(out_fn, crop)


if __name__ == '__main__':
    main()
