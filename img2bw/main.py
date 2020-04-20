import os
import argparse
import img2bw


def main():
    parser = argparse.ArgumentParser()

    # Mandatory parameters
    parser.add_argument('--input', help="Input file or directory", default=None)
    parser.add_argument('--output', help="Output file or directory", default=None)
    parser.add_argument('--output-ext', help="Output file extension",
                        choices=img2bw.VALID_EXTENSIONS, default=img2bw.VALID_EXTENSIONS[0])

    # Options
    ALGORITHMS_MODES = img2bw.METHODS_AVAILABLE + ["try-all"]
    parser.add_argument('--method', help="Method used to perform the binarization",
                        choices=ALGORITHMS_MODES, default=ALGORITHMS_MODES[0])
    parser.add_argument('--block-size', help="Odd size of pixel neighborhood which is used to calculate the "
                                             "threshold value (local threshold)", default=35, type=int)
    parser.add_argument('--num-classes', help="Number of classes to be thresholded (multiotsu)", default=3, type=int)

    args = parser.parse_args()
    if args.input:
        # Set default paths
        input_dir = os.path.abspath(args.input) if args.input else os.path.abspath(os.getcwd())
        output_dir = os.path.abspath(args.output) if args.output else os.path.abspath(os.getcwd())

        # Extract text
        img2bw.binarizer_loader(input_dir, output_dir, args.method, args.output_ext,
                                block_size=args.block_size, num_classes=args.num_classes)
        print("Done!")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
