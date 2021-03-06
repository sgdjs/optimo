# Optimo Keyboard Layout

The Optimo layout is a fork of the [bepo](http://bepo.fr) layout. 
It comes in three variants:

* [Optimo](#optimo): for ANSI keyboards (104 keys) 
* [Optima](#optima): for ISO keyboard (105 keys)
* [OptimoP](#optimop): for Planck Keyboard (40%)

## Features

* New position of M, W and Z
* Direct access to ´ (dead acute), shift access to \` (dead grave)

* Developer oriented changes:
  * Direct access to numbers (since version
    [1.7](https://github.com/sgdjs/optimo/releases/tag/1.7))
  * < and > in shift access, « and » in alt-gr
  * \ { } \_ ; : ? ! and no-break space on new positions

## Optimo

Layout for orthogonal or staggered keyboards of 104 keys

![Image](optimo/bepo-Optimo.png)

## Optima 

Layout for ISO keyboards of 105 keys 

![Image](optima/bepo-Optima.png)

## OptimoP

Optimo layout for the Planck keyboard (firmware [here](https://github.com/sgdjs/qmk_firmware/tree/optimo/keyboards/planck/keymaps/optimo))

**Special Feature**: optimized line of numbers and symbols

![Otimp](optimp/bepo-Optimp.png)

# Installation (Mac and Windows)

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

# More

The bepo.fr branch is set to track https://git.tuxfamily.org/dvorak/pilotes.git

Instructions for the tools (French link): http://bepo.fr/wiki/ConfigGenerator

This readme in French [here](LISEZMOI.md)
