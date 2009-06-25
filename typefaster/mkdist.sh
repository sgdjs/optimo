#!/bin/sh -x
#
# Génération de l'archive contenant le pilote de clavier bépo
#
# Copyright (C) 2008 Gaëtan Lehmann <gaetan.lehmann@jouy.inra.fr>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#

set -ev

# store the current dir. The image will be stored here.
OUT=$PWD
VERSION=$1

if [ -z "$VERSION" ]
then
  echo "il faut un numéro de version"
  exit 1
fi


# make a temp dir to create the... temp files
mkdir tmp
pushd tmp

# get the last version
svn export svn://svn.tuxfamily.org/svnroot/dvorak/svn/pilotes/trunk pilotes
mkdir bepo-typefaster-$VERSION

# copy the licenses
cp pilotes/CC-SA-BY.txt pilotes/GFDL.txt bepo-typefaster-$VERSION

# copy the drivers and the readmes
cp pilotes/typefaster/bepo* pilotes/typefaster/LISEZ_MOI.txt bepo-typefaster-$VERSION

# build the archive
zip -r ../bepo-typefaster-$VERSION.zip bepo-typefaster-$VERSION

popd

# and remove the temp dir
rm -rf tmp
