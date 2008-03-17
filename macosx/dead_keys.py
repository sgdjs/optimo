#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Génération de touches mortes pour mac os 
#
# Copyright (C) 2008 Gaëtan Lehmann <gaetan.lehmann@jouy.inra.fr>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#


import unicodedata, re, sys, compose, xkb

# the reg exp used to parse the unicode name
chrRegExp = re.compile(r'LATIN (CAPITAL|SMALL) LETTER (.+)')

finalModNames = {
'ACUTE': 'acute',
'BAR': 'bar',
'DOT ABOVE': 'abovedot',
'TOPBAR': 'topbar', 
'HORN': 'horn', 
'CIRCUMFLEX': 'circumflex', 
'HOOK': 'hook', 
'LONG RIGHT LEG': 'longrightleg', 
'INVERTED BREVE': 'invertedbreve', 
'CURL': 'curl', 
'PALATAL HOOK': 'palatalhook', 
'LEFT HOOK': 'lefthook', 
'BELT': 'belt', 
'CROSSED-TAIL': 'crossedtail', 
'HOOK ABOVE': 'hookabove', 
'RIGHT HALF RING': 'righthalfring', 
'MACRON': 'macron', 
'BREVE BELOW': 'brevebelow', 
'TILDE': 'tilde', 
'FISHHOOK': 'fishhook', 
'CEDILLA': 'cedilla', 
'GRAVE': 'grave', 
'COMMA BELOW': 'commabelow', 
'SWASH TAIL': 'swashtail', 
'RING BELOW': 'ringbelow', 
'RETROFLEX HOOK': 'retroflexhook', 
'STROKE': 'stroke', 
'DIAERESIS BELOW': 'diaresisbelow', 
'LONG LEG': 'longleg', 
'DOT BELOW': 'belowdot', 
'CIRCUMFLEX BELOW': 'circumflexbelow', 
'RING ABOVE': 'ringabove', 
'DOUBLE GRAVE': 'doublegrave', 
'OGONEK': 'ogonek', 
'LINE BELOW': 'linebelow', 
'DIAERESIS': 'diaeresis', 
'TILDE BELOW': 'tildebelow', 
'DIAGONAL STROKE': 'diagonalstroke', 
'MIDDLE TILDE': 'middletilde', 
'TAIL': 'tail', 
'MIDDLE DOT': 'middledot', 
'BREVE': 'breve', 
'CARON': 'caron', 
'DOUBLE ACUTE': 'doubleacute',
'CURRENCY': 'currency',
}

currency = {
'LATIN CAPITAL LETTER A WITH CURRENCY': u'₳',
'LATIN SMALL LETTER A WITH CURRENCY': u'؋',
'LATIN CAPITAL LETTER B WITH CURRENCY': u'₱',
'LATIN SMALL LETTER B WITH CURRENCY': u'฿',
'LATIN CAPITAL LETTER C WITH CURRENCY': u'₡',
'LATIN SMALL LETTER C WITH CURRENCY': u'¢',
'LATIN CAPITAL LETTER C WITH CURRENCY AND CEDILLA': u'₵',
'LATIN SMALL LETTER C WITH CURRENCY AND CEDILLA': u'₵',
'LATIN CAPITAL LETTER D WITH CURRENCY': u'₯',
'LATIN SMALL LETTER D WITH CURRENCY': u'₫',
'LATIN CAPITAL LETTER E WITH CURRENCY': u'₠',
'LATIN SMALL LETTER E WITH CURRENCY': u'€',
'LATIN CAPITAL LETTER F WITH CURRENCY': u'₣',
'LATIN SMALL LETTER F WITH CURRENCY': u'ƒ',
'LATIN CAPITAL LETTER G WITH CURRENCY': u'₲',
'LATIN SMALL LETTER G WITH CURRENCY': u'₲',
'LATIN CAPITAL LETTER H WITH CURRENCY': u'₴',
'LATIN SMALL LETTER H WITH CURRENCY': u'₴',
'LATIN CAPITAL LETTER I WITH CURRENCY': u'៛',
'LATIN SMALL LETTER I WITH CURRENCY': u'﷼',
'LATIN CAPITAL LETTER K WITH CURRENCY': u'₭',
'LATIN SMALL LETTER K WITH CURRENCY': u'₭',
'LATIN CAPITAL LETTER L WITH CURRENCY': u'₤',
'LATIN SMALL LETTER L WITH CURRENCY': u'£',
'LATIN CAPITAL LETTER M WITH CURRENCY': u'ℳ',
'LATIN SMALL LETTER M WITH CURRENCY': u'₥',
'LATIN CAPITAL LETTER N WITH CURRENCY': u'₦',
'LATIN SMALL LETTER N WITH CURRENCY': u'₦',
'LATIN CAPITAL LETTER O WITH CURRENCY': u'૱',
'LATIN SMALL LETTER O WITH CURRENCY': u'௹',
'LATIN CAPITAL LETTER P WITH CURRENCY': u'₧',
'LATIN SMALL LETTER P WITH CURRENCY': u'₰',
'LATIN SMALL LETTER R WITH CURRENCY': u'₨',
'LATIN SMALL LETTER R WITH CURRENCY': u'₢',
'LATIN CAPITAL LETTER S WITH CURRENCY': u'$',
'LATIN SMALL LETTER S WITH CURRENCY': u'₪',
'LATIN CAPITAL LETTER T WITH CURRENCY': u'₮',
'LATIN SMALL LETTER T WITH CURRENCY': u'৳',
'LATIN CAPITAL LETTER THORN WITH CURRENCY': u'৲',
'LATIN SMALL LETTER THORN WITH CURRENCY': u'৲',
'LATIN CAPITAL LETTER U WITH CURRENCY': u'圓',
'LATIN SMALL LETTER U WITH CURRENCY': u'元',
'LATIN CAPITAL LETTER W WITH CURRENCY': u'₩',
'LATIN SMALL LETTER W WITH CURRENCY': u'₩',
'LATIN CAPITAL LETTER Y WITH CURRENCY': u'円',
'LATIN SMALL LETTER Y WITH CURRENCY': u'¥',
}

circumflex = {
'LATIN CAPITAL LETTER 0': u'0',
'LATIN CAPITAL LETTER 0 WITH CIRCUMFLEX': u'⁰',
'LATIN CAPITAL LETTER 1': u'1',
'LATIN CAPITAL LETTER 1 WITH CIRCUMFLEX': u'¹',
'LATIN CAPITAL LETTER 2': u'2',
'LATIN CAPITAL LETTER 2 WITH CIRCUMFLEX': u'²',
'LATIN CAPITAL LETTER 3': u'3',
'LATIN CAPITAL LETTER 3 WITH CIRCUMFLEX': u'³',
'LATIN CAPITAL LETTER 4': u'4',
'LATIN CAPITAL LETTER 4 WITH CIRCUMFLEX': u'⁴',
'LATIN CAPITAL LETTER 5': u'5',
'LATIN CAPITAL LETTER 5 WITH CIRCUMFLEX': u'⁵',
'LATIN CAPITAL LETTER 6': u'6',
'LATIN CAPITAL LETTER 6 WITH CIRCUMFLEX': u'⁶',
'LATIN CAPITAL LETTER 7': u'7',
'LATIN CAPITAL LETTER 7 WITH CIRCUMFLEX': u'⁷',
'LATIN CAPITAL LETTER 8': u'8',
'LATIN CAPITAL LETTER 8 WITH CIRCUMFLEX': u'⁸',
'LATIN CAPITAL LETTER 9': u'9',
'LATIN CAPITAL LETTER 9 WITH CIRCUMFLEX': u'⁹',
'LATIN CAPITAL LETTER +': u'+',
'LATIN CAPITAL LETTER + WITH CIRCUMFLEX': u'⁺',
'LATIN CAPITAL LETTER (': u'(',
'LATIN CAPITAL LETTER ( WITH CIRCUMFLEX': u'⁽',
'LATIN CAPITAL LETTER )': u')',
'LATIN CAPITAL LETTER ) WITH CIRCUMFLEX': u'⁾',
'LATIN CAPITAL LETTER =': u'=',
'LATIN CAPITAL LETTER = WITH CIRCUMFLEX': u'⁼',
'LATIN CAPITAL LETTER -': u'-',
'LATIN CAPITAL LETTER - WITH CIRCUMFLEX': u'⁻',
}

stroke = {
'LATIN CAPITAL LETTER 2 WITH STROKE': u'ƻ',
'LATIN CAPITAL LETTER LESS': u'&#x003c;',
'LATIN CAPITAL LETTER LESS WITH STROKE': u'≮',
'LATIN CAPITAL LETTER GREATER': u'>',
'LATIN CAPITAL LETTER GREATER WITH STROKE': u'≯',
'LATIN CAPITAL LETTER = WITH STROKE': u'≠',
# missing chars in python 2.5 unicode
'LATIN CAPITAL LETTER E WITH STROKE': u'Ɇ',
'LATIN SMALL LETTER E WITH STROKE': u'ɇ',
# u with stroke
'LATIN CAPITAL LETTER U WITH STROKE': u'Ʉ',
'LATIN SMALL LETTER U WITH STROKE': u'ʉ',
}


from terminators import terminators, combiningTerminators


# 'STRIKETHROUGH', 
# 'SMALL LETTER J':, 
# 'SMALL LETTER Z', 

def case_order(a,b):
  if a[0] != b[0]:
    return cmp(a, b)
  return cmp(b[1], a[1])
  
def mod_order(a,b):
  if len(a) == len(b):
    return cmp(a,b)
  return cmp(len(a), len(b))

def mod_order2(a,b):
  if a[0] == b[0]:
    return 0
  if a[0] == 'none':
    return -1
  if b[0] == 'none':
    return 1
  return cmp(a, b)
  
  
# create the unicode dict, with extended chars for the dead keys
# key: the unicode name (str)
# value: the unicode char (unicode)
unicode_dict = {}
for c in range(0,0x10000):
  C = unichr(c)
  try:
    name = unicodedata.name(C)
  except:
    continue
  if name.startswith('LATIN '):
    unicode_dict[name] = C
# append the currency signs
unicode_dict.update(currency)
unicode_dict.update(circumflex)
unicode_dict.update(stroke)


# iterate over all the items to build the set of modifiers for the
# basic latin characters, and the set of modifiers
#
# The result is stored in d
# key: a tuple where the first item is the letter name, and the second
# is "SMALL" or "CAPITAL". Ex: ('W', 'CAPITAL')
# value: a set of tuple of modifiers. Ex: set([('acute',), ('circumflex',),
# ('acute', 'circumflex'), ()]). The modifiers or ordered in the tuple.
#
d = {}

# the dictionnary which associate the char, case, and modifiers to an unicode
# character
# key: ( ( name, case), (mod1, mod2, ...) )
# value: an unicode char
dc = {}

# the set of modifiers used
dm = set()

# the set of sets of modifiers
dmm = set()

for name, C in unicode_dict.iteritems():
  # to register the name in compose
  compose.name(C)
  # split the name and the modifiers
  ns = name.split(' WITH ')
  n = ns[0]
  ms = ' AND '.join(ns[1:])
  modifiers = ms.split(' AND ')
  # some chars have a WITH to describe something which is not a modifier
  for m in ['SMALL LETTER J', 'SMALL LETTER Z', 'STRIKETHROUGH']:
    if m in modifiers :
      n = n + ' WITH ' + m
      modifiers.remove(m)
  # translate the dotless modifier to dot above.
  if 'DOTLESS' in n:
    n = n.replace('DOTLESS ', '')
    modifiers.append('DOT ABOVE')
  # translate the middle dot modifier to dot above
  if 'MIDDLE DOT' in modifiers:
    del modifiers[ modifiers.index('MIDDLE DOT') ]
    modifiers.append('DOT ABOVE')
  # remove empty string in the modifier, to generate an empty tuple
  if '' in modifiers:
    modifiers.remove('')
  # translate the modifier names to there final name, sort the modifiers, and
  # and convert the list to a tuple
  modifiers = [finalModNames[m] for m in modifiers]
  modifiers = sorted(modifiers)
  modifiers = tuple(modifiers)

  # store the modifiers independently
  for m in modifiers:
    dm.add(m)
  # and store the modifier set
  dmm.add(modifiers)

  m = chrRegExp.match( n )
  if m:
#    print m.group(1), m.group(2), m.group(3)
    case = m.group(1)
    letter = m.group(2)

    key = (letter, case)
    modSet = d.get( key , set([]) )
    if modifiers in modSet:
      print >> sys.stderr, name, "est déjà défini."
      dc[ (key, modifiers) ] = min( dc[ (key, modifiers) ], C )
    else :
      dc[ (key, modifiers) ] = C
    modSet.add( modifiers )
    d[key] = modSet


# now generate the xml code!
#

deadXMLCode = ""

deadXMLCode += '\n'+ "  <actions>"

# store the previous character to deadXMLCode += '\n'+ a blank line bitween the chars
previous = None

# store the actions already deadXMLCode += '\n'+ed. Space and nbsp are aleady there because they are
# special case treated at the end.
actions = set([u' ', u' '])

for c in sorted(d.keys(), case_order):
  if len(d[c]) != 1 or len(c[0]) == 1:
    if tuple([]) in d[c]:
      if dc[ c, tuple([]) ].lower() != previous:
        deadXMLCode += '\n'
      deadXMLCode += '\n'+ '    <action id="%s">' % dc[ c, tuple([]) ]
      for mod in sorted(d[c], mod_order) :
        # deadXMLCode += '\n'+ '    ', '_'.join([finalModNames[m] for m in mod]), dc[ c, mod ]
        if len(mod) == 0:
          fm = 'none'
        else:
          fm = '_'.join(mod)
        deadXMLCode += '\n'+ u'      <when state="%s" output="%s"/>' % (fm, dc[ c, mod ] )
        
      C = dc[ c, tuple([]) ]
      if compose.charActions.has_key(C):
        a = compose.charActions[C]
        if compose.statesByAction.has_key(a):
          for s in sorted(compose.statesByAction[a]):
            deadXMLCode += '\n'+ u'      <when state="%s" next="%s"/>' % ('_'.join(s), '_'.join(s+(a,)))
        if compose.outputsByAction.has_key(a):
          for s, c1 in sorted(compose.outputsByAction[a]):
            deadXMLCode += '\n'+ u'      <when state="%s" output="%s"/>' % ('_'.join(s), c1)        
        
      deadXMLCode += '\n'+ '    </action>'
      actions.add(C)
      
      # generate the code for 2 modifiers, when a char with on of the 2 diacritic sign
      # is produced
      subd = {}
      for mod in [m for m in d[c] if len(m) == 2 ] :
        for m1 in mod:
          if (m1,) in d[c]:
            for m2 in mod:
              if m1 != m2:
                l = subd.get(dc[ c, (m1,) ], [])
                l.append((m2, dc[ c, mod ]))
                subd[dc[ c, (m1,) ]] = l
      for c1 in sorted(subd.keys()):
        deadXMLCode += '\n'+ '    <action id="%s">' % c1
        deadXMLCode += '\n'+ u'      <when state="%s" output="%s"/>' % ('none', c1)
        for m, c2 in sorted(subd[c1]):
          deadXMLCode += '\n'+ u'      <when state="%s" output="%s"/>' % (m, c2)
          
        if compose.charActions.has_key(c1):
          a = compose.charActions[c1]
          if compose.statesByAction.has_key(a):
            for s in sorted(compose.statesByAction[a]):
              deadXMLCode += '\n'+ u'      <when state="%s" next="%s"/>' % ('_'.join(s), '_'.join(s+(a,)))
          if compose.outputsByAction.has_key(a):
            for s, C in sorted(compose.outputsByAction[a]):
              deadXMLCode += '\n'+ u'      <when state="%s" output="%s"/>' % ('_'.join(s), C)
        
        deadXMLCode += '\n'+ '    </action>'
        actions.add(c1)
        
      previous = dc[ c, tuple([]) ].lower()
              
        
    else:
      raise ' '.join(c), d[c]
#  else:
#    deadXMLCode += '\n'+ '*********************************************', c
    
    
# actions with multi keys and without dead keys
for C in sorted( set(compose.charActions.keys() + list(xkb.chars) ) - actions - set(["Multi_key"])):
  a = compose.composeChars.get(C, C)
  if not a.startswith("dead_"):
    deadXMLCode += '\n'
    deadXMLCode += '\n'+ u'    <action id="%s">' % C
    deadXMLCode += '\n'+ u'      <when state="none" output="%s"/>' % C
    if compose.statesByAction.has_key(a):
      for s in sorted(compose.statesByAction[a]):
        deadXMLCode += '\n'+ u'      <when state="%s" next="%s"/>' % ('_'.join(s), '_'.join(s+(a,)))
    if compose.outputsByAction.has_key(a):
      for s, c1 in sorted(compose.outputsByAction[a]):
        deadXMLCode += '\n'+ u'      <when state="%s" output="%s"/>' % ('_'.join(s), c1)        
    deadXMLCode += '\n'+ u'    </action>'


# the space char produces the terminator char when a dead_ states is activated
deadXMLCode += '\n'
deadXMLCode += '\n'+ u'    <action id=" ">'
deadXMLCode += '\n'+ u'      <when state="none" output=" "/>'
for m in sorted(dmm, mod_order):
  if m != tuple():
    deadXMLCode += '\n'+ '      <when state="%s" output="%s"/>' % ('_'.join(m), ''.join([terminators[n] for n in m]))
if compose.charActions.has_key(u' '):
  a = compose.charActions[u' ']
  if compose.statesByAction.has_key(a):
    for s in sorted(compose.statesByAction[a]):
      deadXMLCode += '\n'+ u'      <when state="%s" next="%s"/>' % ('_'.join(s), '_'.join(s+(a,)))
  if compose.outputsByAction.has_key(a):
    for s, C in sorted(compose.outputsByAction[a]):
      deadXMLCode += '\n'+ u'      <when state="%s" output="%s"/>' % ('_'.join(s), C)
deadXMLCode += '\n'+ u'    </action>'


# the space char produces the terminator char when a dead_ states is activated
deadXMLCode += '\n'
deadXMLCode += '\n'+ u'    <action id=" "> <!-- nbsp -->'
deadXMLCode += '\n'+ u'      <when state="none" output=" "/>'
for m in sorted(dmm, mod_order):
  if m != tuple():
    deadXMLCode += '\n'+ '      <when state="%s" output="%s"/>' % ('_'.join(m), ''.join([combiningTerminators[n] for n in m]))
if compose.charActions.has_key(u' '):
  a = compose.charActions[u' ']
  if compose.statesByAction.has_key(a):
    for s in sorted(compose.statesByAction[a]):
      deadXMLCode += '\n'+ u'      <when state="%s" next="%s"/>' % ('_'.join(s), '_'.join(s+(a,)))
  if compose.outputsByAction.has_key(a):
    for s, C in sorted(compose.outputsByAction[a]):
      deadXMLCode += '\n'+ u'      <when state="%s" output="%s"/>' % ('_'.join(s), C)
deadXMLCode += '\n'+ u'    </action>'



modStates = {}
for m in dm:
  modStates[m] = [('none', m)]

for m in sorted(dmm, mod_order):
  if len(m) == 2:
    m1, m2 = m
    modStates[m1].append((m2, '%s_%s' % (m1, m2)))
    modStates[m2].append((m1, '%s_%s' % (m1, m2)))
  
deadXMLCode += '\n'
deadXMLCode += '\n'
for m in sorted(modStates.keys()):
  l = modStates[m]
  deadXMLCode += '\n'+ '    <action id="%s">' % m
  for s, n in sorted(l, mod_order2):
    deadXMLCode += '\n'+ '      <when state="%s" next="%s"/>' % (s, n)
    
  if compose.charActions.has_key(m):
    a = compose.charActions[m]
    if compose.statesByAction.has_key(a):
      for s in sorted(compose.statesByAction[a]):
        deadXMLCode += '\n'+ u'      <when state="%s" next="%s"/>' % ('_'.join(s), '_'.join(s+(a,)))
    if compose.outputsByAction.has_key(a):
      for s, c1 in sorted(compose.outputsByAction[a]):
        deadXMLCode += '\n'+ u'      <when state="%s" output="%s"/>' % ('_'.join(s), c1)   
            
  deadXMLCode += '\n'+ '    </action>'
  
deadXMLCode += '\n'+ '    <action id="Multi_key">'
deadXMLCode += '\n'+ '      <when state="none" next="Multi_key"/>'
deadXMLCode += '\n'+ '    </action>'
deadXMLCode += '\n'
deadXMLCode += '\n'+ '    <action id="">'
deadXMLCode += '\n'+ '      <when state="none" output=""/>'
deadXMLCode += '\n'+ '    </action>'

deadXMLCode += '\n'+ "  </actions>"
  
deadXMLCode += '\n'
deadXMLCode += '\n'
deadXMLCode += '\n'+ '  <terminators>'
for m in sorted(dmm, mod_order):
  if m != tuple():
    deadXMLCode += '\n'+ '    <when state="%s" output="%s"/>' % ('_'.join(m), ''.join([terminators[n] for n in m]))
for ss in sorted(compose.states):
  C = ''.join([compose.terminators.get(compose.char(s), compose.char(s)) for s in ss])
  s = '_'.join(list(ss))
  deadXMLCode += '\n'+ '    <when state="%s" output="%s"/>' % (s, C)
deadXMLCode += '\n'+ '  </terminators>'

if __name__ == "__main__":
  print deadXMLCode
  
  