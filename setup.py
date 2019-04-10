from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='mkpdfs-mkdocs',
    version='1.0.0',
    url='https://mkpdfs.comwes.eu',
    license='GPLv3',
    license_file="LICENSE",
    author='Comwes, Ntabuhashe Gerard',
    author_email='contact@comwes.eu',
    description='Allows the generation of the PDF version of your MkDocs documentation.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.4',
    install_requires=[
        'mkdocs>=0.17',
        'weasyprint>=0.44',
        'beautifulsoup4>=4.6.3'
    ],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/comwes/mkpdfs-mkdocs-plugin/issues',
        'Say Thanks!': 'http://saythanks.io/to/comwes',
        'Source': 'https://github.com/comwes/mkpdfs-mkdocs-plugin',
    },
    keywords='mkdocs documentation pdf export weasyprint markdown plugin',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Topic :: Documentation',
        'Topic :: Printing',
        'Programming Language :: Other',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),

    entry_points={
        'mkdocs.plugins': [
            'mkpdfs = mkpdfs_mkdocs:Mkpdfs',
        ]
    },
    zip_safe=False,
)
