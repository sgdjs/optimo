#!/bin/sh

# store the current dir. The image will be stored here.
OUT=$PWD
VERSION=$1

# make a temp dir to create the... temp files
mkdir tmp
pushd tmp

# get the last version
svn export svn://svn.tuxfamily.org/svnroot/dvorak/svn/pilotes/trunk pilotes
pushd pilotes/macosx

# generate the alt confs
python generate_alt.py

# remove the devel files
rm -f generate_alt.py devel.txt mkdmg.sh 

# copy tho licenses
cp ../CC-SA-BY.txt ../GFDL.txt  .

# create the image
hdiutil create $OUT/fr-dvorak-bepo-macosx-$VERSION.dmg \
  -ov \
  -srcdir . \
  -volname "fr-dvorak-bépo ($VERSION)"

popd
popd
# and remove the temp dir
rm -rf tmp
