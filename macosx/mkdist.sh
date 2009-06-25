#!/bin/sh -x
#
# Génération du dmg contenant le pilote de clavier bépo
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
pushd pilotes/macosx

rm -f "$OUT/bepo-macosx-$VERSION.dmg"
hdiutil create "$OUT/tmp/bepo-macosx-$VERSION.dmg" -size 13m -fs HFS+ -volname "bépo ($VERSION)"
dev_handle=`hdiutil mount "$OUT/tmp/bepo-macosx-$VERSION.dmg" | egrep "/b.+po \(.+\)" | cut -f 1`

# generate the alt confs
python generate_alt.py

# use the icon for the volume
ditto -rsrcFork bepo.icns "/Volumes/bépo ($VERSION)/.VolumeIcon.icns"
/Developer/Tools/SetFile -a C "/Volumes/bépo ($VERSION)"

# set the icon for the bundle
SetCustomIcon bepo.bundle bepo.icns

# copy tho licenses
cp ../CC-SA-BY.txt ../GFDL.txt  "/Volumes/bépo ($VERSION)"

# copy the bundle and the readmes
cp -R bepo.bundle LISEZ_MOI.txt READ_ME.txt "/Volumes/bépo ($VERSION)"

hdiutil detach $dev_handle
hdiutil convert -imagekey zlib-level=9 -format UDZO "$OUT/tmp/bepo-macosx-$VERSION.dmg" -o "$OUT/bepo-macosx-$VERSION.dmg"

popd
popd
# and remove the temp dir
rm -rf tmp
