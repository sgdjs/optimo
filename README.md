# Optimo Keyboard Layout

The Optimo layout is a fork of the [bepo](http://bepo.fr) layout adapted
to the reduced format (40%) of the Planck Keyboard:

* New position of M, W and Z
* Direct access to ´ (dead acute), better access to \` (dead grave)
* Reverse ) and +
* Developer oriented changes:
  * < and > in direct access, reversed with « and »
  * \_ and \[EFI\] (Narrow No-Break SPace) on liberated W key, space only space

## Planck

Optimized layout for the Optimo Planck keyboard. 

![Otimp](optimp/bepo-Optimp.png)

## Ortholinear

Optimized layout for orthogonal keyboards of 104 keys

![Image](optimo/bepo-Optimo.png)

## Optima

Optimized layout with A fingers position, for staggered ISO keyboards

![Image](optima/bepo-Optima.png)

## Development

Optimo is open to new ideas:

* Improved access to [ and ] (Ç deserves a dead key)
* Reverse back ) and + for optima
* Numbers optimized for strong fingers (Optimo only)
* Symetry, improved access to ,

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
