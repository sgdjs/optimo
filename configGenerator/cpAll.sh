#!/bin/sh

#VERSION=0.1.1
VERSION=1.0rc3


cp "results/layout-${VERSION}-user.xkb" ../xkb/fr-dvorak-bepo.xkb
cp "results/layout-${VERSION}-user-legacy.xkb" ../xkb/fr-dvorak-bepo-xorglegacy.xkb
cp "results/layout-${VERSION}.XCompose" ../xkb/XCompose

cp "results/fr-dvorak-bepo-${VERSION}A.klc" ../windows/fr-dvorak-bepo-azerty.klc
cp "results/fr-dvorak-bepo-${VERSION}B.klc" ../windows/fr-dvorak-bepo.klc
cp "results/fr-dvorak-bepo-${VERSION}C.klc" ../windows/fr-dvorak-bepo-qwertz.klc
cp "results/layout-${VERSION}.kbd" ../klavaro/fr-dvorak-bepo.kbd
cp "results/layout-${VERSION}.keyboard" ../ktouch/fr-dvorak-bepo.keyboard
cp "results/layout-${VERSION}.xml" ../typefaster/fr-dvorak-bepo.xml
cp "results/layout-${VERSION}.map" ../keymaps/fr-dvorak-bepo.map
cp "results/layout-${VERSION}.kbdmap" ../kbdmap/fr-dvorak-bepo.kbd
cp "results/layout-${VERSION}.wscons" ../wscons/fr-dvorak-bepo.map
cp "results/layout-${VERSION}.keylayout" ../macosx/fr-dvorak-bepo.bundle/Contents/Resources/fr-dvorak-bepo.keylayout
