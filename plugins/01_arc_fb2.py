# Плагин архивирует файл *.fb2 в файл *.fb2.zip
from config import icons_path
from plugin_collection import FilePlugin, DebugException, Param
from ebookmeta.myzipfile import ZipFile, ZIP_DEFLATED
import os
import ebookmeta


class ZipFb2(FilePlugin):
    def init(self, **kwargs):
        self._title = 'Архивировать fb2 в fb2.zip'
        self._description = 'Преобразовывает файлы fb2 в формат fb2.zip'
        self._hotkey = 'Alt+A'
        self._is_context_menu = True
        self.pane = True
        self.icon = icons_path + '/arc_fb2.png'
        dest_folder = self.load_settings('dest_folder_arc', default_value='')
        self.add_param(name='dest_folder',
                       type=Param.Folder,
                       title='Поместить файлы в папку:',
                       default_value=dest_folder)
        self.add_param(name='create_tree',
                       type=Param.Boolean,
                       title='Создавать структуру папок на основе тегов',
                       default_value=False)
        self.add_param(name='pattern',
                       type=Param.Choice,
                       title='Шаблон имени автора:',
                       default_value=['#f {#m }#l', '#l {#m }#f'])

        self.add_param(name='delete_source',
                       type=Param.Boolean,
                       title='Удалить исходные файлы после архивации',
                       default_value=False)

    def validate(self):
        dest_folder = self.get_param('dest_folder').value
        self.save_settings('dest_folder_arc', value=dest_folder)

    def perform_operation(self, file):
        if file.lower().endswith('.fb2'):
            file_path = os.path.dirname(file)
            file_name = os.path.basename(file)
            if self.get_param('create_tree').value:
                meta = ebookmeta.get_metadata(file)
                new_file_name = meta.get_filename_by_pattern('#Author/#Series/#Author{ - #Series{ - #number}} - #Title',
                                                             self.get_param('pattern').value) + '.zip'
                if self.get_param('dest_folder').value:
                    zip_name = os.path.join(self.get_param('dest_folder').value, new_file_name)
                else:
                    zip_name = new_file_name
                dst = os.path.normpath(os.path.join(file_path, zip_name))
                if not os.path.exists(dst):
                    if not os.path.exists(os.path.dirname(dst)):
                        os.makedirs(os.path.dirname(dst))
                else:
                    raise DebugException(f'Файл "{zip_name}" уже существует!')
                zipp = ZipFile(dst, mode='w', compression=ZIP_DEFLATED)
                zipp.write(file, file_name)
                zipp.close()
                if self.get_param('delete_source').value:
                    os.remove(file)
                return dst
            else:
                if self.get_param('dest_folder').value:
                    zip_name = os.path.join(self.get_param('dest_folder').value, file_name + '.zip')
                else:
                    zip_name = file + '.zip'

                if not os.path.exists(zip_name):
                    os.chdir(file_path)
                    zipp = ZipFile(zip_name, mode='w', compression=ZIP_DEFLATED)
                    zipp.write(file_name)
                    zipp.close()
                else:
                    raise DebugException(f'Файл "{zip_name}" уже существует!')
                if self.get_param('delete_source').value:
                    os.remove(file)
                return zip_name
        else:
            if file.lower().endswith('.fb2.zip'):
                raise DebugException(f'"{file}" уже заархивирован в fb2.zip')
            else:
                raise DebugException(f'"{file}" не является файлом fb2!')
