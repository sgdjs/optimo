# Sgdjs’ Optimo Keyboard Layouts

The Optimo layout is a fork of the [bepo](bepo.fr) keyboard layout with:

* Better availability of W and Z
* Direct access to ´ (dead acute), better access to \` (dead grave)
* Developer oriented changes:
  * < and > in direct access, reversed with « and »
  * \_ and [EFI] (Narrow No-Break SPace) on liberated W key, space only space

## Optimo

Optimized layout for orthogonal keyboards of 104 keys

![Image](optimo/bepo-Optimo.png)

## Optima

Optimized layout with A fingers position, for staggered ISO keyboards

![Image](optima/bepo-Optima.png)

## Development

Optimo is still a work in progress. Ideas:

* The liberated Z key could be better used
* = could be easier access, and also %
* ´ (dead acute/grave key) could be changed with K
* Improved access to [ and ] (Ç deserves a dead key)
* Improved access to ( and ), and re-thinking the numbers row for symetry
* Numbers optimized for strong fingers (Optimo only)
* Symetry, improved access to ,
* An improved Planck keyboard would require to move M (to ' ?)

## Installation (Mac and Windows)

### MacOS

Copy the keylayout file in the root or user library, like the ./mac-copy.sh
script does.

### Windows

Unzip the file attached to the tag and launch setup.exe, or do the
manual method:

Download and install the [Microsoft Keyboard Layout Creator](https://msdn.microsoft.com/en-us/globalization/keyboardlayouts)

* Open the file bepo-OptimoB.klc with MKLC.
* Generate the DLL and install program wherever
* Lauch setup.exe

## More

The bepo.fr branch is set to track https://git.tuxfamily.org/dvorak/pilotes.git

Instructions for the tools (French link): http://bepo.fr/wiki/ConfigGenerator
