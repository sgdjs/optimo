# -*- coding: utf-8 -*-

import unicodedata, re, sys

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
'LATIN CAPITAL LETTER B WITH CURRENCY': u'₱',
'LATIN CAPITAL LETTER C WITH CURRENCY': u'₡',
'LATIN SMALL LETTER C WITH CURRENCY': u'¢',
'LATIN CAPITAL LETTER D WITH CURRENCY': u'₯',
'LATIN SMALL LETTER D WITH CURRENCY': u'₫',
'LATIN CAPITAL LETTER E WITH CURRENCY': u'₠',
'LATIN SMALL LETTER E WITH CURRENCY': u'€',
'LATIN CAPITAL LETTER F WITH CURRENCY': u'₣',
'LATIN SMALL LETTER F WITH CURRENCY': u'ƒ',
'LATIN CAPITAL LETTER G WITH CURRENCY': u'₲',
'LATIN SMALL LETTER G WITH CURRENCY': u'₴',
'LATIN CAPITAL LETTER K WITH CURRENCY': u'₭',
'LATIN CAPITAL LETTER L WITH CURRENCY': u'₤',
'LATIN SMALL LETTER L WITH CURRENCY': u'£',
'LATIN CAPITAL LETTER M WITH CURRENCY': u'ℳ',
'LATIN SMALL LETTER M WITH CURRENCY': u'₥',
'LATIN CAPITAL LETTER N WITH CURRENCY': u'₦',
'LATIN CAPITAL LETTER P WITH CURRENCY': u'₧',
'LATIN SMALL LETTER P WITH CURRENCY': u'₰',
'LATIN SMALL LETTER R WITH CURRENCY': u'₨',
'LATIN SMALL LETTER R WITH CURRENCY': u'₢',
'LATIN CAPITAL LETTER S WITH CURRENCY': u'$',
'LATIN SMALL LETTER S WITH CURRENCY': u'₪',
'LATIN CAPITAL LETTER T WITH CURRENCY': u'₮',
'LATIN CAPITAL LETTER W WITH CURRENCY': u'₩',
'LATIN CAPITAL LETTER X WITH CURRENCY': u'₵',
'LATIN CAPITAL LETTER Y WITH CURRENCY': u'¥',
}

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
      print name, "est déjà défini."
    else :
      dc[ (key, modifiers) ] = C
    modSet.add( modifiers )
    d[key] = modSet


# now generate the xml code!
#
# store the previous character to print a blank line bitween the chars
previous = None

for c in sorted(d.keys(), case_order):
  if len(d[c]) != 1 or len(c[0]) == 1:
    if tuple([]) in d[c]:
      if dc[ c, tuple([]) ].lower() != previous:
        print
#      print ' '.join(c), ' '.join([dc[ c, a ] for a in d[c]])
      print '    <action id="%s">' % dc[ c, tuple([]) ]
      for mod in sorted(d[c], mod_order) :
        # print '    ', '_'.join([finalModNames[m] for m in mod]), dc[ c, mod ]
        if len(mod) == 0:
          fm = 'none'
        else:
          fm = '_'.join(mod)
#        print u'      <when state="%s" output="%s"/> <!-- %s -->' % (fm, dc[ c, mod ], unicodedata.name(dc[ c, mod ]) )
        print u'      <when state="%s" output="%s"/>' % (fm, dc[ c, mod ] )
      print '    </action>'
      
      # generate the code for 2 modifiers, when a char with on of the 2 diacritic sign
      # is produced
      subd = {}
      for mod in [m for m in d[c] if len(m) == 2 ] :
        for m1 in mod:
          if (m1,) in d[c]:
       #     print '    <action id="%s">' % dc[ c, (m1,) ]
#            print u'      <when state="%s" output="%s"/> <!-- %s -->' % ('none', dc[ c, (m1,) ], unicodedata.name(dc[ c, (m1,) ]))
        #    print u'      <when state="%s" output="%s"/>' % ('none', dc[ c, (m1,) ])
            for m2 in mod:
              if m1 != m2:
                l = subd.get(dc[ c, (m1,) ], [])
                l.append((m2, dc[ c, mod ]))
                subd[dc[ c, (m1,) ]] = l
#                print u'      <when state="%s" output="%s"/> <!-- %s -->' % (m2, dc[ c, mod ], unicodedata.name(dc[ c, mod ]))
#                print u'      <when state="%s" output="%s"/>' % (m2, dc[ c, mod ])
      #      print '    </action>'
      #print subd
      for c1 in sorted(subd.keys()):
        print '    <action id="%s">' % c1
        print u'      <when state="%s" output="%s"/>' % ('none', c1)
        for m, c2 in subd[c1]:
          print u'      <when state="%s" output="%s"/>' % (m, c2)
        print '    </action>'
        
      previous = dc[ c, tuple([]) ].lower()
              
        
    else:
      raise ' '.join(c), d[c]
#  else:
#    print '*********************************************', c
    
    
modStates = {}
for m in dm:
  modStates[m] = [('none', m)]

print
print
print '  <terminators>'
for m in sorted(dmm, mod_order):
  if m != tuple():
    print '    <when state="%s" output="?"/>' % '_'.join(m)
  if len(m) == 2:
    m1, m2 = m
    modStates[m1].append((m2, '%s_%s' % (m1, m2)))
    modStates[m2].append((m1, '%s_%s' % (m1, m2)))
print '  <terminators>'
  
print
print
for m in sorted(modStates.keys()):
  l = modStates[m]
  print '    <action id="%s">' % m
  for s, n in sorted(l, mod_order2):
    print '      <when state="%s" next="%s"/>' % (s, n)
  print '    </action>'
  
  
  