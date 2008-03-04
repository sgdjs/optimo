#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Génération du clavier pour mac os à partir d'un fichier xkb
#
# Copyright (C) 2008 Gaëtan Lehmann <gaetan.lehmann@jouy.inra.fr>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#


import xkb, dead_keys, codecs

xkb.tmplValues[u"actionsAndTerminators"] = dead_keys.deadXMLCode
out = codecs.open("fr-dvorak-bepo.bundle/Contents/Resources/fr-dvorak-bepo.keylayout", "w", "utf8")
out.write( xkb.tmpl % xkb.tmplValues )
