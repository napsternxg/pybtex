# Copyright 2006 Andrey Golovizin
#
# This file is part of pybtex.
#
# pybtex is free software; you can redistribute it and/or modify
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# pybtex is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rdiff-backup; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA

from pybtex.backends import BackendBase
import codecs

file_extension = 'txt'

class Writer(BackendBase):
    symbols = {
        'ndash': '-',
        'newblock': '',
        'nbsp': ' '
    }
    
    def format_tag(self, tag_name, text):
        return text
    
    def write_item(self, entry):
    	self.output("[%s] " % entry.label)
        self.output(entry.text.render(self))
	self.output('\n')