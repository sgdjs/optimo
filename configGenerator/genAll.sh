#!/bin/bash

#VERSION=0.1.1
VERSION=0.6.5.1
LAYOUT=layout-${VERSION}.conf
DEADS=deads-${VERSION}.conf

./configGenerator.pl "$LAYOUT" "$DEADS" x_xkb > ${LAYOUT/conf/xkb}
./configGenerator.pl "$LAYOUT" "$DEADS" x_xmodmap > ${LAYOUT/conf/xmodmap}
./configGenerator.pl "$LAYOUT" "$DEADS" win_msklc | iconv -f utf-8 -t utf-16 > "${LAYOUT/conf/klc}"
