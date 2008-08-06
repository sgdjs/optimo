#!/bin/sh

#VERSION=0.1.1
VERSION=1.0rc1

./configGenerator.pl $VERSION x_xkb_root > "results/layout-${VERSION}.xkb"
./configGenerator.pl $VERSION x_xkb_user > "results/layout-${VERSION}-user.xkb"
./configGenerator.pl $VERSION x_xmodmap  > "results/layout-${VERSION}.xmodmap"
./configGenerator.pl $VERSION x_compose  > "results/layout-${VERSION}.XCompose"

#Fichiers pour Windows
./configGenerator.pl $VERSION win_msklc_azerty | iconv -f utf-8 -t utf-16le > "results/fr-dvorak-bepo-${VERSION}A-kbd.klc"
./configGenerator.pl $VERSION win_msklc_bepo   | iconv -f utf-8 -t utf-16le > "results/fr-dvorak-bepo-${VERSION}B-kbd.klc"
./configGenerator.pl $VERSION win_msklc_qwertz | iconv -f utf-8 -t utf-16le > "results/fr-dvorak-bepo-${VERSION}C-kbd.klc"
./configGenerator.pl $VERSION win_msklc_azerty | iconv -f utf-8 -t utf-16 > "results/fr-dvorak-bepo-${VERSION}A.klc"
./configGenerator.pl $VERSION win_msklc_bepo   | iconv -f utf-8 -t utf-16 > "results/fr-dvorak-bepo-${VERSION}B.klc"
./configGenerator.pl $VERSION win_msklc_qwertz | iconv -f utf-8 -t utf-16 > "results/fr-dvorak-bepo-${VERSION}C.klc"
perl klc2ini.pl results/fr-dvorak-bepo-${VERSION}B.klc
perl ini2html.pl results/layout.ini
mv results/layout.ini results/layoutB.ini
perl klc2ini.pl results/fr-dvorak-bepo-${VERSION}A.klc
mv results/layout.ini results/layoutA.ini
perl klc2ini.pl results/fr-dvorak-bepo-${VERSION}C.klc
mv results/layout.ini results/layoutC.ini

./map.py         "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.txt"
./svg.py         "results/layout-${VERSION}.xkb" "results/fr-dvorak-bepo-${VERSION}"
./klavaro.py     "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.kbd"
./ktouch.py      "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.keyboard"
./typefaster.py  "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.xml"
./keymaps.py     "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.map"
./kbdmap.py      "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.kbdmap"
./wscons.py      "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.wscons"
./macosx.py      "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.keylayout"

perl -p -e 's#\tinclude "pc\(pc105\)"#\tinclude "pc/pc(pc105)"#g' "results/layout-${VERSION}-user.xkb" > "results/layout-${VERSION}-user-legacy.xkb"
