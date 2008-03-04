#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Parseur de fichier xkb et attribution des symboles aux touches pour mac os
#
# Copyright (C) 2008 Gaëtan Lehmann <gaetan.lehmann@jouy.inra.fr>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#


import re, sys, maCompose, codecs

terminators = {
"abovedot": u"˙",
"acute": u"´",
"bar": u"-",
"belowdot": u".",
"belt": u"?",
"breve": u"˘",
"brevebelow": u"?",
"caron": u"ˇ",
"cedilla": u"¸",
"circumflex": u"^",
"circumflexbelow": u"̭",
"commabelow": u",",
"crossedtail": u"?",
"curl": u"?",
"currency": u"¤",
"diaeresis": u"¨",
"diaresisbelow": u"̤",
"diagonalstroke": u"?",
"doubleacute": u"˝",
"doublegrave": u"?",
"fishhook": u"?",
"grave": u"`",
"hook": u"?",
"hookabove": u"̉",
"horn": u"̛",
"invertedbreve": u"̑",
"lefthook": u"?",
"linebelow": u"_",
"longleg": u"?",
"longrightleg": u"?",
"macron": u"¯",
"middletilde": u"?",
"ogonek": u"˛",
"palatalhook": u"?",
"retroflexhook": u"̢",
"righthalfring": u"ʾ",
"ringabove": u"°",
"ringbelow": u"̥",
"stroke": u"/",
"swashtail": u"?",
"tail": u"?",
"tilde": u"~",
"tildebelow": u"̰",
"topbar": u"⁻",
}

str_catchKey = r"^\s*key\s*<([A-Z0-9]{4})>\s*{(.*)\[(.*)\]\s*}\s*;\s*(:?//.*|$)"
re_catchKey = re.compile(str_catchKey)

f = file("xkb")

normal = {}
shift = {}
altgr = {}
altgrshift = {}
options = {}

for l in f:
  res = re_catchKey.match(l)
  if res:
    key = unicode(res.group(1))
    charsGroup = res.group(3)
    chars = re.split(r', *', charsGroup)
    chars = [c.strip() for c in chars]
    chars = [maCompose.char(c) for c in chars]
    chars = chars + ['']*(4-len(chars))
    
    normal[key], shift[key], altgr[key], altgrshift[key] = chars
    options[key] = res.group(2)
#    print key, chars
# print options["AE02"]
# sys.exit()

tmplValues = {}
chars = set()

tmplValues.update(normal)

for k, v in normal.iteritems():
  V = v
  if "FOUR_LEVEL_SEMIALPHABETIC" not in options[k]:
    if len(v) == 1:
      V = v.upper()
  else:
    V = shift[k]
  tmplValues[k+'_capslock'] = V
  chars.add(V)

for k, v in shift.iteritems():
  tmplValues[k+'_shift'] = v
  chars.add(v)
  
  V = v
  if "FOUR_LEVEL_SEMIALPHABETIC" not in options[k]:
    if len(v) == 1:
      V = v.lower()
  else:
    V = normal[k]
  tmplValues[k+'_shift_capslock'] = V
  chars.add(V)

for k, v in altgr.iteritems():
  tmplValues[k+'_option'] = v
  chars.add(v)

  V = v
  if "FOUR_LEVEL_SEMIALPHABETIC" not in options[k]:
    if len(v) == 1:
      V = v.upper()
  else:
    V = altgrshift[k]
  tmplValues[k+'_option_capslock'] = V
  chars.add(V)

  V = terminators.get( v, v )
  tmplValues[k+'_option_command'] = V
  chars.add(V)


for k, v in altgrshift.iteritems():
  tmplValues[k+'_shift_option'] = v
  chars.add(v)

  V = v
  if "FOUR_LEVEL_SEMIALPHABETIC" not in options[k]:
    if len(v) == 1:
      V = v.lower()
  else:
    V = altgr[k]
  tmplValues[k+'_shift_option_capslock'] = V
  chars.add(V)
 
chars.remove('')
actions = set( [maCompose.composeChars[c] for c in chars if c] )

tmpl = codecs.open("fr-dvorak-bepo.keylayout.tmpl", encoding='utf8').read()

if __name__ == "__main__":
  tmplValues[u"actionsAndTerminators"] = ""
  print tmpl % tmplValues

