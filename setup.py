import os

from codecs import open
from setuptools import setup

from sphinx.setup_command import BuildDoc

try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser

CONF = ConfigParser()

HERE = os.path.abspath(os.path.dirname(__file__))


def create_version_py(packagename, version, source_dir='.'):
    package_dir = os.path.join(source_dir, packagename)
    version_py = os.path.join(package_dir, 'version.py')

    version_str = "# This is an automatic generated file please do not edit\n" \
                  "__version__ = '{:s}'".format(version)

    with open(version_py, 'w') as f:
        f.write(version_str)


# read content from README.md
with open(os.path.join(HERE, 'README.md')) as f:
    long_description = f.read()

CONF.read([os.path.join(os.path.dirname(__file__), 'setup.cfg')])

metadata = dict(CONF.items('metadata'))

PACKAGENAME = metadata['package_name']

VERSION = metadata['version']

LICENSE = metadata['license']

DESCRIPTION = metadata['description']

LONG_DESCRIPTION = long_description

LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

AUTHOR = metadata['author']

AUTHOR_EMAIL = metadata['author_email']

# freezes version information in version.py
create_version_py(PACKAGENAME, VERSION)


cmdclassd = {'build_sphinx': BuildDoc,
             'build_docs': BuildDoc}

setup(
    name=metadata['package_name'],

    version=VERSION,

    description=DESCRIPTION,

    long_description=LONG_DESCRIPTION,

    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,

    # The project's main homepage.
    url='https://github.com/soar-telescope/goodman_focus',

    # Author details
    author=u'Simon Torres R., ',

    author_email='storres@ctio.noao.edu',

    cmdclass=cmdclassd,

    # Choose your license
    license=LICENSE,

    packages=['goodman_focus'],

    package_dir={'goodman_focus': 'goodman_focus'},

)
