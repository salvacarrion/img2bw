# img2bw

**img2bw** is a simple command-line application to binarize images.

**Binarization algorithms:** `otsu`, `isodata`, `li`, `local`, `mean`, `minimum`, `multiotsu`, `niblack`, `sauvola`, 
`triangle`, `yen`, `p-tile`, `two-peaks`, `min-error`, `pun`, `kapur`, `johannsen`, `wolf`,
`nick`, `bradley-roth`, `bernsen`, `contract`, `singh`, `feng`.

Example:

![](https://raw.githubusercontent.com/salvacarrion/img2bw/master/data/readme/montaje_small.jpg)


## Requirements

- Python3


## Installation

Open the terminal, go to the folder of this package and type:

```
pip install img2bw
```


## Usage


To binarize a single image, type:

```
img2bw image.jpg --method otsu
```

To binarize all the images in a directory, type:

```
img2bw input_dir/ --output output_dir/
```

> If no method is specified, `otsu` will be used.
>
> You can try all the methods using `--method try-all`


### More options

To view all the available options, type `img2bw --help` in the terminal:

```
usage: img2bw [-h] [-o OUTPUT] [-e {jpg,jpeg,jfif,png,tiff,bmp,pnm}]
              [-m {otsu,isodata,li,local,mean,minimum,multiotsu,niblack,sauvola,triangle,yen,try-all}]
              [-b BLOCK_SIZE] [-c NUM_CLASSES]
              input

positional arguments:
  input                 Input file or directory

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file or directory
  -e {jpg,jpeg,jfif,png,tiff,bmp,pnm}, --output-ext {jpg,jpeg,jfif,png,tiff,bmp,pnm}
                        Output file extension
  -m {otsu,isodata,li,local,mean,minimum,multiotsu,niblack,sauvola,triangle,yen,try-all}, --method {otsu,isodata,li,local,mean,minimum,multiotsu,niblack,sauvola,triangle,yen,try-all}
                        Method used to perform the binarization
  -b BLOCK_SIZE, --block-size BLOCK_SIZE
                        Odd size of pixel neighborhood which is used to
                        calculate the threshold value (local threshold)
  -c NUM_CLASSES, --num-classes NUM_CLASSES
                        Number of classes to be thresholded (multiotsu)
```

### Additional information

This package is simply wrapper to easily apply multiple threshold algorithms to an image (or a directory).
I didn't code the algorithms in it so I thank the authors of these libraries that made this wrapper possible:

- [scikit-image](https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_thresholding.html)
- [pythreshold](https://github.com/manuelaguadomtz/pythreshold)
