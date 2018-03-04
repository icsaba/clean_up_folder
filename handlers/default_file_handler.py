from metas.handler import Handler
from utils.utils import move_file, OTHER_FOLDER


class DefaultFileHandler(Handler):

    def _handle(self, file_):
        folder_name = file_.extension[1:] if file_.extension else OTHER_FOLDER

        move_file(file_.path, folder_name, file_.name)

        return True
