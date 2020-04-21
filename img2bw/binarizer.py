import os
from img2bw import utils

import numpy as np

from skimage import io
from skimage.filters import *
from skimage.color import rgb2gray

from pythreshold.global_th import *
from pythreshold.global_th.entropy import *
from pythreshold.local_th import *

# Global variables
METHODS_AVAILABLE = ["otsu", "isodata", "li", "local", "mean", "minimum", "multiotsu",
                     "niblack", "sauvola", "triangle", "yen",
                     "p-tile", "two-peaks", "min-error", "pun", "kapur", "johannsen", "wolf",
                     "nick", "bradley-roth", "bernsen", "contract", "singh", "feng"]

VALID_EXTENSIONS = ["jpg", "jpeg", "jfif", "png", "tiff", "bmp", "pnm"]


def binarizer_loader(input_dir, output_dir, method, output_ext="jpg", *args, **kwargs):
    # Get files
    files = utils.get_files(input_dir, extensions=VALID_EXTENSIONS)

    # Create output folder
    # output_dir = os.path.join(output_dir, "output")
    # utils.create_folder(output_dir, empty_folder=False)

    # Check if the directory exists
    if not os.path.exists(output_dir):
        print("\t- [ERROR] The output directory does not exists")
        return

    # Walk through images
    for i, filename in enumerate(files, 1):
        tail, basedir = utils.get_tail(filename)
        fname, ext = utils.get_fname(filename)

        print("")
        print(f'==============================================================')
        print(f'[INFO] ({i}/{len(files)}) Binarizing image: "{tail}"')
        print(f'==============================================================')

        # Select method/s
        if method == "try-all":
            methods = METHODS_AVAILABLE
        else:
            methods = [method]

        # Allow to use methods
        img = load_image(filename)
        for m in methods:
            try:
                # Convert image to grayscale (2d)
                _img = rgb2gray(img)

                # Binarize image
                _img = binarizer(_img, m, *args, **kwargs)

                # Normalize image to 0..255
                _img = normalize(_img)

                # Convert to uint8
                _img = _img.astype(np.uint8)

                # Save image
                savepath = f"{output_dir}/{fname}_{m}.{output_ext}"
                io.imsave(savepath, _img)
                print(f"\t- [INFO] Image saved! [method: {m}; path: {savepath}")
            except Exception as e:
                print(f"\t- [ERROR] We couldn't binarize the image. [method: {m}; path: {filename}")


def load_image(filename):
    return io.imread(filename)


def binarizer(img, method, *args, **kwargs):

    if method == "otsu":
        thresh = threshold_otsu(img)
        # thresh = otsu_threshold(img)
    elif method == "isodata":
        thresh = threshold_isodata(img)
    elif method == "li":
        thresh = threshold_li(img)
    elif method == "local":
        thresh = threshold_local(img, block_size=kwargs.get("block_size", 35))
        # thresh = lmean_threshold(img, block_size=kwargs.get("block_size", 35))
    elif method == "mean":
        thresh = threshold_mean(img)
    elif method == "minimum":
        thresh = threshold_minimum(img)
    elif method == "multiotsu":
        multi_thresh = threshold_multiotsu(img, classes=kwargs.get("num_classes", 3))
        n_nary = np.digitize(img, bins=multi_thresh)  # Output n classes
        return n_nary
    elif method == "niblack":
        thresh = threshold_niblack(img)
        # thresh = niblack_threshold(img)
    elif method == "sauvola":
        thresh = threshold_sauvola(img)
        # thresh = sauvola_threshold(img)
    elif method == "triangle":
        thresh = threshold_triangle(img)
    elif method == "yen":
        thresh = threshold_yen(img)
    elif method == "p-tile":
        thresh = p_tile_threshold(img, 0.5)
    elif method == "two-peaks":
        thresh = two_peaks_threshold(img)
    elif method == "min-error":
        thresh = min_err_threshold(img)
    elif method == "pun":
        thresh = pun_threshold(img)
    elif method == "kapur":
        thresh = kapur_threshold(img)
    elif method == "johannsen":
        thresh = johannsen_threshold(img)
    elif method == "wolf":
        thresh = wolf_threshold(img)
    elif method == "nick":
        thresh = nick_threshold(img)
    elif method == "bradley-roth":
        thresh = bradley_roth_threshold(img)
    elif method == "bernsen":
        thresh = bernsen_threshold(img)
    elif method == "contract":
        thresh = contrast_threshold(img)
    elif method == "singh":
        thresh = singh_threshold(img)
    elif method == "feng":
        thresh = feng_threshold(img)
    else:
        raise NameError(f"Unknown algorithm '{method}'")
    # Apply binarization
    binary = img > thresh
    return binary


def normalize(img):
    img = img.astype(np.float)
    img = img / np.max(np.abs(img))  # 2D image
    img = img * (255.0 / img.max())
    img = np.nan_to_num(img, nan=0, posinf=0, neginf=0)  # Remove: nan and +-inf (if any)
    return img

