"""
Created on Mon Jun 02 14:38:30 2014

@author: Dorian
"""
import sphinx
import sphinx.quickstart
import sphinx.apidoc


def configure_doc():
    sphinx.quickstart.main(['sphinx-quickstart'])


def genere_doc():
    sphinx.apidoc.main(['sphinx-apidoc', '-f', '--output-dir=doc/generated', './'])
    sphinx.main(['sphinx-build', '-b', 'html', 'doc', 'doc/_build/html'])
