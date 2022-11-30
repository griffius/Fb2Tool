from ebookmeta.utils import split_ext
from plugin_collection import FilePlugin
import os
import shutil
import ebookmeta
from ebookmeta.myzipfile import ZipFile, ZIP_DEFLATED


class MoveArchiver(FilePlugin):
	def __init__(self, booka='', finaldir='', use_structur='', dir_pattern='', author_pattern='', dir_out=''):
		super().__init__()
		self.booka = booka
		self.finaldir = finaldir
		self.use_structur = use_structur
		self.dir_pattern = dir_pattern
		self.author_pattern = author_pattern
		self.dir_out = dir_out

	def get_scructur(self, archiv=''):
		meta = ebookmeta.get_metadata(self.booka)
		structura = meta.get_filename_by_pattern(self.dir_pattern, self.author_pattern)
		structura = structura.replace(split_ext(meta.file), '')
		file_name = os.path.basename(meta.file) + '.zip' if archiv else os.path.basename(meta.file)
		d = dict({'full_path': meta.file, 'structura': structura, 'file_name': file_name})
		return d

	def move_src(self):
		full_info_book = self.get_scructur()
		src, struc, f = full_info_book['full_path'], full_info_book['structura'], full_info_book['file_name']
		struc = full_info_book['structura'] if self.use_structur else False
		if struc:
			dst = os.path.normpath(os.path.join(self.finaldir, struc, f))
			if not os.path.exists(dst):
				if not os.path.exists(os.path.dirname(dst)):
					os.makedirs(os.path.dirname(dst))
		else:
			dst = os.path.normpath(os.path.join(self.finaldir, f))
		shutil.move(src, dst)

	def arc_src(self):
		full_info_book = self.get_scructur('True')
		src, struc, f = full_info_book['full_path'], full_info_book['structura'], full_info_book['file_name']
		struc = full_info_book['structura'] if self.use_structur else False
		if struc:
			dst = os.path.normpath(os.path.join(self.finaldir, struc, f))
			if not os.path.exists(dst):
				if not os.path.exists(os.path.dirname(dst)):
					os.makedirs(os.path.dirname(dst))
		else:
			dst = os.path.normpath(os.path.join(self.finaldir, f))
		zip = ZipFile(dst, mode='w', compression=ZIP_DEFLATED)
		zip.write(src, os.path.basename(src))
		zip.close()
		os.remove(full_info_book['full_path'])

	def arc_out(self):
		filelist_out = []
		for root, dir, files in os.walk(self.dir_out):
			files = [file for file in files if file.lower().endswith(('.mobi', '.epub'))]
			for file in files:
				all_data = os.path.normpath(os.path.join(root, file))
				file = os.path.split(all_data)[1]
				filename_out = all_data + '.zip'
				d = dict({'full_input': all_data, 'file_name': file, 'full_file_name_out': filename_out})
				filelist_out.append(d)
		for file in filelist_out:
			zip = ZipFile(file['full_file_name_out'], mode='w', compression=ZIP_DEFLATED)
			zip.write(file['full_input'], file['file_name'])
			zip.close()
			os.remove(file['full_input'])
