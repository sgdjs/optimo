REM Batch à lancer dans ...\msklc\bin\i386\ avec les 6 fichiers .klc
REM Il génère les fichiers dlls avec kbdutool.exe
REM Penser à modificer le numéro de version (set ver=...)
REM Le nom de la dll est en dos 8.3 donc le nom de version est abrégé en rc2x
REM Il faut ensuite faire les fichiers d'installation avec msklc
REM (Attention a bien garder le même nom de dll.)
@echo off
set ver=
md bepo%ver%a
md bepo%ver%
md bepo%ver%c
cd bepo%ver%a
md amd64
md i386
md ia64
md sources
md wow64
cd..
cd bepo%ver%
md amd64
md i386
md ia64
md sources
md wow64
cd..
cd bepo%ver%c
md amd64
md i386
md ia64
md sources
md wow64
cd..
copy bepo-%ver%a.klc bepo%ver%a.klc
kbdutool.exe -u -s bepo-%ver%A-kbd.klc
move /y bepo%ver%a.* bepo%ver%a/sources/
kbdutool.exe -u -x bepo-%ver%A-kbd.klc
move /y bepo%ver%a.dll bepo%ver%a/i386/
kbdutool.exe -u -i bepo-%ver%A-kbd.klc
move /y bepo%ver%a.dll bepo%ver%a/ia64/
kbdutool.exe -u -m bepo-%ver%A-kbd.klc
move /y bepo%ver%a.dll bepo%ver%a/amd64/
kbdutool.exe -u -o bepo-%ver%A-kbd.klc
move /y bepo%ver%a.dll bepo%ver%a/wow64/
copy bepo-%ver%b.klc bepo%ver%.klc
kbdutool.exe -u -s bepo-%ver%B-kbd.klc
move /y bepo%ver%.* bepo%ver%/sources/
kbdutool.exe -u -x bepo-%ver%B-kbd.klc
move /y bepo%ver%.dll bepo%ver%/i386/
kbdutool.exe -u -i bepo-%ver%B-kbd.klc
move /y bepo%ver%.dll bepo%ver%/ia64/
kbdutool.exe -u -m bepo-%ver%B-kbd.klc
move /y bepo%ver%.dll bepo%ver%/amd64/
kbdutool.exe -u -o bepo-%ver%B-kbd.klc
move /y bepo%ver%.dll bepo%ver%/wow64/
copy bepo-%ver%c.klc bepo%ver%c.klc
kbdutool.exe -u -s bepo-%ver%C-kbd.klc
move /y bepo%ver%c.* bepo%ver%c/sources/
kbdutool.exe -u -x bepo-%ver%C-kbd.klc
move /y bepo%ver%c.dll bepo%ver%c/i386/
kbdutool.exe -u -i bepo-%ver%C-kbd.klc
move /y bepo%ver%c.dll bepo%ver%c/ia64/
kbdutool.exe -u -m bepo-%ver%C-kbd.klc
move /y bepo%ver%c.dll bepo%ver%c/amd64/
kbdutool.exe -u -o bepo-%ver%C-kbd.klc
move /y bepo%ver%c.dll bepo%ver%c/wow64/