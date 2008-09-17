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

import xkb, dead_keys, codecs, unicodedata
from terminators import terminators, combiningTerminators, spaceTerminators


header = u"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://web.resource.org/cc/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="297mm" height="210mm" id="svg3276" sodipodi:version="0.32" inkscape:version="0.45.1" sodipodi:docbase="/home/nicolas/work/dvorak_nb" sodipodi:docname="dvorak_nb_blank.svg" inkscape:output_extension="org.inkscape.output.svg.inkscape">
  <defs id="defs3278"/>
  <sodipodi:namedview inkscape:document-units="mm" pagecolor="#ffffff" bordercolor="#666666" borderopacity="1.0" inkscape:pageopacity="0.0" inkscape:pageshadow="2" inkscape:zoom="0.65806102" inkscape:cx="614.00827" inkscape:cy="450.09753" inkscape:current-layer="layer1" id="namedview3280" showguides="true" inkscape:guide-bbox="true" inkscape:window-width="990" inkscape:window-height="585" inkscape:window-x="0" inkscape:window-y="332"/>
  <metadata id="metadata3282">
    <rdf:RDF>
      <cc:Work rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g inkscape:label="Layer 1" inkscape:groupmode="layer" id="layer1">

    <rect style="opacity: 1; fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="rect3285" width="52.671261" height="52.671261" x="36.852917" y="129.41629" rx="7.7852464"/>
    <rect rx="7.7852464" y="129.41629" x="102.75843" height="52.671261" width="52.671261" id="use3769" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="129.41629" x="168.66394" height="52.671261" width="52.671261" id="use3771" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="129.41629" x="234.56946" height="52.671261" width="52.671261" id="use3773" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="129.41629" x="300.47498" height="52.671261" width="52.671261" id="use3775" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="129.41629" x="366.38049" height="52.671261" width="52.671261" id="use3777" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="129.41629" x="432.28601" height="52.671261" width="52.671261" id="use3779" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="129.41629" x="498.1915" height="52.671261" width="52.671261" id="use3781" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="129.41629" x="564.09705" height="52.671261" width="52.671261" id="use3783" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="129.41629" x="630.00256" height="52.671261" width="52.671261" id="use3785" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="129.41629" x="695.90802" height="52.671261" width="52.671261" id="use3787" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="129.41629" x="761.81354" height="52.671261" width="52.671261" id="use3789" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="129.41629" x="827.71906" height="52.671261" width="52.671261" id="use3791" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="196.81883" x="128.68188" height="52.671261" width="52.671261" id="use3797" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="264.22134" x="145.41165" height="52.671261" width="52.671261" id="use3799" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="196.75412" x="194.43207" height="52.671261" width="52.671261" id="use3801" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="196.75412" x="260.18225" height="52.671261" width="52.671261" id="use3803" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="196.75412" x="325.93243" height="52.671261" width="52.671261" id="use3805" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="196.75412" x="391.68259" height="52.671261" width="52.671261" id="use3807" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="196.75412" x="457.43277" height="52.671261" width="52.671261" id="use3809" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="196.75412" x="523.18292" height="52.671261" width="52.671261" id="use3811" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="196.75412" x="588.93311" height="52.671261" width="52.671261" id="use3813" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="196.75412" x="654.68329" height="52.671261" width="52.671261" id="use3815" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="196.75412" x="720.43347" height="52.671261" width="52.671261" id="use3817" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="196.75412" x="786.18365" height="52.671261" width="52.671261" id="use3819" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="196.75412" x="851.93384" height="52.671261" width="52.671261" id="use3821" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="331.62384" x="111.16536" height="52.671261" width="52.671261" id="use3847" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="264.22134" x="211.31717" height="52.671261" width="52.671261" id="use3849" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="264.22134" x="277.22269" height="52.671261" width="52.671261" id="use3851" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="264.22134" x="343.1282" height="52.671261" width="52.671261" id="use3853" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="264.22134" x="409.03369" height="52.671261" width="52.671261" id="use3855" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="264.22134" x="474.93921" height="52.671261" width="52.671261" id="use3857" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="264.22134" x="540.84473" height="52.671261" width="52.671261" id="use3859" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="264.22134" x="606.75024" height="52.671261" width="52.671261" id="use3861" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="264.22134" x="672.65576" height="52.671261" width="52.671261" id="use3863" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="264.22134" x="738.56128" height="52.671261" width="52.671261" id="use3865" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="264.22134" x="804.4668" height="52.671261" width="52.671261" id="use3867" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="264.22134" x="870.37231" height="52.671261" width="52.671261" id="use3869" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="331.62384" x="177.07086" height="52.671261" width="52.671261" id="use3899" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="331.62384" x="242.97638" height="52.671261" width="52.671261" id="use3901" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="331.62384" x="308.8819" height="52.671261" width="52.671261" id="use3903" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="331.62384" x="374.78741" height="52.671261" width="52.671261" id="use3905" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="331.62384" x="440.69293" height="52.671261" width="52.671261" id="use3907" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="331.62384" x="506.59845" height="52.671261" width="52.671261" id="use3909" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="331.62384" x="572.50397" height="52.671261" width="52.671261" id="use3911" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="331.62384" x="638.40948" height="52.671261" width="52.671261" id="use3913" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="331.62384" x="704.315" height="52.671261" width="52.671261" id="use3915" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect rx="7.7852464" y="331.62384" x="770.22046" height="52.671261" width="52.671261" id="use3917" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" ry="7.7852464"/>
    <rect style="opacity: 1; fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="rect3921" width="76.483505" height="52.671261" x="36.852917" y="196.88356" rx="7.7852464" inkscape:tile-w="54.921261" inkscape:tile-h="54.921261" inkscape:tile-cx="47.065393" inkscape:tile-cy="155.75194" ry="7.7852464"/>
    <rect style="opacity: 1; fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="rect3923" width="93.681244" height="52.671261" x="36.852917" y="264.22134" rx="7.7852464" inkscape:tile-w="54.921261" inkscape:tile-h="54.921261" inkscape:tile-cx="47.065393" inkscape:tile-cy="155.75194" ry="7.7852464"/>
    <rect style="opacity: 1; fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="rect3925" width="61.93158" height="52.671261" x="36.852917" y="331.62384" rx="7.7852464" inkscape:tile-w="54.921261" inkscape:tile-h="54.921261" inkscape:tile-cx="47.065393" inkscape:tile-cy="155.75194" ry="7.7852464"/>
    <rect style="opacity: 1; fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="rect4021" width="73.8377" height="52.671261" x="36.852917" y="399.8042" rx="7.7852464" inkscape:tile-w="54.921261" inkscape:tile-h="54.921261" inkscape:tile-cx="47.065393" inkscape:tile-cy="155.75194" ry="7.7852464"/>
    <rect style="opacity: 1; fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="rect4023" width="61.93158" height="52.671261" x="125.78251" y="399.8042" rx="7.7852464" inkscape:tile-w="54.921261" inkscape:tile-h="54.921261" inkscape:tile-cx="47.065393" inkscape:tile-cy="155.75194" ry="7.7852464"/>
    <rect style="opacity: 1; fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="rect4025" width="61.93158" height="52.671261" x="202.44826" y="399.8042" rx="7.7852464" inkscape:tile-w="54.921261" inkscape:tile-h="54.921261" inkscape:tile-cx="47.065393" inkscape:tile-cy="155.75194" ry="7.7852464"/>
    <rect ry="7.7852464" inkscape:tile-cy="155.75194" inkscape:tile-cx="47.065393" inkscape:tile-h="54.921261" inkscape:tile-w="54.921261" rx="7.7852464" y="399.8042" x="276.44827" height="52.671261" width="380.75113" id="rect4027" style="opacity: 1; fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;"/>
    <rect ry="7.7852464" inkscape:tile-cy="155.75194" inkscape:tile-cx="47.065393" inkscape:tile-h="54.921261" inkscape:tile-w="54.921261" rx="7.7852464" y="399.8042" x="668.93488" height="52.671261" width="61.93158" id="rect4029" style="opacity: 1; fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;"/>
    <rect style="opacity: 1; fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="rect4031" width="61.93158" height="52.671261" x="744.34033" y="399.8042" rx="7.7852464" inkscape:tile-w="54.921261" inkscape:tile-h="54.921261" inkscape:tile-cx="47.065393" inkscape:tile-cy="155.75194" ry="7.7852464"/>
    <rect ry="7.7852464" inkscape:tile-cy="155.75194" inkscape:tile-cx="47.065393" inkscape:tile-h="54.921261" inkscape:tile-w="54.921261" rx="7.7852464" y="399.8042" x="818.42285" height="52.671261" width="61.93158" id="rect4033" style="opacity: 1; fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;"/>
    <rect style="opacity: 1; fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="rect4035" width="101.47603" height="52.671261" x="893.49506" y="399.8042" rx="7.7852459" inkscape:tile-w="54.921261" inkscape:tile-h="54.921261" inkscape:tile-cx="47.065393" inkscape:tile-cy="155.75194" ry="7.7852464"/>
    <rect ry="7.7852464" style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="rect4037" width="101.10686" height="52.671261" x="893.8642" y="129.41629" rx="7.7852464"/>
    <path style="fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dashoffset: 0pt; stroke-opacity: 1;" d="M 988.47656,196.75412 C 992.0745,196.75412 994.97105,200.22634 994.97105,204.53937 L 994.97105,309.01172 C 994.97105,313.32475 992.0745,316.79697 988.47656,316.79697 L 940.53987,316.79697 C 940.53987,316.79697 935.63003,314.89201 935.73833,309.01172 C 936.00156,302.56257 935.95117,268.09593 935.83497,254.99658 C 935.71877,249.49531 932.05064,250.16518 932.05064,250.16518 L 920.06233,250.16518 C 917.84389,249.78528 915.94237,246.48507 915.94237,245.7409 C 915.94237,235.49914 915.94237,195.89387 915.94237,205.36586 C 915.61802,197.02595 919.26637,196.75412 921.33585,196.75412 C 938.04154,196.75412 988.47656,196.75412 988.47656,196.75412 z " id="rect4039" sodipodi:nodetypes="ccccccccccccc"/>
    <rect style="opacity: 1; fill: none; fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 2.25; stroke-linecap: square; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0pt; stroke-opacity: 1;" id="rect4048" width="157.70181" height="52.671261" x="837.26917" y="331.62384" rx="7.7852459" inkscape:tile-w="54.921261" inkscape:tile-h="54.921261" inkscape:tile-cx="47.065393" inkscape:tile-cy="155.75194" ry="7.7852464"/>
    <text font-size="19" font-family="DejaVu Sans" style="fill:#000000" x="55.245689" y="230.91899">Tab</text>
    <text font-size="19" font-family="DejaVu Sans" style="fill:#000000" x="42"        y="298.24963">Verr. Maj</text>
    <text font-size="19" font-family="DejaVu Sans" style="fill:#ff0000" x="47.83379"  y="364.66342">Maj</text>
    <text font-size="19" font-family="DejaVu Sans" style="fill:#000000" x="56.095467" y="431.76309">Ctrl</text>
    <text font-size="19" font-family="DejaVu Sans" style="fill:#000000" x="129.02135" y="431.76309">Super</text>
    <text font-size="19" font-family="DejaVu Sans" style="fill:#000000" x="220.45229" y="431.76309">Alt</text>
    <text font-size="19" font-family="DejaVu Sans" style="fill:#003eff" x="672"       y="431.76309">Alt Gr</text>
    <text font-size="19" font-family="DejaVu Sans" style="fill:#000000" x="748"       y="431.76309">Super</text>
    <text font-size="19" font-family="DejaVu Sans" style="fill:#000000" x="823"       y="431.76309">Menu</text>
    <text font-size="19" font-family="DejaVu Sans" style="fill:#000000" x="926.60248" y="431.76309">Ctrl</text>
    <text font-size="19" font-family="DejaVu Sans" style="fill:#ff0000" x="891.62524" y="364.66342">Maj</text>
    <text font-size="19" font-family="DejaVu Sans" style="fill:#000000" x="925"       y="230.91899">Entrée</text>
    <text font-size="13" font-family="DejaVu Sans" style="fill:#000000" x="900.2666"  y="149.31816">Retour Arrière</text>

"""

footer = u"""
  </g>
</svg>
"""

charTmpl = u"""    <text x="%s" y="%s" font-family="DejaVu Sans Mono" font-size="20" style="fill:%s">%s</text>"""

mainColor = "#000000"
shiftColor = "#ff0000"
altgrColor = "#003eff"
altgrShiftColor = "#ca00ff"
deadColor = "#008000"

mainOffset = (45-36.852917, 175-129.41629)
shiftOffset = (45-36.852917, 150-129.41629)
altgrOffset = (70-36.852917, 175-129.41629)
altgrShiftOffset = (70-36.852917, 150-129.41629)


mainChars = u"$\"«»()_+-/*=%^,.'#1234567890@BÉPOÈ!VDLJZWAUIE?CTSRNMÇÊÀYH:K;QGXF—<>[]|&`¨€~\{}…ÆŒÙ°"

keys = [
  ["TLDE", "AE01", "AE02", "AE03", "AE04", "AE05", "AE06", "AE07", "AE08", "AE09", "AE10", "AE11", "AE12"],
  ["AD01", "AD02", "AD03", "AD04", "AD05", "AD06", "AD07", "AD08", "AD09", "AD10", "AD11", "AD12"],
  ["AC01", "AC02", "AC03", "AC04", "AC05", "AC06", "AC07", "AC08", "AC09", "AC10", "AC11", "BKSL"],
  ["LSGT", "AB01", "AB02", "AB03", "AB04", "AB05", "AB06", "AB07", "AB08", "AB09", "AB10"],
  ["SPCE"]
]

firstOffset = [(36.852917, 129.41629), (128.68188, 196.81883), (145.41165, 264.22134), (111.16536, 331.62384), (445, 399.8042)]
xKeyOffset = 102.75843-36.852917


def offset(k):
  for i, line in enumerate(keys):
    if k in line:
      j = line.index(k)
      fo = firstOffset[i]
      return (fo[0] + xKeyOffset*j, fo[1])
  raise "no such key: "+k


def offsetAndColor(k):
  k2 = k.split("_")[0]
  o = offset(k2)
  if "_shift_option" in k:
    so = altgrShiftOffset
    color = altgrShiftColor
  elif "_shift" in k:
    so = shiftOffset
    color = shiftColor
  elif "_option" in k:
    so = altgrOffset
    color = altgrColor
  else:
    so = mainOffset
    color = mainColor
  return (o[0]+so[0], o[1]+so[1], color)


def xmlChar(v):
  if v == u'"':
    v = u"&#x0022;"
  elif v == u'<':
    v = u"&#x003c;"
  elif v == u'&':
    v = u'&#x0026;'
  return v
  
  
out = codecs.open(sys.argv[2]+".svg", "w", "utf8")
print >> out, header
for k, v in xkb.tmplValues.iteritems():
  v2 = terminators.get( v, v )
  if "_capslock" in k or "_command" in k:
   continue
  x, y, color = offsetAndColor(k)
  if terminators.has_key(v):
   color = deadColor
  print >> out, charTmpl % (x, y, color, xmlChar(v2))
print >> out, footer
out.close()


out = codecs.open(sys.argv[2]+"-simplifiee.svg", "w", "utf8")
print >> out, header
for k, v in xkb.tmplValues.iteritems():
  v2 = terminators.get( v, v )
  if "_capslock" in k or "_command" in k:
    continue
  x, y, color = offsetAndColor(k)
  if color == shiftColor and xkb.tmplValues[k.split("_")[0]] == v.lower():
    color = mainColor
  elif color == altgrShiftColor and xkb.tmplValues[k.split("_")[0]+"_option"] == v.lower():
    color = altgrColor
  if terminators.has_key(v):
    color = deadColor
  if ("_option" not in k and v2 in mainChars) or ("_option" in k and v2 in mainChars.lower()) or ("_shift" in k and k.count("_") == 1) or (k.count("_") == 0 and xkb.tmplValues[k+"_shift"] != v2.upper()):
    print >> out, charTmpl % (x, y, color, xmlChar(v2))
print >> out, footer
out.close()


out = codecs.open(sys.argv[2]+"-capslock.svg", "w", "utf8")
print >> out, header
for k, v in xkb.tmplValues.iteritems():
  v2 = terminators.get( v, v )
  if "_capslock" not in k or "_command" in k:
    continue
  x, y, color = offsetAndColor(k)
  if terminators.has_key(v):
    color = deadColor
  print >> out, charTmpl % (x, y, color, xmlChar(v2))
print >> out, footer
out.close()


# find the dead keys used here
dks = set()
for v in xkb.tmplValues.itervalues():
  if terminators.has_key(v):
    dks.add(v)

for m in sorted(dks):
  deadName = "dead_" + m.replace("ringabove", "abovering")
  out = codecs.open(sys.argv[2]+"-"+deadName+".svg", "w", "utf8")
  print >> out, header
  fullMapValues = {}
  for k, mods in sorted(dead_keys.dc):
    if mods == (m,) and dead_keys.dc.has_key((k, ())):
      k2 = dead_keys.dc[k, ()]
      v2 = dead_keys.dc[k, mods]
      for k3, v3 in xkb.tmplValues.iteritems():
        if v3 == k2 and "_capslock" not in k3 and "_command" not in k:
          x, y, color = offsetAndColor(k3)
          print >> out, charTmpl % (x, y, color, xmlChar(v2))
    elif m in mods:
      K = (k, tuple(a for a in mods if a != m))
      if dead_keys.dc.has_key(K):
        k2 = dead_keys.dc[K]
        v2 = dead_keys.dc[k, mods]
        for k3, v3 in xkb.tmplValues.iteritems():
          if v3 == k2 and "_capslock" not in k3 and "_command" not in k:
            x, y, color = offsetAndColor(k3)
            print >> out, charTmpl % (x, y, color, xmlChar(v2))
  for k, v in xkb.tmplValues.iteritems():
    if "_capslock" in k or "_command" in k:
      continue
    x, y, color = offsetAndColor(k)
    if v == u" ":
      print >> out, charTmpl % (x, y, color, xmlChar(spaceTerminators[m]))
    elif v == m:
      print >> out, charTmpl % (x, y, color, xmlChar(terminators[m]))
    elif v == u" ":
      print >> out, charTmpl % (x, y, color, xmlChar(combiningTerminators[m])) 
  print >> out, footer
  out.close()



for i, m1 in enumerate(sorted(dks)):
  for m2 in sorted(dks)[i+1:]:
    s = u""
    for k, mods in sorted(dead_keys.dc):
      if mods == (m1, m2) and dead_keys.dc.has_key((k, ())):
        k2 = dead_keys.dc[k, ()]
        v2 = dead_keys.dc[k, mods]
        for k3, v3 in xkb.tmplValues.iteritems():
          if v3 == k2 and "_capslock" not in k3 and "_command" not in k:
            x, y, color = offsetAndColor(k3)
            s += charTmpl % (x, y, color, xmlChar(v2))
    if s != u"":
      for k, v in xkb.tmplValues.iteritems():
        if "_capslock" in k or "_command" in k:
          continue
        x, y, color = offsetAndColor(k)
        if v == u" ":
          s += charTmpl % (x, y, color, xmlChar(spaceTerminators[m1])+xmlChar(spaceTerminators[m2]))
        elif v == u" ":
          s += charTmpl % (x, y, color, xmlChar(combiningTerminators[m1])+xmlChar(combiningTerminators[m2])) 
      deadName = "+".join("dead_" + m.replace("ringabove", "abovering") for m in (m1, m2))
      out = codecs.open(sys.argv[2]+"-"+deadName+".svg", "w", "utf8")
      print >> out, header
      print >> out, s
      print >> out, footer
      out.close()
