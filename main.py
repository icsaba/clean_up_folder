import argparse

from commands.create_folders import CreateFolders
from commands.move_files import MoveFiles


def main(path):

    command_stack = [
        CreateFolders(path),
        MoveFiles(path)
    ]

    for cmd in command_stack:
        cmd.execute()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cleaning up a given folder')
    parser.add_argument('--path', help='absolute path of the folder')

    args = parser.parse_args()

    main(args.path)
