#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# produit le fichier dead.conf
#
# Copyright (C) 2008 Gaëtan Lehmann <gaetan.lehmann@jouy.inra.fr>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#


import dead_keys, compose, sys
f = file("dead.conf", "w")

for m in sorted([m for m in dead_keys.dmm if len(m) == 1]):
  deadName = "dead_" + m[0].replace("ringabove", "abovering")
  print >> f, "# %s" % deadName
  print >> f
  for k, mods in sorted(dead_keys.dc):
    if mods == m and dead_keys.dc.has_key((k, ())):
      print >> f, "L!%s\t%s\t%s" % (deadName, compose.name(dead_keys.dc[k, ()]), compose.name(dead_keys.dc[k, mods]))
    elif m[0] in mods:
      K = (k, tuple(a for a in mods if a != m[0]))
      if dead_keys.dc.has_key(K):
        print >> f, "L!%s\t%s\t%s" % (deadName, compose.name(dead_keys.dc[K]), compose.name(dead_keys.dc[k, mods]))
  print >> f
  