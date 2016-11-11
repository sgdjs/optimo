REM Batch à lancer dans ...\msklc\bin\i386\ avec les 6 fichiers .klc
REM Il génère les fichiers dlls avec kbdutool.exe
REM Penser à modificer le numéro de version (set ver=...)
REM Le nom de la dll est en dos 8.3 donc le nom de version est abrégé en rc2x
REM Il faut ensuite faire les fichiers d'installation avec msklc
REM (Attention a bien garder le même nom de dll.)
@echo off
set ver=Optima
md bepo%ver%b
cd bepo%ver%b
md amd64
md i386
md ia64
md sources
md wow64

copy bepo-%ver%B.klc bepo%ver%b.klc
kbdutool.exe -u -s bepo-%ver%B-kbd.klc
move /y bepo%ver%b.klc bepo%ver%b/sources/
move /y bepo*.* bepo%ver%b/sources/
kbdutool.exe -u -x bepo-%ver%B-kbd.klc
move /y bepo*.dll bepo%ver%b/i386/
kbdutool.exe -u -i bepo-%ver%B-kbd.klc
move /y bepo*.dll bepo%ver%b/ia64/
kbdutool.exe -u -m bepo-%ver%B-kbd.klc
move /y bepo*.dll bepo%ver%b/amd64/
kbdutool.exe -u -o bepo-%ver%B-kbd.klc
move /y bepo*.dll bepo%ver%b/wow64/
