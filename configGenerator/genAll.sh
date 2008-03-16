#!/bin/bash

#VERSION=0.1.1
VERSION=0.6.5.1

./configGenerator.pl $VERSION x_xkb                                > "layout-${VERSION}.xkb"
./configGenerator.pl $VERSION x_xmodmap                            > "layout-${VERSION}.xmodmap"
./configGenerator.pl $VERSION x_compose                            > "layout-${VERSION}.XCompose"
./configGenerator.pl $VERSION win_msklc | iconv -f utf-8 -t utf-16 > "layout-${VERSION}.klc"
