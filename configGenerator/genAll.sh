#!/bin/bash

#VERSION=0.1.1
VERSION=0.6.5.1

./configGenerator.pl $VERSION x_xkb                                > "results/layout-${VERSION}.xkb"
./configGenerator.pl $VERSION x_xmodmap                            > "results/layout-${VERSION}.xmodmap"
./configGenerator.pl $VERSION x_compose                            > "results/layout-${VERSION}.XCompose"
./configGenerator.pl $VERSION win_msklc | iconv -f utf-8 -t utf-16 > "results/layout-${VERSION}.klc"
