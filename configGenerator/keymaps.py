#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Produit une carte de touches à partir d'un fichier xkb
#
# Copyright (C) 2008 Gaëtan Lehmann <gaetan.lehmann@jouy.inra.fr>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#

import defaults, sys
defaults.xkbFile = sys.argv[1]

import xkb, dead_keys, codecs
from terminators import terminators


fullMapTmpl = keyboardTemplate = u"""# fr-dvorak-bepo  http://www.clavier-dvorak.org
charset "iso-8859-15"
keymaps 0-3,4-6,8,12
include "linux-with-alt-and-altgr"
strings as usual
compose as usual for "iso-8859-1"


keycode 41 = %(TLDE)s %(TLDE_shift)s %(TLDE_option)s %(TLDE_shift_option)s
keycode  2 = %(AE01)s %(AE01_shift)s %(AE01_option)s %(AE01_shift_option)s
keycode  3 = %(AE02)s %(AE02_shift)s %(AE02_option)s %(AE02_shift_option)s
keycode  4 = %(AE03)s %(AE03_shift)s %(AE03_option)s %(AE03_shift_option)s
keycode  5 = %(AE04)s %(AE04_shift)s %(AE04_option)s %(AE04_shift_option)s
keycode  6 = %(AE05)s %(AE05_shift)s %(AE05_option)s %(AE05_shift_option)s
keycode  7 = %(AE06)s %(AE06_shift)s %(AE06_option)s %(AE06_shift_option)s
keycode  8 = %(AE07)s %(AE07_shift)s %(AE07_option)s %(AE07_shift_option)s
keycode  9 = %(AE08)s %(AE08_shift)s %(AE08_option)s %(AE08_shift_option)s
keycode 10 = %(AE09)s %(AE09_shift)s %(AE09_option)s %(AE09_shift_option)s
keycode 11 = %(AE10)s %(AE10_shift)s %(AE10_option)s %(AE10_shift_option)s
keycode 12 = %(AE11)s %(AE11_shift)s %(AE11_option)s %(AE11_shift_option)s
keycode 13 = %(AE12)s %(AE12_shift)s %(AE12_option)s %(AE12_shift_option)s
# 
keycode 16 = %(AD01)s %(AD01_shift)s %(AD01_option)s %(AD01_shift_option)s
keycode 17 = %(AD02)s %(AD02_shift)s %(AD02_option)s %(AD02_shift_option)s
keycode 18 = %(AD03)s %(AD03_shift)s %(AD03_option)s %(AD03_shift_option)s
keycode 19 = %(AD04)s %(AD04_shift)s %(AD04_option)s %(AD04_shift_option)s
keycode 20 = %(AD05)s %(AD05_shift)s %(AD05_option)s %(AD05_shift_option)s
keycode 21 = %(AD06)s %(AD06_shift)s %(AD06_option)s %(AD06_shift_option)s
keycode 22 = %(AD07)s %(AD07_shift)s %(AD07_option)s %(AD07_shift_option)s
keycode 23 = %(AD08)s %(AD08_shift)s %(AD08_option)s %(AD08_shift_option)s
keycode 24 = %(AD09)s %(AD09_shift)s %(AD09_option)s %(AD09_shift_option)s
keycode 25 = %(AD10)s %(AD10_shift)s %(AD10_option)s %(AD10_shift_option)s
keycode 26 = %(AD11)s %(AD11_shift)s %(AD11_option)s %(AD11_shift_option)s
keycode 27 = %(AD12)s %(AD12_shift)s %(AD12_option)s %(AD12_shift_option)s
#
keycode 30 = %(AC01)s %(AC01_shift)s %(AC01_option)s %(AC01_shift_option)s
keycode 31 = %(AC02)s %(AC02_shift)s %(AC02_option)s %(AC02_shift_option)s
keycode 32 = %(AC03)s %(AC03_shift)s %(AC03_option)s %(AC03_shift_option)s
keycode 33 = %(AC04)s %(AC04_shift)s %(AC04_option)s %(AC04_shift_option)s
keycode 34 = %(AC05)s %(AC05_shift)s %(AC05_option)s %(AC05_shift_option)s
keycode 35 = %(AC06)s %(AC06_shift)s %(AC06_option)s %(AC06_shift_option)s
keycode 36 = %(AC07)s %(AC07_shift)s %(AC07_option)s %(AC07_shift_option)s
keycode 37 = %(AC08)s %(AC08_shift)s %(AC08_option)s %(AC08_shift_option)s
keycode 38 = %(AC09)s %(AC09_shift)s %(AC09_option)s %(AC09_shift_option)s
keycode 39 = %(AC10)s %(AC10_shift)s %(AC10_option)s %(AC10_shift_option)s
keycode 40 = %(AC11)s %(AC11_shift)s %(AC11_option)s %(AC11_shift_option)s
keycode 43 = %(BKSL)s %(BKSL_shift)s %(BKSL_option)s %(BKSL_shift_option)s
#
keycode 86 = %(LSGT)s %(LSGT_shift)s %(LSGT_option)s %(LSGT_shift_option)s
keycode 44 = %(AB01)s %(AB01_shift)s %(AB01_option)s %(AB01_shift_option)s
keycode 45 = %(AB02)s %(AB02_shift)s %(AB02_option)s %(AB02_shift_option)s
keycode 46 = %(AB03)s %(AB03_shift)s %(AB03_option)s %(AB03_shift_option)s
keycode 47 = %(AB04)s %(AB04_shift)s %(AB04_option)s %(AB04_shift_option)s
keycode 48 = %(AB05)s %(AB05_shift)s %(AB05_option)s %(AB05_shift_option)s
keycode 49 = %(AB06)s %(AB06_shift)s %(AB06_option)s %(AB06_shift_option)s
keycode 50 = %(AB07)s %(AB07_shift)s %(AB07_option)s %(AB07_shift_option)s
keycode 51 = %(AB08)s %(AB08_shift)s %(AB08_option)s %(AB08_shift_option)s
keycode 52 = %(AB09)s %(AB09_shift)s %(AB09_option)s %(AB09_shift_option)s
keycode 53 = %(AB10)s %(AB10_shift)s %(AB10_option)s %(AB10_shift_option)s
#
keycode  57 = space space

#
#include "euro"
#include "windowkeys"
#include "compose"
	
keycode  1 = Escape Escape
keycode 14 = Delete  Delete
keycode 15 = Tab Tab
keycode 28 = Return
keycode 29 = Control
keycode 42 = Shift
keycode 54 = Shift
keycode 56 = Alt
keycode 58 = Caps_Lock
keycode 97 = Control
"""

namesData = {
  0x0000: "nul",
  0x0001: "Control_a",
  0x0002: "Control_b",
  0x0003: "Control_c",
  0x0004: "Control_d",
  0x0005: "Control_e",
  0x0006: "Control_f",
  0x0007: "Control_g",
  0x0008: "BackSpace",
  0x0009: "Tab",
  0x000a: "Linefeed",
  0x000b: "Control_k",
  0x000c: "Control_l",
  0x000d: "Control_m",
  0x000e: "Control_n",
  0x000f: "Control_o",
  0x0010: "Control_p",
  0x0011: "Control_q",
  0x0012: "Control_r",
  0x0013: "Control_s",
  0x0014: "Control_t",
  0x0015: "Control_u",
  0x0016: "Control_v",
  0x0017: "Control_w",
  0x0018: "Control_x",
  0x0019: "Control_y",
  0x001a: "Control_z",
  0x001b: "Escape",
  0x001c: "Control_backslash",
  0x001d: "Control_bracketrig",
  0x001e: "Control_asciicircu",
  0x001f: "Control_underscore",
  0x0020: "space",
  0x0021: "exclam",
  0x0022: "quotedbl",
  0x0023: "numbersign",
  0x0024: "dollar",
  0x0025: "percent",
  0x0026: "ampersand",
  0x0027: "apostrophe",
  0x0028: "parenleft",
  0x0029: "parenright",
  0x002a: "asterisk",
  0x002b: "plus",
  0x002c: "comma",
  0x002d: "minus",
  0x002e: "period",
  0x002f: "slash",
  0x0030: "zero",
  0x0031: "one",
  0x0032: "two",
  0x0033: "three",
  0x0034: "four",
  0x0035: "five",
  0x0036: "six",
  0x0037: "seven",
  0x0038: "eight",
  0x0039: "nine",
  0x003a: "colon",
  0x003b: "semicolon",
  0x003c: "less",
  0x003d: "equal",
  0x003e: "greater",
  0x003f: "question",
  0x0040: "at",
  0x0041: "A",
  0x0042: "B",
  0x0043: "C",
  0x0044: "D",
  0x0045: "E",
  0x0046: "F",
  0x0047: "G",
  0x0048: "H",
  0x0049: "I",
  0x004a: "J",
  0x004b: "K",
  0x004c: "L",
  0x004d: "M",
  0x004e: "N",
  0x004f: "O",
  0x0050: "P",
  0x0051: "Q",
  0x0052: "R",
  0x0053: "S",
  0x0054: "T",
  0x0055: "U",
  0x0056: "V",
  0x0057: "W",
  0x0058: "X",
  0x0059: "Y",
  0x005a: "Z",
  0x005b: "bracketleft",
  0x005c: "backslash",
  0x005d: "bracketright",
  0x005e: "asciicircum",
  0x005f: "underscore",
  0x0060: "grave",
  0x0061: "a",
  0x0062: "b",
  0x0063: "c",
  0x0064: "d",
  0x0065: "e",
  0x0066: "f",
  0x0067: "g",
  0x0068: "h",
  0x0069: "i",
  0x006a: "j",
  0x006b: "k",
  0x006c: "l",
  0x006d: "m",
  0x006e: "n",
  0x006f: "o",
  0x0070: "p",
  0x0071: "q",
  0x0072: "r",
  0x0073: "s",
  0x0074: "t",
  0x0075: "u",
  0x0076: "v",
  0x0077: "w",
  0x0078: "x",
  0x0079: "y",
  0x007a: "z",
  0x007b: "braceleft",
  0x007c: "bar",
  0x007d: "braceright",
  0x007e: "asciitilde",
  0x007f: "Delete",
  0x00a0: "nobreakspace",
  0x00a1: "exclamdown",
  0x00a2: "cent",
  0x00a3: "sterling",
  0x00a5: "yen",
  0x00a7: "section",
  0x00a9: "copyright",
  0x00aa: "ordfeminine",
  0x00ab: "guillemotleft",
  0x00ac: "notsign",
  0x00ad: "hyphen",
  0x00ae: "registered",
  0x00af: "macron",
  0x00b0: "degree",
  0x00b1: "plusminus",
  0x00b2: "twosuperior",
  0x00b3: "threesuperior",
  0x00b5: "mu",
  0x00b6: "paragraph",
  0x00b7: "periodcentered",
  0x00b9: "onesuperior",
  0x00ba: "masculine",
  0x00bb: "guillemotright",
  0x00bf: "questiondown",
  0x00c0: "Agrave",
  0x00c1: "Aacute",
  0x00c2: "Acircumflex",
  0x00c3: "Atilde",
  0x00c4: "Adiaeresis",
  0x00c5: "Aring",
  0x00c6: "AE",
  0x00c7: "Ccedilla",
  0x00c8: "Egrave",
  0x00c9: "Eacute",
  0x00ca: "Ecircumflex",
  0x00cb: "Ediaeresis",
  0x00cc: "Igrave",
  0x00cd: "Iacute",
  0x00ce: "Icircumflex",
  0x00cf: "Idiaeresis",
  0x00d0: "ETH",
  0x00d1: "Ntilde",
  0x00d2: "Ograve",
  0x00d3: "Oacute",
  0x00d4: "Ocircumflex",
  0x00d5: "Otilde",
  0x00d6: "Odiaeresis",
  0x00d7: "multiply",
  0x00d8: "Ooblique",
  0x00d9: "Ugrave",
  0x00da: "Uacute",
  0x00db: "Ucircumflex",
  0x00dc: "Udiaeresis",
  0x00dd: "Yacute",
  0x00de: "THORN",
  0x00df: "ssharp",
  0x00e0: "agrave",
  0x00e1: "aacute",
  0x00e2: "acircumflex",
  0x00e3: "atilde",
  0x00e4: "adiaeresis",
  0x00e5: "aring",
  0x00e6: "ae",
  0x00e7: "ccedilla",
  0x00e8: "egrave",
  0x00e9: "eacute",
  0x00ea: "ecircumflex",
  0x00eb: "ediaeresis",
  0x00ec: "igrave",
  0x00ed: "iacute",
  0x00ee: "icircumflex",
  0x00ef: "idiaeresis",
  0x00f0: "eth",
  0x00f1: "ntilde",
  0x00f2: "ograve",
  0x00f3: "oacute",
  0x00f4: "ocircumflex",
  0x00f5: "otilde",
  0x00f6: "odiaeresis",
  0x00f7: "division",
  0x00f8: "oslash",
  0x00f9: "ugrave",
  0x00fa: "uacute",
  0x00fb: "ucircumflex",
  0x00fc: "udiaeresis",
  0x00fd: "yacute",
  0x00fe: "thorn",
  0x00ff: "ydiaeresis",
}

defaultDeads = ["grave", "acute", "circumflex", "tilde", "diaeresis", "cedilla", "ogonek", "caron", "breve", "doubleacute"]


for i in range(256):
  if not namesData.has_key(i):
    namesData[i] = hex(i)
#  print i, namesData[i]

names = {}
for c, n in namesData.iteritems():
  names[chr(c)] = n
#print names

fullMapValues = {}
for k, v in xkb.tmplValues.iteritems():
#  v = terminators.get( v, v )
  if v == u"&#x0022;":
   v = u'"'
  if v == u"&#x003c;":
   v = u'<'
  if v == u'&#x0026;':
   v = u'&'
  try:
   l = codecs.encode(v, "iso-8859-15")
   fullMapValues[k] = names[l]
  except:
#    if terminators.has_key(v):
    if v in defaultDeads:
      fullMapValues[k] = "dead_" + v
    else:
      print k, v
      fullMapValues[k] = "VoidSymbol"
#out = codecs.open(sys.argv[2], "w", "utf8")
out = file(sys.argv[2], "w")
out.write( fullMapTmpl % fullMapValues )
