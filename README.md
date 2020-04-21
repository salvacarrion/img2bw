# img2bw

**img2bw** is a simple command-line application to binarize images.

![](https://raw.githubusercontent.com/salvacarrion/img2bw/master/data/readme/montaje_small.jpg)


## Requirements

- Python3.7 or more


## Installation

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


## Thresholding algorithms

These are the available algorithms along with common names and their corresponding papers.
You can use them with the option: `--method (name)`
 
- **Global thresholding:**
    - `otsu`: Otsu's method
        - *Otsu, Nobuyuki. "A threshold selection method from gray-level histograms." IEEE transactions on systems, man, and cybernetics 9.1 (1979): 62-66.*
    - `p-tile`: p-tile threshold algorithm
        - *Parker, J. R. (2010). Algorithms for image processing and computer vision. John Wiley & Sons. (p-tile)*
    - `two-peaks`: Selects two peaks from the histogram and return the index of the minimum value between them.
        - *Parker, J. R. (2010). Algorithms for image processing and computer vision. John Wiley & Sons. (Two peaks)*
    - `multiotsu`: Generates `classes - 1` threshold values to divide gray levels 
        - *Liao, P-S., Chen, T-S. and Chung, P-C., "A fast algorithm for multilevel thresholding", Journal of Information Science and  Engineering 17 (5): 713-727, 2001.*
    - `isodata`: Histogram-based threshold, Ridler-Calvard method or inter-means
        - *Ridler, TW & Calvard, S (1978), "Picture thresholding using an iterative selection method" IEEE Transactions on Systems, Man and Cybernetics 8: 630-632, :DOI:10.1109/TSMC.1978.4310039*
    - `min-error`: Minimum error thresholding algorithm.
        - *Kittler, J. and J. Illingworth. ‘‘On Threshold Selection Using Clustering Criteria,’’ IEEE Transactions on Systems, Man, and Cybernetics 15, no. 5 (1985): 652–655.*
    - `minimum`: Minimum method. The histogram of the input image is computed and smoothed until there are only two maxima.
        - *C. A. Glasbey, "An analysis of histogram-based thresholding algorithms," CVGIP: Graphical Models and Image Processing, vol. 55, pp. 532-537, 1993.*
    - `triangle`: Threshold value based on the triangle algorithm
        - *Zack, G. W., Rogers, W. E. and Latt, S. A., 1977, Automatic Measurement of Sister Chromatid Exchange Frequency,  Journal of Histochemistry and Cytochemistry 25 (7), pp. 741-753 :DOI:10.1177/25.7.70454*
    - `yen`: Yen's method
        - *Yen J.C., Chang F.J., and Chang S. (1995) "A New Criterion for Automatic Multilevel Thresholding" IEEE Trans. on Image Processing, 4(3): 370-378. :DOI:10.1109/83.366472*
    - `mean`: Threshold value based on the mean of grayscale values.
        - *C. A. Glasbey, "An analysis of histogram-based thresholding algorithms," CVGIP: Graphical Models and Image Processing,vol. 55, pp. 532-537, 1993. :DOI:10.1006/cgip.1993.1040*
   
- **Entropy thresholding:**
    - `pun`: Pun's threshold algorithm.
        - *Pun, T. "A New Method for Grey-Level Picture Thresholding Using the Entropy of the Histogram,"" Signal Processing 2, no. 3 (1980): 223–237.*
    - `kapur`: Kapur's threshold algorithm
        - *Kapur, J. N., P. K. Sahoo, and A. K. C.Wong. "A New Method for Gray-Level Picture Thresholding Using the Entropy of the Histogram,"" Computer Vision, Graphics, and Image Processing 29, no. 3 (1985): 273–285.*
    - `johannsen`: Johannsen's threshold algorithm.
        - *Johannsen, G., and J. Bille "A Threshold Selection Method Using Information Measures,"" Proceedings of the Sixth International Conference on Pattern Recognition, Munich, Germany (1982): 140–143.*
    - `li`: Li's iterative Minimum Cross Entropy method
        - *Li C.H. and Lee C.K. (1993) "Minimum Cross Entropy Thresholding" Pattern Recognition, 26(4): 617-625 :DOI:10.1016/0031-3203(93)90115-D*

- **Local thresholding:**
    - `bradley-roth`: Bradley-Roth thresholding algorithm
        - *Bradley, D., & Roth, G. (2007). Adaptive thresholding using the integral image. Journal of Graphics Tools, 12(2), 13-21.*
    - `bernsen`: Bernsen thresholding algorithm
        - *Bernsen, J (1986), "Dynamic Thresholding of Grey-Level Images", Proc. of the 8th Int. Conf. on Pattern Recognition*
    - `contrast`: Contrast thresholding algorithm
        - *Parker, J. R. (2010). Algorithms for image processing and computer vision. John Wiley & Sons. (Contrast thresholding)*
    - `feng`: Feng's thresholding algorithm
        - *Meng-Ling Feng and Yap-Peng Tan, "Contrast adaptive thresholding of low quality document images”, IEICE Electron. Express, Vol. 1, No. 16, pp.501-506, (2004).*
    - `local-mean`: Adaptive or dynamic thresholding. The threshold value is the mean of the neighbourhood area minus the constant C
        - *Source: [https://docs.opencv.org/modules/imgproc/doc/miscellaneous_transformations.html?highlight=threshold#adaptivethreshold](https://docs.opencv.org/modules/imgproc/doc/miscellaneous_transformations.html?highlight=threshold#adaptivethreshold)*
    - `local-median`: Adaptive or dynamic thresholding. The threshold value is the median of the neighbourhood area minus the constant C
        - *Source: [https://docs.opencv.org/modules/imgproc/doc/miscellaneous_transformations.html?highlight=threshold#adaptivethreshold](https://docs.opencv.org/modules/imgproc/doc/miscellaneous_transformations.html?highlight=threshold#adaptivethreshold)*
    - `local-gaussian`: Adaptive or dynamic thresholding. The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant
        - *Source: [https://docs.opencv.org/modules/imgproc/doc/miscellaneous_transformations.html?highlight=threshold#adaptivethreshold](https://docs.opencv.org/modules/imgproc/doc/miscellaneous_transformations.html?highlight=threshold#adaptivethreshold)*
    - `niblack`: Niblack local threshold
        - *Niblack, W.: "An introduction to digital image processing" (Prentice- Hall, Englewood Cliffs, NJ, 1986), pp. 115–116*
    - `sauvola`: Sauvola local threshold
        - *Sauvola, J., Seppanen, T., Haapakoski, S., and Pietikainen, M.: "Adaptive document thresholding". Proc. 4th Int. Conf. on Document Analysis and Recognition, Ulm Germany, 1997, pp. 147–152.*
    - `wolf`: Wolf's thresholding algorithm.
        - *C. Wolf, J-M. Jolion, "Extraction and Recognition of Artificial Text in Multimedia Documents", Pattern Analysis and Applications, 6(4):309-326, (2003).*
    - `nick`: NICK thresholding algorithm.
        - *Khurshid, K., Siddiqi, I., Faure, C., & Vincent, N. (2009, January). Comparison of Niblack inspired Binarization methods for ancient documents. In IS&T/SPIE Electronic Imaging (pp. 72470U-72470U). International Society for Optics and Photonics.*
    - `singh`: Singh thresholding algorithm
        - *Singh, O. I., Sinam, T., James, O., & Singh, T. R. (2012). Local contrast and mean based thresholding technique in image binarization. International Journal of Computer Applications, 51, 5-10.*
   

## More options

To view all the available options, type `img2bw --help` in the terminal:

```
usage: img2bw [-h] [-o OUTPUT] [-e {jpg,jpeg,jfif,png,tiff,bmp,pnm}]
              [-m {otsu,isodata,li,local,mean,minimum,multiotsu,niblack,sauvola,triangle,yen,p-tile,two-peaks,min-error,pun,kapur,johannsen,wolf,nick,bradley-roth,bernsen,contrast,singh,feng,try-all}]
              [-b BLOCK_SIZE] [-c NUM_CLASSES]
              input

positional arguments:
  input                 Input file or directory

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output directory
  -e {jpg,jpeg,jfif,png,tiff,bmp,pnm}, --output-ext {jpg,jpeg,jfif,png,tiff,bmp,pnm}
                        Output file extension
  -m {otsu,isodata,li,local,mean,minimum,multiotsu,niblack,sauvola,triangle,yen,p-tile,two-peaks,min-error,pun,kapur,johannsen,wolf,nick,bradley-roth,bernsen,contrast,singh,feng,try-all}, --method {otsu,isodata,li,local,mean,minimum,multiotsu,niblack,sauvola,triangle,yen,p-tile,two-peaks,min-error,pun,kapur,johannsen,wolf,nick,bradley-roth,bernsen,contrast,singh,feng,try-all}
                        Method used to perform the binarization
  -b BLOCK_SIZE, --block-size BLOCK_SIZE
                        Odd size of pixel neighborhood which is used to
                        calculate the threshold value (local threshold)
  -c NUM_CLASSES, --num-classes NUM_CLASSES
                        Number of classes to be thresholded (multiotsu)

```


## Additional information

This package is simply wrapper to easily apply multiple threshold algorithms to an image (or the images in a directory).
I didn't code the algorithms so I send a big thank you to all the authors of libraries that made this wrapper possible:

- [scikit-image](https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_thresholding.html)
- [pythreshold](https://github.com/manuelaguadomtz/pythreshold)
