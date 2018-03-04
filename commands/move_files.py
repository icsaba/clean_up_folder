import os

from handlers.default_file_handler import DefaultFileHandler
from handlers.image_file_handler import ImageFileHandler
from metas.command import Command
from utils.utils import FileProps


class MoveFiles(Command):

    def __init__(self, path):
        self.path = path
        self.handler = ImageFileHandler(DefaultFileHandler())

    def execute(self):
        files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]

        for f in files:
            _, extension = os.path.splitext(f)
            file_ = FileProps(self.path, f, extension)

            self.handler.handle(file_)
