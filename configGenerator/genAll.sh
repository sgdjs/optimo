#!/bin/sh

#VERSION=0.1.1
VERSION=0.6.5.1

./configGenerator.pl $VERSION x_xkb_root > "results/layout-${VERSION}.xkb"
./configGenerator.pl $VERSION x_xkb_user > "results/layout-${VERSION}-user.xkb"
./configGenerator.pl $VERSION x_xmodmap  > "results/layout-${VERSION}.xmodmap"
./configGenerator.pl $VERSION x_compose  > "results/layout-${VERSION}.XCompose"

./configGenerator.pl $VERSION win_msklc_azerty | iconv -f utf-8 -t utf-16 > "results/layout-${VERSION}-vkAzerty.klc"
./configGenerator.pl $VERSION win_msklc_bepo   | iconv -f utf-8 -t utf-16 > "results/layout-${VERSION}-vkBepo.klc"
./configGenerator.pl $VERSION win_msklc_qwertz | iconv -f utf-8 -t utf-16 > "results/layout-${VERSION}-vkQwertz.klc"

./map.py     "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.txt"
./svg.py     "results/layout-${VERSION}.xkb" "results/layout-${VERSION}"
./klavaro.py "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.kbd"
./ktouch.py  "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.keyboard"
./keymaps.py "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.map"
./kbdmap.py  "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.kbdmap"
./wscons.py  "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.wscons"
./macosx.py  "results/layout-${VERSION}.xkb" "results/layout-${VERSION}.keylayout"

perl -p -e 's#\tinclude "pc\(pc105\)"#\tinclude "pc/pc(pc105)"#g' "results/layout-${VERSION}-user.xkb" > "results/layout-${VERSION}-user-legacy.xkb"
