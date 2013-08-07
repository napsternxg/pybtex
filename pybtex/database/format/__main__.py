#!/usr/bin/env python

# Copyright (c) 2013  Andrey Golovizin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from pybtex.cmdline import CommandLine, make_option, standard_option

class PybtexFormatCommandLine(CommandLine):
    prog = 'pybtex-format'
    args = '[options] in_filename out_filename'
    description = 'convert between bibliography database formats'
    long_description = """

pybtex-format formats bibliography database as human-readable text.
    """.strip()
    num_args = 2

    options = (
        (None, (
            make_option(
                '-f', '--from', dest='from_format',
                help='input format (%plugin_choices)', metavar='FORMAT',
                type='load_plugin', plugin_group='pybtex.database.input',
            ),
            standard_option('output_backend'),
            standard_option('min_crossrefs'),
            standard_option('keyless_entries'),
        )),
        ('encoding options', (
            standard_option('encoding'),
            standard_option('input_encoding'),
            standard_option('output_encoding'),
        )),
    )
    option_defaults = {
        'keyless_entries': False,
    }

    def run(self, options, args):
        from pybtex.database.format import format_database

        format_database(args[0], args[1],
                options.from_format,
                options.output_backend,
                input_encoding=options.input_encoding or options.encoding,
                output_encoding=options.output_encoding or options.encoding,
                parser_options = {'keyless_entries': options.keyless_entries},
                min_crossrefs=options.min_crossrefs
        )


main = PybtexFormatCommandLine()


if __name__ == '__main__':
    main()