from functools import partial
import os
import sys
import traceback

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QApplication, QMenu, QAction, QWidget, QLabel
from PyQt5.QtCore import Qt, QPoint, QCoreApplication, QTimer, QEvent, QSize
from PyQt5.QtGui import QIcon, QKeySequence

from .mainwindow_ui import Ui_MainWindow
from .addfilesdialog import AddFilesDialog
from .renamedialog import RenameDialog
from .movefilesdialog import MoveFilesDialog
from .textviewdialog import TextViewDialog
from .aboutdialog import AboutDialog
from .convertdialog import ConvertDialog
from .convertfilesdialog import ConvertFilesDialog
from .runplugindialog import RunPluginDialog
from .settingsdialog import SettingsDialog

import config
import database
from plugin_collection import PluginCollection
from .pluginform import PluginForm
from mark.markread import MarkRead

settings = config.settings


_t = QCoreApplication.translate


class MainWindow (QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.menu = None
        config.init()
        config.load()
        database.init()

        self.prevSplitterSizes = None
        self.isAutoApplyFilter = True
        self.actionsEnabled = False

        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon(':/icons/fb2tool_32px.png'))
        
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setStretchFactor(0, 0)
        self.splitter.setStretchFactor(1, 1)
       
        if settings.ui_window_x and settings.ui_window_y:
            self.move(settings.ui_window_x, settings.ui_window_y)

        if settings.ui_window_height and settings.ui_window_width:
            self.resize(settings.ui_window_width, settings.ui_window_height)

        if len(settings.ui_splitter_sizes) > 0:
            if settings.ui_info_panel_visible:
                self.actionViewInfo_panel.setChecked(True)
                self.splitter.setSizes(settings.ui_splitter_sizes)
            else:
                self.actionViewInfo_panel.setChecked(False)
                self.prevSplitterSizes = settings.ui_splitter_sizes
                self.onViewInfoPanel(False)
        
        self.frameFilter.setVisible(settings.ui_filter_panel_visible)
        self.actionFilter_panel.setChecked(settings.ui_filter_panel_visible)
        self.isAutoApplyFilter = settings.ui_auto_apply_filter
        
        self.textFilter.clicked.connect(self.onToolFilterMenu)
        self.textFilter.textChanged.connect(self.setFilterOnTextChanged)
        self.textFilter.returnPressed.connect(self.setFilterOnReturnPressed)

        self.bookInfo.clear()

        self.bookList.setColumnsWidth(settings.ui_columns_width)
        self.bookList.setColumnsOrder(settings.ui_columns_order)
        self.bookList.setHiddenColumns(settings.ui_hidden_columns)
        self.bookList.setHiddenColumnsWidth(settings.ui_hidden_columns_width)
        self.bookList.selectionModel().selectionChanged.connect(self.onBookListSelectionChanged)

        self.bookList.installEventFilter(self)
        self.bookList.setContextMenuPolicy(Qt.CustomContextMenu)

        self.bookList.customContextMenuRequested.connect(self.onBookListContextMenu)

        self.toolBar.visibilityChanged.connect(self.onToobarVisibilityChange)
        self.toolBar_plugins.visibilityChanged.connect(self.onToobar_pluginsVisibilityChange)
        self.toolBar.setVisible(settings.ui_toolbar_visible)
        self.toolBar_plugins.setVisible(settings.ui_toolbar_plugins_visible)

        if settings.ui_toolbar_icon_size == 'small':
            self.onToolbarIconSmall()
        else:
            self.onToolbarIconLarge()
        self.actionSave_metadata.setEnabled(False)
        self.bookInfo.dataChanged.connect(self.OnBookInfoDataChanged)

        self.setPlatformUI()

        self.bookInfo.mainInfoCollapsed = settings.ui_main_info_collapsed
        self.bookInfo.publishInfoCollapsed = settings.ui_publish_info_collapsed
        self.bookInfo.coverInfoCollapsed = settings.ui_cover_info_collapsed
        self.bookInfo.descriptionInfoCollapsed = settings.ui_description_info_collapsed

        QTimer.singleShot(1, self.loadFilesFromCommandLine)

        # Init plugins
        self.pluginCollection = PluginCollection()
        self.initPluginsMenu()

        self.toolBar.setIcons()
        self.actionsSetEnabled()
        self.onToolbar_plugins()
        self.statusbar()

        self.markread = MarkRead()
        self.mark_enable()

    def mark_enable(self):
        if os.path.isfile(os.path.join(config.config_path, 'markread')):
            self.actionMark_read.setVisible(True)
        else:
            self.actionMark_read.setVisible(False)

    def statusbar(self):
        self.total = QLabel(_t('main', 'List is empty'))
        self.statusBar.addWidget(self.total)
        self.sel_book = QLabel('')
        self.statusBar.addWidget(self.sel_book)

    def runPlugin(self, action):
        plugin = action.data()
        run_plugin = True

        book_info_list = self.getSelectedBookList()
        if len(book_info_list):
            try:
                plugin.init()
                pluginForm = PluginForm(self, plugin.params(), title=plugin.title())
                if pluginForm.exec_():
                    plugin_params = pluginForm.getParams()
                    plugin.set_params(plugin_params)
                    plugin.validate()
                else:
                    run_plugin = False
            except:
                run_plugin = False
                errorDialog = TextViewDialog(self, [{'src': None, 'dest': None, 'error': traceback.format_exc()}])
                errorDialog.exec()

            if run_plugin:
                self.wait()
        
                runPluginDialog = RunPluginDialog(self, plugin, book_info_list)
                runPluginDialog.exec()

                self.bookList.updateRows()
                self.stopWait()

                errors = runPluginDialog.getErrors()
                if len(errors) > 0:
                    errorDialog = TextViewDialog(self, errors)
                    errorDialog.exec()
                else:
                    QMessageBox.information(self, 'Fb2Tool', _t('main',
                                                                    'Operation "{0}" complete').format(plugin.title()))
                        
    def initPluginsMenu(self):
        for plugin in self.pluginCollection.plugins():
            try:
                plugin.init()
                action = self.menuTools.addAction(plugin.title())
                action.setData(plugin)
                if plugin.hotkey():
                    action.setShortcut(QKeySequence(plugin.hotkey()))
                action.setIcon(QIcon(plugin.icon))
                action.triggered.connect(partial(self.runPlugin, action))
            except Exception as e:
                print(e)
        self.menuTools.addSeparator()
        action = self.menuTools.addAction(_t('main', 'Reload plugins'))
        action.setIcon(QIcon(':/icons/reload_plugins_30px.png'))
        action.triggered.connect(self.reloadPlugins)
        if len(self.pluginCollection.errors) > 0:
            errorDialog = TextViewDialog(self, self.pluginCollection.errors)
            errorDialog.exec()

    def reloadPlugins(self):
        self.menuTools.clear()
        self.toolBar_plugins.clear()
        self.pluginCollection.reload_plugins()
        self.initPluginsMenu()
        self.onToolbar_plugins()
        self.actionsSetEnabled()

    def onBookListContextMenu(self, point):
        self.menu = QMenu()
        self.menu.addAction(self.actionRename)
        self.menu.addAction(self.actionConvert)
        self.menu.addSeparator()
        for plugin in self.pluginCollection.plugins():
            try:
                if plugin.is_context_menu():
                    action = self.menu.addAction(plugin.title())
                    action.setEnabled(self.menuTools.isEnabled())
                    action.setIcon(QIcon(plugin.icon))
                    action.setData(plugin)
                    if plugin.hotkey():
                        action.setShortcut(QKeySequence(plugin.hotkey()))
                    action.triggered.connect(partial(self.runPlugin, action))
            except Exception as e:
                print(e)

        self.menu.addSeparator()
        self.menu.addAction(self.actionRemove_selected_files)

        self.menu.exec(self.bookList.viewport().mapToGlobal(point))

    def eventFilter(self, source, event):
        if source is self.bookList:
            if event.type() == QEvent.DragEnter:
                if event.mimeData().hasUrls():
                    event.accept()
                    return True
            elif event.type() == QEvent.Drop:
                urlList = [x.toLocalFile() for x in event.mimeData().urls()]
                self.addFilesAndDirs(urlList)
                event.accept()
                return True
        return QWidget.eventFilter(self, source, event)

    def addFilesAndDirs(self, list_to_load):
        files_to_load = []
        if list_to_load == "def":
            if settings.convert_default_dir:
                for root, dir, files in os.walk(settings.convert_default_dir):
                    for file in files:
                        files_to_load.append(os.path.join(root, file))
            else:
                QMessageBox.critical(self, 'Fb2Tool', _t('main', 'Key "Default dir" not exists or is null'))
        else:
            for item in list_to_load:
                if os.path.isdir(item):
                    for root, dir, files in os.walk(item):
                        for file in files:
                            files_to_load.append(os.path.join(root, file))
                elif os.path.isfile(item):
                    files_to_load.append(item)
        if len(files_to_load) > 0:
            self.AddFiles(files_to_load)

    def loadFilesFromCommandLine(self):
        if len(sys.argv) > 1:
            if sys.argv[1] == "def":
                self.addFilesAndDirs("def")
            elif sys.argv[1] == "markread":
                self.close()
                self.onMarkRead()
            else:
                self.addFilesAndDirs(sys.argv[1:])

    def OnBookInfoDataChanged(self, dataChanged):
        self.actionSave_metadata.setEnabled(dataChanged)

    def setFilterOnTextChanged(self):
        if self.isAutoApplyFilter:
            self.setFilter()

    def setFilterOnReturnPressed(self):
        if not self.isAutoApplyFilter:
            self.setFilter()

    def setFilter(self):
        self.bookList.setFilter(self.textFilter.text())  

    def onAddFiles(self):
        result = QFileDialog.getOpenFileNames(self, 
                                              caption=_t('main', 'Add files'), 
                                              directory=settings.add_files_last_selected,
                                              filter=_t('main', 'Ebook files (*.fb2 *.fb2.zip *.epub);;All files (*.*)'))
        if len(result[0]) > 0:
            self.AddFiles(result[0])
            for file in result[0]:
                (settings.add_files_last_selected, _) = os.path.split(file)

    def onAddFolder(self):
        fileList = []
        folder = QFileDialog.getExistingDirectory(self,
                                                  caption=_t('main', 'Add folder'),
                                                  directory=settings.add_folder_last_selected)
        if folder:
            settings.add_folder_last_selected = folder
            for root, dir, files in os.walk(folder):
                for file in files:
                    fileList.append(os.path.join(root, file))
        
            self.AddFiles(fileList)

    def AddFiles(self, files):
        # Remove unsupported files from list
        files = [file for file in files if file.lower().endswith(('.fb2', '.fb2.zip', '.epub'))]
        if len(files) > 0:
            loadFilesDialog = AddFilesDialog(self, files)
            loadFilesDialog.exec()
            self.bookList.updateRows()
            errors = loadFilesDialog.getErrors()
            if len(errors) > 0:
                errorDialog = TextViewDialog(self, errors)
                errorDialog.exec()
        self.bookList.setFocus()
        self.bookList.selectRow(0)
        self.sel_book.setText(self.onSklon(_t('main', 'book'), _t('main', 'books'), _t('main', 'books'), '1'))
        total = self.bookList.model().rowCount()
        sclon = self.onSklon(_t('main', 'book'), _t('main', 'books'), _t('main', 'books'))
        self.total.setText(_t('main', 'On the list {0} {1}').format(total, sclon))

    def onSelectAll(self):
        self.wait()
        self.bookList.selectAll()
        self.sel_book.setText(self.onSklon(_t('main', 'book'), _t('main', 'books'), _t('main', 'books'), '1'))
        self.stopWait()

    def onRemoveSelected(self):
        self.wait()
        self.bookList.remove(self.bookList.getSelectedId())
        total = self.bookList.model().rowCount()
        sclon = self.onSklon(_t('main', 'book'), _t('main', 'books'), _t('main', 'books'))
        self.total.setText(_t('main', 'On the list {0} {1}').format(total, sclon))
        if self.bookList.model().rowCount() == 0:
            self.total.setText(_t('main', 'List is empty'))
            self.bookInfo.clear()
            self.actionsEnabled = False
            self.actionsSetEnabled()
        self.stopWait()

    def wait(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)

    def stopWait(self):
        QApplication.restoreOverrideCursor()

    def getSelectedBookList(self):
        list_id = self.bookList.getSelectedId()
        book_info_list = []
        for id in list_id:
            book_info = database.get_book_info(id)
            book_info_list.append(book_info)
        return book_info_list

    def onBookListSelectionChanged(self):
        if self.bookInfo.isDataChanged:
            if QMessageBox.question(self, 'Fb2Tool', _t('main', 'Save changes?')) == QMessageBox.Yes:
                self.SaveMetadata()

        book_info_list = self.getSelectedBookList()

        self.bookInfo.clear()

        if len(book_info_list) > 0:
            self.actionsEnabled = True
            self.bookInfo.setData(book_info_list)
        else:
            self.actionsEnabled = False
        self.sel_book.setText(self.onSklon(_t('main', 'book'), _t('main', 'books'), _t('main', 'books'), '1'))
        self.actionsSetEnabled()

    def onSklon(self, one, two, five, ch=''):
        n = len(self.bookList.selectionModel().selectedRows()) if ch else self.bookList.model().rowCount()
        ost = len(self.bookList.selectionModel().selectedRows()) if ch else self.bookList.model().rowCount()
        ost %= 10
        if ost == 1 and n != 11:
            return _t('main', '{0} {1} is choosen').format(str(ost), one) if ch else one
        elif 2 <= ost <= 4 or n == 11:
            return _t('main', '{0} {1} are selected').format(str(ost), two) if ch else two
        else:
            return _t('main', '{0} {1} is selected').format(str(ost), five) if ch else five

    def actionsSetEnabled(self):
        self.actionRename.setEnabled(self.actionsEnabled)
        self.actionConvert.setEnabled(self.actionsEnabled)
        self.actionSelect_all.setEnabled(self.actionsEnabled)
        self.actionRemove_selected_files.setEnabled(self.actionsEnabled)
        self.menuTools.setEnabled(self.actionsEnabled)
        self.toolBar_plugins.setEnabled(self.actionsEnabled)

    def onViewFilterPanel(self, isVisible):
        self.frameFilter.setVisible(isVisible)
        if not isVisible:
            self.bookList.setFilter('')
        else:
            self.setFilter()
            self.textFilter.setFocus(True)

    def onViewInfoPanel(self, checked):
        self.splitter.setChildrenCollapsible(not checked)

        if checked:
            self.splitter.setHandleWidth(1)
            self.splitter.setSizes(self.prevSplitterSizes)
        else:
            self.prevSplitterSizes = self.splitter.sizes()
            self.splitter.setHandleWidth(0)
            self.splitter.setSizes((0, 1))

    def onViewToolbar(self, checked):
        self.toolBar.setVisible(checked)

    def onViewTollbar_Plugins(self, checked):
        self.toolBar_plugins.setVisible(checked)

    def onSaveMetadata(self):
        if self.bookInfo.isDataChanged:
            self.SaveMetadata()

    def SaveMetadata(self):
        self.wait()
        book_info_list = self.bookInfo.getData()
        errors = []
        for book_info in book_info_list:
            try:
                database.update_book_info(book_info)
            except Exception as e:
                errors.append({'src': book_info.file, 'dest': None, 'error': str(e)})
        self.bookInfo.isDataChanged = False
        self.actionSave_metadata.setEnabled(False)
        self.bookList.updateRows()
        self.stopWait()
        if len(errors) > 0:
            errorDialog = TextViewDialog(self, errors)
            errorDialog.exec()

    def onRename(self):
        book_info_list = self.getSelectedBookList()
        if len(book_info_list):
            renameDialog = RenameDialog(self)
            renameDialog.bookList = book_info_list
            renameDialog.authorFormatList = settings.rename_author_template_list
            renameDialog.tranlatorFormatList = settings.rename_translator_template_list
            renameDialog.filenameFormatList = settings.rename_filename_template_list
            renameDialog.renamePathList = settings.rename_path_list
            renameDialog.authorFormat = settings.rename_author_format
            renameDialog.translatorFormat = settings.rename_translator_format
            renameDialog.filenameFormat = settings.rename_filename_format
            renameDialog.deleteSourceFiles = settings.rename_delete_source_files
            renameDialog.overwriteExistingFiles = settings.rename_overwrite
            renameDialog.backupBeforeRename = settings.rename_backup
            renameDialog.renameInSourceFolder = settings.rename_in_source_folder
            renameDialog.renameMoveToFolder = settings.rename_move_to_folder
            
            if renameDialog.exec_():
                self.wait()
                moveFilesDialog = MoveFilesDialog(self,
                                                  book_info_list=book_info_list,
                                                  filename_format=renameDialog.filenameFormat,
                                                  author_format=renameDialog.authorFormat,
                                                  translator_format=renameDialog.translatorFormat,
                                                  delete_src=renameDialog.deleteSourceFiles,
                                                  backup_src=renameDialog.backupBeforeRename,
                                                  overwrite_exists=renameDialog.overwriteExistingFiles,
                                                  rename_in_source_folder=renameDialog.renameInSourceFolder,
                                                  move_to_folder=renameDialog.renameMoveToFolder)
                moveFilesDialog.exec()
                self.bookList.updateRows()
                self.stopWait()
                
                settings.rename_delete_source_files = renameDialog.deleteSourceFiles
                settings.rename_overwrite = renameDialog.overwriteExistingFiles
                settings.rename_backup = renameDialog.backupBeforeRename
                settings.rename_in_source_folder = renameDialog.renameInSourceFolder
                settings.rename_move_to_folder = renameDialog.renameMoveToFolder

                errors = moveFilesDialog.getErrors()
                if len(errors) > 0:
                    errorDialog = TextViewDialog(self, errors)
                    errorDialog.exec()

            settings.rename_author_format = renameDialog.authorFormat
            settings.rename_translator_format = renameDialog.translatorFormat
            settings.rename_filename_format = renameDialog.filenameFormat
            settings.rename_author_template_list = renameDialog.authorFormatList
            settings.rename_translator_template_list = renameDialog.tranlatorFormatList
            settings.rename_filename_template_list = renameDialog.filenameFormatList
            settings.rename_path_list = renameDialog.renamePathList
            config.save()

    def onConvert(self):
        if (not settings.convert_converter_path or 
                (settings.convert_converter_path and not os.path.exists(settings.convert_converter_path))):
            QMessageBox.critical(self, 'Fb2Tool', _t('main', 'Check settings for fb2converter!'))
            
            return
       
        convertDialog = ConvertDialog(self)
        convertDialog.outputFormat = settings.convert_output_format
        convertDialog.outputPath = settings.convert_output_path
        convertDialog.overwrite = settings.convert_overwrite
        convertDialog.stk = settings.convert_stk
        convertDialog.convertPathList = settings.convert_path_list
        convertDialog.packoutput = settings.convert_pack_output
        convertDialog.movetofinal = settings.convert_movetofinal
        convertDialog.finalDir = settings.convert_finaldir
        convertDialog.packfinal = settings.convert_pack_final
        convertDialog.usestructursrc = settings.convert_use_structur_src
        convertDialog.authorpattern = settings.convert_author_pattern
        convertDialog.dirpattern = settings.convert_dir_pattern
        if convertDialog.exec_():
            book_info_list = self.getSelectedBookList()
            convertProgress = ConvertFilesDialog(self,
                                                 book_info_list=book_info_list,
                                                 out_format=convertDialog.outputFormat,
                                                 out_path=convertDialog.outputPath,
                                                 overwrite=convertDialog.overwrite,
                                                 stk=convertDialog.stk,
                                                 debug=convertDialog.debug,
                                                 converter_path=settings.convert_converter_path,
                                                 converter_config=settings.convert_converter_config,
                                                 packoutput=convertDialog.packoutput,
                                                 movetofinal=convertDialog.movetofinal,
                                                 finaldir=convertDialog.finalDir,
                                                 packfinal=convertDialog.packfinal,
                                                 usestructursrc=convertDialog.usestructursrc,
                                                 authorpattern=convertDialog.authorpattern,
                                                 dirpattern=convertDialog.dirpattern)
            convertProgress.exec()

            if len(convertProgress.errors) > 0:
                errorDialog = TextViewDialog(self, convertProgress.errors)
                errorDialog.exec()

            settings.convert_output_format = convertDialog.outputFormat
            settings.convert_output_path = convertDialog.outputPath
            settings.convert_overwrite = convertDialog.overwrite 
            settings.convert_stk = convertDialog.stk
            settings.convert_path_list = convertDialog.convertPathList
            settings.convert_pack_output = convertDialog.packoutput
            settings.convert_movetofinal = convertDialog.movetofinal
            settings.convert_finaldir = convertDialog.finalDir
            settings.convert_pack_final = convertDialog.packfinal
            settings.convert_use_structur_src = convertDialog.usestructursrc
            settings.convert_author_pattern = convertDialog.authorpattern
            settings.convert_dir_pattern = convertDialog.dirpattern
            config.save()
            self.onRemove_Null_Records_in_Booklist()

    def onSettings(self):
        settingsDialog = SettingsDialog(self)
        settingsDialog.defaultDir = settings.convert_default_dir
        settingsDialog.converterPath = settings.convert_converter_path
        settingsDialog.converterConfig = settings.convert_converter_config

        if settingsDialog.exec_():
            settings.convert_default_dir = settingsDialog.defaultDir
            settings.convert_converter_path = settingsDialog.converterPath
            settings.convert_converter_config = settingsDialog.converterConfig
        if settingsDialog.myclose:
            config.save()
            QMessageBox.information(self, 'Fb2Tool', _t('main', 'Settings has been saved'))

    def onRemove_Null_Records_in_Booklist(self):
        self.bookList.setFocus()
        list_id = []
        for i in range(self.bookList.model().rowCount()):
            self.bookList.selectRow(i)
            book_sel = self.getSelectedBookList()[0]
            if not os.path.exists(book_sel.file):
                list_id.append(book_sel.id)
        self.bookList.remove(list_id)
        if self.bookList.model().rowCount() > 0:
            self.bookList.selectRow(0)
        else:
            self.bookInfo.clear()
            self.actionsSetEnabled()

    def onToolFilterMenu(self):
        actionList = {
            'title': _t('main', 'Title'),
            'authors': _t('main', 'Author'),
            'series': _t('main', 'Series'),
            'tags': _t('main', 'Tags'),
            'lang': _t('main', 'Lang'),
            'translators': _t('main', 'Translator'),
            'type': _t('main', 'Type'),
            'file': _t('main', 'File')
        }
        menu = QMenu()
        for key in actionList:
            acitonItem = menu.addAction(actionList[key])
            acitonItem.setData(key)

        menu.addSeparator()

        actionItem = menu.addAction('AND')
        actionItem.setData('AND')
        actionItem = menu.addAction('OR')
        actionItem.setData('OR')

        menu.addSeparator()
        actionItem = QAction(_t('main', 'Auto-apply filter'), parent=menu, checkable=True, checked=self.isAutoApplyFilter)
        actionItem.setData('AutoApplyFilter')
        menu.addAction(actionItem)
        
        menu_x = -1 * menu.sizeHint().width() + self.textFilter.width()
        menu_y = -1 * menu.sizeHint().height() - 2
        
        action = menu.exec_(self.textFilter.mapToGlobal(QPoint(menu_x , menu_y)))
        if action:
            if action.data() == 'AutoApplyFilter':
                self.isAutoApplyFilter = not self.isAutoApplyFilter
            elif action.data() in ('AND', 'OR'):
                self.textFilter.setText(self.textFilter.text() + ' {} '.format(action.data()))
            else:
                self.textFilter.setText(self.textFilter.text() + ' {}:'.format(action.data()))
            self.textFilter.setFocus(True)

    def onToolbarIconLarge(self):
        self.toolBar.setLargeIcons()
        self.toolBar_plugins.setIconSize(QSize(36, 36))
        self.actionToolbarIconsLarge.setChecked(True)
        self.actionToolbarIconSmall.setChecked(False)

    def onToolbarIconSmall(self):
        self.toolBar.setSmallIcons()
        self.toolBar_plugins.setIconSize(QSize(24, 24))
        self.actionToolbarIconsLarge.setChecked(False)
        self.actionToolbarIconSmall.setChecked(True)

    def onToobarVisibilityChange(self):
        self.actionViewToolbar.setChecked(self.toolBar.isVisible())

    def onToobar_pluginsVisibilityChange(self):
        self.actionView_Toolbar_Tools.setChecked(self.toolBar_plugins.isVisible())

    def onToolbar_plugins(self):
        for plugin in self.pluginCollection.plugins():
            if plugin.pane:
                actionpane = self.toolBar_plugins.addAction(QIcon(plugin.icon), plugin.description())
                actionpane.setData(plugin)
                actionpane.triggered.connect(partial(self.runPlugin, actionpane))

    def setPlatformUI(self):
        self.frameFilter.setStyleSheet('''
            #frameFilter {
                border-top: 1px solid #bfbfbf;
            }
        ''')
        self.splitter.setStyleSheet('''
            QSplitter::handle { 
                background: #bfbfbf; 
            }
        ''')
        if sys.platform == 'win32':
            self.toolBar.setStyleSheet('''
                #toolBar { 
                    padding:4px; 
                    border-bottom: 1px solid #bfbfbf; 
                    border-left: 1px solid #ffffff; 
                    border-right: 1px solid #ffffff;  
                    background-color: #f7f7f7
                } 
            ''')
        
        elif sys.platform == 'darwin':
            self.toolBar.setStyleSheet('''
                #toolBar {
                    padding: 4px;
                }
            ''')
            self.setUnifiedTitleAndToolBarOnMac(True)
            self.frameFilter.layout().setContentsMargins(8, 8, 8, 8)
        else:
            self.toolBar.setStyleSheet('''
                #toolBar { 
                    padding: 2px;
                    border-bottom: 1px solid #bfbfbf; 
                    border-left: 1px solid #ffffff; 
                    border-right: 1px solid #ffffff;  
                    background-color: #f7f7f7}
            ''')

    def onAbout(self):
        about = AboutDialog(self)
        about.exec()

    def onMarkRead(self):
        self.markread.show()
        if not self.markread.fill_list_book():
            QMessageBox.critical(self.markread, "Ошибка", "Что-то не так с базой данных или с запросом к ней")
            self.markread.onSettings()

    def onAboutQt(self):
        QMessageBox.aboutQt(self)

    def closeEvent(self, e):
        self.exitApp()

    def onRestart(self):
        self.close()
        win = MainWindow()
        win.show()

    def onExit(self):
        self.close()

    def exitApp(self):
        settings.ui_window_x = self.pos().x()
        settings.ui_window_y = self.pos().y()
        settings.ui_window_width = self.size().width()
        settings.ui_window_height = self.size().height()
        settings.ui_info_panel_visible = self.actionViewInfo_panel.isChecked()
        settings.ui_filter_panel_visible = self.actionFilter_panel.isChecked()
        settings.ui_toolbar_visible = self.toolBar.isVisible()
        settings.ui_toolbar_plugins_visible = self.toolBar_plugins.isVisible()
        settings.ui_auto_apply_filter = self.isAutoApplyFilter
        settings.ui_columns_order = self.bookList.getColumnsOrder()
        settings.ui_columns_width = self.bookList.getColumnsWidth()
        settings.ui_hidden_columns = self.bookList.getHiddenColumns()
        settings.ui_hidden_columns_width = self.bookList.getHiddenColumnsWidth()
        settings.ui_toolbar_icon_size = 'small' if self.actionToolbarIconSmall.isChecked() else 'large'
        settings.ui_main_info_collapsed = self.bookInfo.mainInfoCollapsed
        settings.ui_publish_info_collapsed = self.bookInfo.publishInfoCollapsed
        settings.ui_cover_info_collapsed = self.bookInfo.coverInfoCollapsed
        settings.ui_description_info_collapsed = self.bookInfo.descriptionInfoCollapsed
        if self.actionViewInfo_panel.isChecked():
            settings.ui_splitter_sizes = self.splitter.sizes()
        else:
            settings.ui_splitter_sizes = self.prevSplitterSizes
        database.close()
        config.save()
        os.remove(config.database_name)
