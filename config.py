import os
import json
import codecs
import sys
from types import SimpleNamespace

if sys.platform == 'win32':
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config')
    plugins_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins')
else:
    config_path = os.path.join(os.path.expanduser('~'), '.Fb2Tool', 'config')
    plugins_path = os.path.join(os.path.expanduser('~'), '.Fb2Tool', 'plugins')

config_file = os.path.join(config_path, 'settings.json')
icons_path = os.path.join(plugins_path, 'icons')
database_name = os.path.join(config_path, 'Fb2Tool.db')

settings = SimpleNamespace(
    add_folder_last_selected=os.path.expanduser('~'),
    add_files_last_selected=os.path.expanduser('~'),
    ui_window_x=None,
    ui_window_y=None,
    ui_window_width=None,
    ui_window_height=None,   
    ui_info_panel_visible=True,
    ui_filter_panel_visible=True,
    ui_toolbar_visible=True,
    ui_toolbar_plugins_visible=False,
    ui_statusbar_visible=False,
    ui_toolbar_icon_size='large',
    ui_auto_apply_filter=True, 
    ui_splitter_sizes=[], 
    ui_columns_width=[],
    ui_columns_order=[],
    ui_hidden_columns=[],
    ui_hidden_columns_width=[],
    ui_dialog_size={},
    ui_main_info_collapsed=False,
    ui_publish_info_collapsed=True,
    reader_app_fb2=None,
    reader_app_epub=None,
    rename_in_source_folder=True,
    rename_move_to_folder=os.path.expanduser('~'),
    rename_author_format='{lastname} {f}',
    rename_translator_format='{lastname}',
    rename_filename_format='{author}. {title}',
    rename_delete_source_files=False,
    rename_backup=True,
    rename_overwrite=False,
    rename_author_template_list=[],
    rename_translator_template_list=[],
    rename_filename_template_list=[],
    rename_path_list=[],
    convert_path_list=[],
    convert_path_list_final_fb2=[],
    convert_converter_path=None,
    convert_converter_config=None,
    convert_output_format=None,
    convert_output_path=None,
    convert_overwrite=False,
    convert_stk=False,
    convert_default_dir=None,
    convert_movetofinal=False,
    convert_finaldir=None,
    convert_pack_output=False,
    convert_pack_final=False,
    convert_use_structur_src=False,
    convert_author_pattern='#l{ #f}',
    convert_dir_pattern='#Series',
    plugin_settings={}
)


def init():
    if not os.path.exists(config_path):
        os.makedirs(config_path)
    if os.path.exists(database_name):
        os.unlink(database_name)


def save():
    (config_dir, _) = os.path.split(config_file)
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    with codecs.open(config_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(settings.__dict__, sort_keys=False, indent=4))


def load():
    if not os.path.exists(config_path):
        os.makedirs(config_path)

    if os.path.exists(config_file):
        with codecs.open(config_file, 'r', encoding='utf-8') as f:
            c = json.loads(f.read())
    
        for key in c:
            settings.__dict__[key] = c[key]
