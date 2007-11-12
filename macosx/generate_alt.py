#!/usr/bin/env python
# -*- coding: utf-8 -*-

cmdModifierMap = """
  <modifierMap id="commonModifiers" defaultIndex="0">
    <keyMapSelect mapIndex="0">
      <modifier keys="" />
    </keyMapSelect>
    <keyMapSelect mapIndex="1">
      <!-- <modifier keys="anyShift caps?" /> -->
      <modifier keys="anyShift" />
    </keyMapSelect>
    <keyMapSelect mapIndex="2">
      <modifier keys="caps" />
    </keyMapSelect>
    <keyMapSelect mapIndex="3">
      <modifier keys="anyShift caps" />
    </keyMapSelect>
    <keyMapSelect mapIndex="4">
      <modifier keys="anyOption" />
    </keyMapSelect>
    <keyMapSelect mapIndex="5">
      <!-- <modifier keys="anyShift anyOption command? caps?" /> -->
      <modifier keys="anyShift anyOption" />
    </keyMapSelect>
    <keyMapSelect mapIndex="6">
      <modifier keys="anyShift anyOption caps" />
    </keyMapSelect>
    <keyMapSelect mapIndex="7">
      <modifier keys="anyOption caps" />
    </keyMapSelect>
    <keyMapSelect mapIndex="8">
      <modifier keys="anyOption command caps?" />
    </keyMapSelect>
    <keyMapSelect mapIndex="9">
      <modifier keys="anyShift? anyOption? anyControl command? caps?" />
    </keyMapSelect>
    <keyMapSelect mapIndex="10">
      <modifier keys="anyShift? command caps?" />
    </keyMapSelect>
    <keyMapSelect mapIndex="11">
      <modifier keys="anyShift anyOption command caps?" />
    </keyMapSelect>
  </modifierMap>
"""


azertyAdditionalKeyMaps = """
    <keyMap index="10">  <!-- command -->
      <key code="0" output="q" />
      <key code="1" output="s" />
      <key code="2" output="d" />
      <key code="3" output="f" />
      <key code="4" output="h" />
      <key code="5" output="g" />
      <key code="6" output="w" />
      <key code="7" output="x" />
      <key code="8" output="c" />
      <key code="9" output="v" />
      <key code="10" output="@" />
      <key code="11" output="b" />
      <key code="12" output="a" />
      <key code="13" output="z" />
      <key code="14" output="e" />
      <key code="15" output="r" />
      <key code="16" output="y" />
      <key code="17" output="t" />
      <key code="18" output="&#x0026;" />
      <key code="19" output="é" />
      <key code="20" output="&#x0022;" />
      <key code="21" output="'" />
      <key code="22" output="§" />
      <key code="23" output="(" />
      <key code="24" output="-" />
      <key code="25" output="ç" />
      <key code="26" output="è" />
      <key code="27" output=")" />
      <key code="28" output="!" />
      <key code="29" output="à" />
      <key code="30" output="$" />
      <key code="31" output="o" />
      <key code="32" output="u" />
      <key code="33" output="^" />
      <key code="34" output="i" />
      <key code="35" output="p" />
      <key code="36" output="&#x000d;" /> <!-- Return -->
      <key code="37" output="l" />
      <key code="38" output="j" />
      <key code="39" output="ù" />
      <key code="40" output="k" />
      <key code="41" output="m" />
      <key code="42" output="`" />
      <key code="43" output=";" />
      <key code="44" output="=" />
      <key code="45" output="n" />
      <key code="46" output="," />
      <key code="47" output=":" />
      <key code="48" output="&#x0009;" /> <!-- Tab -->
      <key code="49" output=" " /> <!-- Space -->
      <key code="50" output="&#x003c;" />
      <key code="51" output="&#x0008;" /> <!-- Backspace -->
      <key code="52" output="&#x0003;" /> <!-- Enter (Fn-Return) -->
      <key code="53" output="&#x001b;" /> <!-- Escape -->
      <!-- gap, 54 through 64 -->
      <key code="65" output="," /> <!-- keypad -->
      <key code="66" output="&#x001d;" /> <!-- keypad right arrow? -->
      <key code="67" output="*" /> <!-- keypad -->
      <!-- gap, 68 -->
      <key code="69" output="+" /> <!-- keypad -->
      <key code="70" output="&#x001c;" /> <!-- keypad left arrow? -->
      <key code="71" output="&#x001b;" /> <!-- Clear -->
      <key code="72" output="&#x001f;" /> <!-- keypad down arrow? -->
      <!-- gap, 73 through 74 -->
      <key code="75" output="/" /> <!-- keypad -->
      <key code="76" output="&#x0003;" /> <!-- Enter -->
      <key code="77" output="&#x001e;" /> <!-- keypad up arrow? -->
      <key code="78" output="-" /> <!-- keypad -->
      <!-- gap, 79 through 80 -->
      <key code="81" output="=" /> <!-- keypad -->
      <key code="82" output="0" /> <!-- keypad -->
      <key code="83" output="1" /> <!-- keypad -->
      <key code="84" output="2" /> <!-- keypad -->
      <key code="85" output="3" /> <!-- keypad -->
      <key code="86" output="4" /> <!-- keypad -->
      <key code="87" output="5" /> <!-- keypad -->
      <key code="88" output="6" /> <!-- keypad -->
      <key code="89" output="7" /> <!-- keypad -->
      <!-- gap, 90 -->
      <key code="91" output="8" /> <!-- keypad -->
      <key code="92" output="9" /> <!-- keypad -->
      <!-- gap, 93 through 95 -->
      <key code="96" output="&#x0010;" /> <!-- F5 -->
      <key code="97" output="&#x0010;" /> <!-- F6 -->
      <key code="98" output="&#x0010;" /> <!-- F7 -->
      <key code="99" output="&#x0010;" /> <!-- F3 -->
      <key code="100" output="&#x0010;" /> <!-- F8 -->
      <key code="101" output="&#x0010;" /> <!-- F9 -->
      <key code="102" output="&#x0010;" /> <!-- ?? -->
      <key code="103" output="&#x0010;" /> <!-- F11 -->
      <key code="104" output="&#x0010;" /> <!-- ?? -->
      <key code="105" output="&#x0010;" /> <!-- F13 -->
      <key code="106" output="&#x0010;" /> <!-- F16 -->
      <key code="107" output="&#x0010;" /> <!-- F14 -->
      <key code="108" output="&#x0010;" /> <!-- ?? -->
      <key code="109" output="&#x0010;" /> <!-- F10 -->
      <key code="110" output="&#x0010;" /> <!-- ?? -->
      <key code="111" output="&#x0010;" /> <!-- F12 -->
      <key code="112" output="&#x0010;" /> <!-- ?? -->
      <key code="113" output="&#x0010;" /> <!-- F15 -->
      <key code="114" output="&#x0005;" /> <!-- Help -->
      <key code="115" output="&#x0001;" /> <!-- Home -->
      <key code="116" output="&#x000b;" /> <!-- Page Up -->
      <key code="117" output="&#x007f;" /> <!-- Delete -->
      <key code="118" output="&#x0010;" /> <!-- F4 -->
      <key code="119" output="&#x0004;" /> <!-- End -->
      <key code="120" output="&#x0010;" /> <!-- F2 -->
      <key code="121" output="&#x000c;" /> <!-- Page Down -->
      <key code="122" output="&#x0010;" /> <!-- F1 -->
      <key code="123" output="&#x001c;" /> <!-- left arrow -->
      <key code="124" output="&#x001d;" /> <!-- right arrow -->
      <key code="125" output="&#x001f;" /> <!-- down arrow -->
      <key code="126" output="&#x001e;" /> <!-- up arrow -->
      <!-- gap, 127 -->
    </keyMap>
    <keyMap index="11">  <!-- shift option command -->
      <key code="0" output="Ω" />
      <key code="1" output="∑" />
      <key code="2" output="∆" />
      <key code="3" output="·" />
      <key code="4" output="Î" />
      <key code="5" output="ﬂ" />
      <key code="6" output="›" />
      <key code="7" output="⁄" />
      <key code="8" output="¢" />
      <key code="9" output="√" />
      <key code="10" output="Ÿ" />
      <key code="11" output="∫" />
      <key code="12" output="Æ" />
      <key code="13" output="Å" />
      <key code="14" output="Ê" />
      <key code="15" output="‚" />
      <key code="16" output="Ÿ" />
      <key code="17" output="™" />
      <key code="18" output="´" />
      <key code="19" output="„" />
      <key code="20" output="”" />
      <key code="21" output="’" />
      <key code="22" output="å" />
      <key code="23" output="[" />
      <key code="24" output="–" />
      <key code="25" output="Á" />
      <key code="26" output="»" />
      <key code="27" output="]" />
      <key code="28" output="Û" />
      <key code="29" output="Ø" />
      <key code="30" output="¥" />
      <key code="31" output="Œ" />
      <key code="32" output="ª" />
      <key code="33" output="Ô" />
      <key code="34" output="ï" />
      <key code="35" output="∏" />
      <key code="36" output="&#x000d;" /> <!-- Return -->
      <key code="37" output="|" />
      <key code="38" output="Í" />
      <key code="39" output="‰" />
      <key code="40" output="Ë" />
      <key code="41" output="Ó" />
      <key code="42" output="#" />
      <key code="43" output="•" />
      <key code="44" output="±" />
      <key code="45" output="ı" />
      <key code="46" output="¿" />
      <key code="47" output="\" />
      <key code="48" output="&#x0009;" /> <!-- Tab -->
      <key code="49" output=" " /> <!-- Space -->
      <key code="50" output="≥" />
      <key code="51" output="&#x0008;" /> <!-- Backspace -->
      <key code="52" output="&#x0003;" /> <!-- Enter (Fn-Return) -->
      <key code="53" output="&#x001b;" /> <!-- Escape -->
      <!-- gap, 54 through 64 -->
      <key code="65" output="." /> <!-- keypad -->
      <key code="66" output="*" /> <!-- keypad right arrow? -->
      <key code="67" output="*" /> <!-- keypad -->
      <!-- gap, 68 -->
      <key code="69" output="+" /> <!-- keypad -->
      <key code="70" output="+" /> <!-- keypad left arrow? -->
      <key code="71" output="&#x001b;" /> <!-- Clear -->
      <key code="72" output="=" /> <!-- keypad down arrow? -->
      <!-- gap, 73 through 74 -->
      <key code="75" output="/" /> <!-- keypad -->
      <key code="76" output="&#x0003;" /> <!-- Enter -->
      <key code="77" output="/" /> <!-- keypad up arrow? -->
      <key code="78" output="-" /> <!-- keypad -->
      <!-- gap, 79 through 80 -->
      <key code="81" output="=" /> <!-- keypad -->
      <key code="82" output="0" /> <!-- keypad -->
      <key code="83" output="1" /> <!-- keypad -->
      <key code="84" output="2" /> <!-- keypad -->
      <key code="85" output="3" /> <!-- keypad -->
      <key code="86" output="4" /> <!-- keypad -->
      <key code="87" output="5" /> <!-- keypad -->
      <key code="88" output="6" /> <!-- keypad -->
      <key code="89" output="7" /> <!-- keypad -->
      <!-- gap, 90 -->
      <key code="91" output="8" /> <!-- keypad -->
      <key code="92" output="9" /> <!-- keypad -->
      <!-- gap, 93 through 95 -->
      <key code="96" output="&#x0010;" /> <!-- F5 -->
      <key code="97" output="&#x0010;" /> <!-- F6 -->
      <key code="98" output="&#x0010;" /> <!-- F7 -->
      <key code="99" output="&#x0010;" /> <!-- F3 -->
      <key code="100" output="&#x0010;" /> <!-- F8 -->
      <key code="101" output="&#x0010;" /> <!-- F9 -->
      <key code="102" output="&#x0010;" /> <!-- ?? -->
      <key code="103" output="&#x0010;" /> <!-- F11 -->
      <key code="104" output="&#x0010;" /> <!-- ?? -->
      <key code="105" output="&#x0010;" /> <!-- F13 -->
      <key code="106" output="&#x0010;" /> <!-- F16 -->
      <key code="107" output="&#x0010;" /> <!-- F14 -->
      <key code="108" output="&#x0010;" /> <!-- ?? -->
      <key code="109" output="&#x0010;" /> <!-- F10 -->
      <key code="110" output="&#x0010;" /> <!-- ?? -->
      <key code="111" output="&#x0010;" /> <!-- F12 -->
      <key code="112" output="&#x0010;" /> <!-- ?? -->
      <key code="113" output="&#x0010;" /> <!-- F15 -->
      <key code="114" output="&#x0005;" /> <!-- Help -->
      <key code="115" output="&#x0001;" /> <!-- Home -->
      <key code="116" output="&#x000b;" /> <!-- Page Up -->
      <key code="117" output="&#x007f;" /> <!-- Delete -->
      <key code="118" output="&#x0010;" /> <!-- F4 -->
      <key code="119" output="&#x0004;" /> <!-- End -->
      <key code="120" output="&#x0010;" /> <!-- F2 -->
      <key code="121" output="&#x000c;" /> <!-- Page Down -->
      <key code="122" output="&#x0010;" /> <!-- F1 -->
      <key code="123" output="&#x001c;" /> <!-- left arrow -->
      <key code="124" output="&#x001d;" /> <!-- right arrow -->
      <key code="125" output="&#x001f;" /> <!-- down arrow -->
      <key code="126" output="&#x001e;" /> <!-- up arrow -->
      <!-- gap, 127 -->
    </keyMap>
"""


additionalBaseIndex = """
    <keyMap index="10" baseMapSet="ISO" baseIndex="10">  <!-- command -->
    </keyMap>
    <keyMap index="11" baseMapSet="ISO" baseIndex="11">  <!-- shift option command -->
    </keyMap>
"""

rscDir = 'fr-dvorak-bepo.bundle/Contents/Resources/'
input = file(rscDir + 'fr-dvorak-bepo.keylayout')

toGenerate = [
#  (name, group, id, additionalKeymap, nameExt)
  (rscDir + 'fr-dvorak-bepo-roman.keylayout', 0, 6538, None, ' (Roman)'),
  (rscDir + 'fr-dvorak-bepo-azerty.keylayout', 126, -6539, azertyAdditionalKeyMaps, ' - Azerty'),
  (rscDir + 'fr-dvorak-bepo-azerty-roman.keylayout', 0, 6539, azertyAdditionalKeyMaps, ' - Azerty (Roman)'),
]

for (name, group, id, additionalKeymap, nameExt) in toGenerate:
  input.seek(0)
  output = file(name, 'w')
  
  # there are 2 keymap sets
  additionalKeymapDone = False
  
  l = input.readline()
  while l:
  
    if '<keyboard' in l:
      # change the group, the id, and extend the name
      l = l.replace('group="126"', 'group="%s"' % group)
      l = l.replace('id="-6538"', 'id="%s"' % id)
      l = l.replace('" maxout="', nameExt + '" maxout="')
  
    if additionalKeymap and '<modifierMap' in l:
      # skip this part
      while not '</modifierMap' in l:
        l = input.readline()
      # a last one, to remove the closing tag
      l = input.readline()
      # and write the custom modifierMap instead of the one in the input file
      output.write(cmdModifierMap)
      
    if not additionalKeymapDone and additionalKeymap and '</keyMapSet>' in l:
      # write the additional keymap before closing the keymap set
      output.write(additionalKeymap)
      additionalKeymapDone = True
    # must use elif to avoid adding the additional base index just after the additional keymap
    elif additionalKeymapDone and additionalKeymap and '</keyMapSet>' in l:
      # write the missing base index before closing the keymap set
      output.write(additionalBaseIndex)
      
    output.write(l)
    
    l = input.readline()
    
  output.close()