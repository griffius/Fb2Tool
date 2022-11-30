import os
import json
import codecs
import sys
from types import SimpleNamespace

if sys.platform == 'win32':
	config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config')
else:
	config_path = os.path.join(os.path.expanduser('~'), '.Fb2Tool', 'config')

config_mark_file = os.path.join(config_path, 'markread.json')

settings = SimpleNamespace(
	check_Myhomelib=False,
	myhomelib=None,
	check_Calibre=False,
	calibre=None,
	search_base=None,
	search=None,
	mark_myhomelib=None,
	mark_calibre=None
)


def init():
	if not os.path.exists(config_path):
		os.makedirs(config_path)


def save():
	(config_dir, _) = os.path.split(config_mark_file)
	if not os.path.exists(config_dir):
		os.makedirs(config_dir)
	with codecs.open(config_mark_file, 'w', encoding='utf-8') as f:
		f.write(json.dumps(settings.__dict__, sort_keys=False, indent=4))


def load():
	if not os.path.exists(config_path):
		os.makedirs(config_path)

	if os.path.exists(config_mark_file):
		with codecs.open(config_mark_file, 'r', encoding='utf-8') as f:
			c = json.loads(f.read())

		for key in c:
			settings.__dict__[key] = c[key]
