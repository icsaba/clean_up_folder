from os.path import splitext, isfile, join
from os import listdir

from handlers.default_folder_handler import DefaultFolderHandler
from handlers.image_folder_handler import ImageFolderHandler
from metas.command import Command


class CreateFolders(Command):

    def __init__(self, path):
        self.path = path
        self.handler = ImageFolderHandler(DefaultFolderHandler())

    def execute(self):
        extensions = [splitext(f)[1] for f in listdir(self.path) if isfile(join(self.path, f))]

        for extension in extensions:
            self.handler.handle(extension, self.path)
