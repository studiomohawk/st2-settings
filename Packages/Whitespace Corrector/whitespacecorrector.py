'''
Whitespace Corrector
Licensed under MIT
Copyright (c) 2011 Zhomart <mzhomart@gmail.com>
'''

import sublime, sublime_plugin, re
from sublime import *

class WhitespacecorrectorCommand(sublime_plugin.TextCommand):
	def replace_by_tab(self, tab_size):
		v = self.view
		out = []
		if not tab_size.isdigit(): return
		tab_size = int(tab_size.strip(), 10)
		for l_re in v.lines(Region(0, v.size())):
			line = v.substr(l_re)
			new_line = re.sub('\ {%d}' % tab_size, '\t', line)
			out.append(new_line.rstrip())
		v.replace(self.edit, Region(0, v.size()), '\n'.join(out))


	def run(self, edit):
		self.edit = edit
		self.view.window().show_input_panel('Enter Tab Size', '4', self.replace_by_tab, None, None)
