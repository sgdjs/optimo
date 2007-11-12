#!/bin/sh

OUT=$PWD
VERSION=$1

mkdir tmp
pushd tmp

svn export svn://svn.tuxfamily.org/svnroot/dvorak/svn/pilotes/trunk pilotes
pushd pilotes/macosx

python generate_alt.py
rm -f generate_alt.py devel.txt
cp ../CC-SA-BY.txt ../GFDL.txt  .
hdiutil create $OUT/fr-dvorak-bepo-$VERSION.dmg \
  -ov \
  -srcdir . \
  -volname "fr-dvorak-bépo ($VERSION)"

popd
popd
rm -rf tmp