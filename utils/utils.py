from collections import namedtuple
import os
import shutil

IMG_FOLDER = 'photos'
OTHER_FOLDER = 'other'

FileProps = namedtuple('FileProps', ['path', 'name', 'extension'])


def is_image(ext):
    valid_extensions = {
        '.png',
        '.jpg',
        '.jpeg',
        '.gif',
        '.icon'
    }

    return ext.lower() in valid_extensions


def create_folder(path, folder_name):
    p = os.path.join(path, folder_name)

    if not os.path.exists(p):
        os.mkdir(p)


def move_file(path, folder, f):
    # filename, extension = os.path.splitext(f)
    # folder = extension[1:] if extension else 'other'
    dest = os.path.join(os.path.join(path, folder), f)
    src = os.path.join(path, f)

    shutil.move(src, dest)