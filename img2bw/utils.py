import re
import os
import shutil
import pathlib


def get_tail(filename):
    basedir, tail = os.path.split(filename)
    return tail, basedir


def get_fname(filename):
    basedir, tail = os.path.split(filename)
    fname, ext = os.path.splitext(tail)
    return fname, ext


def get_files(path, extensions=None, sort=True):
    # Must receive a list, a set or a none
    extensions = set(extensions) if extensions else extensions

    # Search
    valid_files = []
    files = os.listdir(path) if os.path.isdir(path) else [path]
    for filename in files:
        fname, ext = get_fname(filename)
        ext = ext.lower().strip().replace('.', '')  # Normalize

        # Skip hidden files (Unix, Windows)
        if not (fname.startswith(".") or fname.startswith("~$")):
            # Check if the extension is valid
            if extensions is None or ext in extensions:
                valid_files.append(os.path.join(path, filename))

    # Sort files using natural order
    if sort:
        valid_files = sorted(valid_files, key=tokenize)
    return valid_files


def create_folder(path, empty_folder=True):
    basedir = os.path.basename(path)

    # Check output path
    if os.path.exists(path) and empty_folder:
        print("\t- [INFO] Deleting '{}' folder contents...".format(basedir))
        shutil.rmtree(path)  # Delete contents recursively

    # Check if we have to create the directory (again)
    if not os.path.exists(path):
        print("\t- [INFO] Creating directories: {}".format(path))
        path = pathlib.Path(path)  # Create path, recursively
        path.mkdir(parents=True, exist_ok=True)


def tokenize(filename):
    # Sorts strings that contain numbers using a natural order (file001, file002, file003, etc)
    digits = re.compile(r'(\d+)')
    return tuple(int(token) if match else token
                 for token, match in
                 ((fragment, digits.search(fragment))
                  for fragment in digits.split(filename)))

