import codecs
import json
import os
import sys
from types import SimpleNamespace

if sys.platform == 'win32':
	config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config')
else:
	config_path = os.path.join(os.path.expanduser('~'), '.Fb2Tool', 'config')

config_mark_file = os.path.join(config_path, 'markread.json')

settings = SimpleNamespace(
	ui_path_bases_collapsed=False,
	ui_query_bases_collapsed=False,
	ui_backup_bases_collapsed=False,
	check_Myhomelib=False,
	myhomelib=None,
	check_Calibre=False,
	calibre=None,
	search_base=None,
	search=None,
	mark_myhomelib=None,
	mark_calibre={},
	create_backup=False,
	location_backup=None,
	count_backup=0
)
new_simple = SimpleNamespace(
	ui_path_bases_collapsed=False,
	ui_query_bases_collapsed=False,
	ui_backup_bases_collapsed=False,
	check_Myhomelib=False,
	myhomelib=None,
	check_Calibre=False,
	calibre=None,
	search_base=None,
	search=None,
	mark_myhomelib=None,
	mark_calibre={},
	create_backup=False,
	location_backup=None,
	count_backup=0
)
new = settings.__dict__.copy()


def init():
	d = None
	if not os.path.exists(config_path):
		os.makedirs(config_path)
	if not os.path.exists(config_mark_file):
		d = {'MarkRead': settings.__dict__}
		with codecs.open(config_mark_file, 'w', encoding='utf-8') as f:
			f.write(json.dumps(d, sort_keys=False, indent=4))


def save(flag, profile):
	with codecs.open(config_mark_file, 'r', encoding='utf-8') as f:
		c = json.loads(f.read())
	if flag == 'new':
		for key in c[profile]:
			c[profile][key] = new_simple.__dict__[key]
	else:
		for key in c[profile]:
			c[profile][key] = settings.__dict__[key]
	with codecs.open(config_mark_file, 'w', encoding='utf-8') as f:
		f.write(json.dumps(c, sort_keys=False, indent=4))


def load(profile=None):
	with codecs.open(config_mark_file, 'r', encoding='utf-8') as f:
		c = json.loads(f.read())
	if not profile:
		profile = 'MarkRead'
	for key in c[profile]:
		settings.__dict__[key] = c[profile][key]


def read_confs():
	with codecs.open(config_mark_file, 'r', encoding='utf-8') as f:
		c = json.loads(f.read())
	return c


def add_conf(profile):
	with codecs.open(config_mark_file, 'r', encoding='utf-8') as f:
		c = json.loads(f.read())
	d = {profile: new}
	c.update(d)
	with codecs.open(config_mark_file, 'w', encoding='utf-8') as f:
		f.write(json.dumps(c, sort_keys=False, indent=4))


def remove_conf(dump):
	with codecs.open(config_mark_file, 'w', encoding='utf-8') as f:
		f.write(json.dumps(dump, sort_keys=False, indent=4))
