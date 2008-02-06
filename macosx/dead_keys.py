# -*- coding: utf-8 -*-

import unicodedata, re, sys

chrRegExp = re.compile(r'LATIN (CAPITAL|SMALL) LETTER (.+)')
d = {}
dc = {}
dm = set()
dmm = set()

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

for c in range(0,0x10000):
  C = unichr(c)
  try:
    name = unicodedata.name(C)
  except:
    continue
    
  if not name.startswith('LATIN '):
    continue
    
#  if 'STROKE' in name : print name
  
  ns = name.split(' WITH ')
  n = ns[0]
  ms = ' AND '.join(ns[1:])
  modifiers = ms.split(' AND ')
  for m in ['SMALL LETTER J', 'SMALL LETTER Z', 'STRIKETHROUGH']:
    if m in modifiers :
      n = n + ' WITH ' + m
      modifiers.remove(m)
      print name, '*********************', C
  if 'DOTLESS' in n:
    n = n.replace('DOTLESS ', '')
    modifiers.append('DOT ABOVE')
  if 'MIDDLE DOT' in modifiers:
    del modifiers[ modifiers.index('MIDDLE DOT') ]
    modifiers.append('DOT ABOVE')
  if '' in modifiers:
    modifiers.remove('')
  modifiers = sorted([finalModNames[m] for m in modifiers])
  modifiers = tuple(modifiers)

  for m in modifiers:
    dm.add(m)
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
  
  
  