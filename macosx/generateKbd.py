
import xkb, dead_keys, codecs

xkb.tmplValues[u"actionsAndTerminators"] = dead_keys.deadXMLCode
out = codecs.open("fr-dvorak-bepo.bundle/Contents/Resources/fr-dvorak-bepo.keylayout", "w", "utf8")
out.write( xkb.tmpl % xkb.tmplValues )
