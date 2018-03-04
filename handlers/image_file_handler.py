from metas.handler import Handler
from utils.utils import is_image, move_file, IMG_FOLDER


class ImageFileHandler(Handler):

    def _handle(self, file_):
        if is_image(file_.extension):
            move_file(file_.path, IMG_FOLDER, file_.name)

            return True
        return False
