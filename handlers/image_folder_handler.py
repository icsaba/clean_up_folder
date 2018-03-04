from metas.handler import Handler
from utils.utils import is_image, create_folder, IMG_FOLDER


class ImageFolderHandler(Handler):

    def _handle(self, extension, path):

        if is_image(extension):
            create_folder(path, IMG_FOLDER)

            return True
        return False
