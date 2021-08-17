#!/usr/bin/env python3
# Copyright Aaron Whitehouse 2021
#
# This lists all packages from the Ubuntu universe repository
# To use, simply download/copy into a .py file and run with:
# python3 list_universe.py
#
# If you receive an import error, you may need to install python3-apt first with e.g.
# sudo apt install python3-apt python3-distro
# but this is often not necessary
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import apt  # python3-apt in Ubuntu
import distro  # python3-distro in Ubuntu

if distro.name() == "Ubuntu":
    cache = apt.Cache()
    package_count = 0

    for package in cache:
        if (
            package.is_installed
            and package.candidate.origins[0].origin == "Ubuntu"
            and package.candidate.origins[0].component == "universe"
        ):
            package_origin = package.candidate.origins[0]
            print(
                package.name,
                # See https://apt-team.pages.debian.net/python-apt/library/apt.package.html#apt.package.Origin
                # for further details on the meanings of the below
                package_origin.origin,  # The Origin, as set in the Release file
                package_origin.archive,  # The archive (eg. Ubuntu release name)
                package_origin.component,  # The component (eg. main/universe)
                # package_origin.site,  # The hostname of the site.
                # package_origin.label,  # The Label, as set in the Release file
                # package_origin.trusted,  # Origin trusted (Release file signed by key in apt keyring)
            )
            package_count += 1

    print(package_count, "packages from Ubuntu universe")
else:
    print("Sorry, this script is only designed to work on Ubuntu.")
