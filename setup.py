#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Cabrama - Câmbio no Brasil para Mastodon
Copyright (C) 2020-2022 Vitor Guia

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from setuptools import setup

with open('README.md', 'r') as f:
    README = f.read()

setup(
    name='sepbit.cabrama',
    version='1.1.0',
    description='Câmbio no Brasil para Mastodon',
    long_description=README,
    license='GPL-3.0-or-later',
    keywords='Sepbit câmbio cotação Brasil Mastodon',
    author='Vitor Guia',
    maintainer='Sepbit',
    maintainer_email='contato@sepbit.com',
    author_email='contato@vitor.guia.nom.br',
    url='https://gitlab.com/sepbit/cabrama',
    packages=['sepbit.cabrama'],
    python_requires='~=3.9',
    install_requires=['setuptools', 'sepbit.sistamapy'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    test_suite='test',
    entry_points={
        'console_scripts': [
            'cabrama=sepbit.cabrama.__main__:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 \
        or later (GPLv3+)',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    zip_safe=False,
)
