from metas.handler import Handler
from utils.utils import create_folder, OTHER_FOLDER


class DefaultFolderHandler(Handler):

    def _handle(self, extension, path):
        folder_name = extension[1:] if extension else OTHER_FOLDER

        create_folder(path, folder_name)

        return True
