BibTeX-compatible bibliography processor in Python
==================================================

Synopsis
--------

::

    latex foo.tex
    pybtex foo.aux
    latex foo.tex
    latex foo.tex


Description
-----------

Pybtex reads citation information from a file and
produces a formatted bibliography. BibTeX style files are supported.
Alternatively it is possible to write styles in Python.

Pybtex currently understands the following bibliography formats:

- BibTeX

- BibTeXML

- YAML-based format

The resulting bibliography may be output in one of the following formats
(not supported by legacy BibTeX styles):

- LaTeX

- HTML

- markdown

- plain text


See also
--------

- `Home page <https://pybtex.org/>`_

- `Pybtex at Bitbucket <https://bitbucket.org/pybtex-devs/pybtex>`_

- `Pybtex at PyPI <https://pypi.python.org/pypi/pybtex>`_
