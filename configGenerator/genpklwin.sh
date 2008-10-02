#!/bin/sh

#VERSION=0.1.1
VERSION=1.0rc2
rm -f -r results/*
#./configGenerator.pl $VERSION win_msklc_azerty | iconv -f utf-8 -t utf-16le > "results/fr-dvorak-bepo-${VERSION}A-kbd.klc"
#./configGenerator.pl $VERSION win_msklc_bepo   | iconv -f utf-8 -t utf-16le > "results/fr-dvorak-bepo-${VERSION}B-kbd.klc"
#./configGenerator.pl $VERSION win_msklc_qwertz | iconv -f utf-8 -t utf-16le > "results/fr-dvorak-bepo-${VERSION}C-kbd.klc"
#./configGenerator.pl $VERSION win_msklc_azerty | iconv -f utf-8 -t utf-16 > "results/fr-dvorak-bepo-${VERSION}A.klc"
./configGenerator.pl $VERSION win_msklc_bepo   | iconv -f utf-8 -t utf-16 > "results/fr-dvorak-bepo-${VERSION}B.klc"
#./configGenerator.pl $VERSION win_msklc_qwertz | iconv -f utf-8 -t utf-16 > "results/fr-dvorak-bepo-${VERSION}C.klc"

perl klc2ini.pl results/fr-dvorak-bepo-${VERSION}B.klc
awk '{print} /\[fingers\]/ {print "methode = aucune"}' < results/layout.ini > results/layout0.ini
mv results/layout0.ini results/layout.ini
perl ini2html.pl results/layout.ini
firefox -savepng "results/layout.html"
#firefox -p screengrab -no-remote -savepng results/layout.html
mv "$HOMEDRIVE$HOMEPATH\Bureau\Image de la page.png" "results/layout.png"
perl split_png.pl
mkdir -p results/pkl/fr-dvorak-bepo-${VERSION}/
rm results/layout.png
mv results/layout.ini results/*.html results/*.png  results/pkl/fr-dvorak-bepo-${VERSION}/

perl klc2ini.pl results/fr-dvorak-bepo-${VERSION}B.klc
awk '{print} /\[fingers\]/ {print "methode = standard\nrow1 = 1123445567888\nrow2 = 112344556788\nrow3 = 112344556788\nrow4 = 11234455678"}' < results/layout.ini > results/layout0.ini
mv results/layout0.ini results/layout.ini
perl ini2html.pl results/layout.ini
firefox -savepng "results/layout.html"
mv "$HOMEDRIVE$HOMEPATH\Bureau\Image de la page.png" "results/layout.png"
perl split_png.pl
mkdir -p results/pkl/fr-dvorak-bepo-${VERSION}-st/
rm results/layout.png results/layout.html
mv results/layout.ini results/*.png  results/pkl/fr-dvorak-bepo-${VERSION}-st/

perl klc2ini.pl results/fr-dvorak-bepo-${VERSION}B.klc
awk '{print} /\[fingers\]/ {print "methode = o0\nrow1 = 1112344556788\nrow2 = 112344556788\nrow3 = 112344556788\nrow4 = 11234455678"}' < results/layout.ini > results/layout0.ini
mv results/layout0.ini results/layout.ini
perl ini2html.pl results/layout.ini
firefox -savepng "results/layout.html"
mv "$HOMEDRIVE$HOMEPATH\Bureau\Image de la page.png" "results/layout.png"
perl split_png.pl
mkdir -p results/pkl/fr-dvorak-bepo-${VERSION}-o0/
rm results/layout.png results/layout.html
mv results/layout.ini results/*.png  results/pkl/fr-dvorak-bepo-${VERSION}-o0/

perl klc2ini.pl results/fr-dvorak-bepo-${VERSION}B.klc
awk '{print} /\[fingers\]/ {print "methode = t6\nrow1 = 1123444567888\nrow2 = 112344556788\nrow3 = 112344556788\nrow4 = 11234455678"}' < results/layout.ini > results/layout0.ini
mv results/layout0.ini results/layout.ini
perl ini2html.pl results/layout.ini
firefox -savepng "results/layout.html"
mv "$HOMEDRIVE$HOMEPATH\Bureau\Image de la page.png" "results/layout.png"
perl split_png.pl
mkdir -p results/pkl/fr-dvorak-bepo-${VERSION}-t6/
rm results/layout.png results/layout.html
mv results/layout.ini results/*.png  results/pkl/fr-dvorak-bepo-${VERSION}-t6/

mv results/pkl/fr-dvorak-bepo-${VERSION}/layout.html results/

#perl klc2ini.pl results/fr-dvorak-bepo-${VERSION}A.klc
#mv results/layout.ini results/layoutA.ini
#perl klc2ini.pl results/fr-dvorak-bepo-${VERSION}C.klc
#mv results/layout.ini results/layoutC.ini