"""
File to make auto-documentation with Sphinx
"""
import sphinx
import sphinx.quickstart
import sphinx.apidoc


def configure_doc():
    """Function to configure auto-documentation"""
    sphinx.quickstart.main(['sphinx-quickstart'])


def genere_doc():
    """Function to genere auto-documentation"""
    sphinx.apidoc.main(['sphinx-apidoc', '-f', '--output-dir=doc/generated', './'])
    sphinx.main(['sphinx-build', '-b', 'html', 'doc', 'doc/_build/html'])
