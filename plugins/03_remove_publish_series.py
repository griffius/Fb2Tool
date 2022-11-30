from config import icons_path
from plugin_collection import MetaPlugin


class RemovePublisherSeries(MetaPlugin):
    def init(self, **kwargs):
        self._title = 'Удалить издательскую серию'
        self._description = 'Данный плагин удаляет издательскаю серию и номер, если они присутствуют'
        self._hotkey = None
        self._is_context_menu = True
        self.pane = True
        self.icon = icons_path + '/del_publish_series.png'

    def validate(self):
        pass

    def perform_operation(self, meta):
        meta.publish_info.series = ''
        meta.publish_info.series_index = ''
        return meta
