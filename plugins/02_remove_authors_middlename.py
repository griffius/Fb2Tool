# Плагин удаляет отчество, если оно присутствует у всех авторов книги
from plugin_collection import MetaPlugin
from config import icons_path


class RemoveAuthorMiddleName(MetaPlugin):
    def init(self, **kwargs):
        self._title = 'Удалить отчество у авторов'
        self._description = 'Данный плагин удаляет отчество у авторов, если оно присутствует'
        self._hotkey = None
        self._is_context_menu = True
        self.pane = True
        self.icon = icons_path + '/del_middlename.png'

    def perform_operation(self, meta):
        new_authors = []

        for author in meta.author_list:
            author_part = author.split()
            if len(author_part) == 3:  # У автора есть отчество
                new_author = author_part[0] + ' ' + author_part[2]
                new_authors.append(new_author)
            else:
                new_authors.append(author)

        meta.set_author_list_from_string(','.join(new_authors))

        return meta
