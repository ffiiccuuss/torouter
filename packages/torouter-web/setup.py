#!/usr/bin/env python
from distutils.core import setup

setup(name='torouter-tui',
      packages=['tui'],
      package_dir = {'tui': 'src/tui/'},
      package_data = {'tui': ['src/static']},
      version='0.1',
      description='Torouter Web UI',
      author='Arturo Filasto',
      author_email='hellais@torproject.org',
      url='https://www.torproject.org/',
      scripts=['src/runui.py', 'src/view.py', 'src/config.py'])

