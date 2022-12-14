#!/usr/bin/env python3

#    Copyright (C) 2022  crazy-catzzz
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name='may_browse',
    version="0.1.0dev",
    packages=['may_browse'],
    author="crazy-catzzz",
    license="AGPLv3",
    install_requires=install_requires,
    entry_points={
        'gui_scripts': [
            'may-browse=may_browse.maybrowse:main',
        ]
    }
)