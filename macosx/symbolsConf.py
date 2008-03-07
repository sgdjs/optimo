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


import sys, compose

out = file("symbols.conf", "w")
for C in sorted(compose.composeChars.keys()):
  code = compose.composeChars[C]
  ucode = repr(C)[2:-1]
  if ucode.startswith(r'\u'):
    ucode = ucode[2:].rjust(4, '0')
    v  = (code, ucode, code, code, ucode)
    s = "\t".join(v) + "\n"
    out.write(s)
