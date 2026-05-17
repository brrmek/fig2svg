# fig2svg
# Magnus Ek 2026
#

import re

def readFigFile():
  # fig fiel is in ascii format so a simple fopen is usfficient.
  pass

def parseFigFile():
  # The fig ile has a command on each line. Keep track of latest selected font, color, line etc.
  # font, color etc will be replaced by css in a header and referenced inside the svg commands
  # All phase boundarises will be parsed into a path. ToDo if coloring of an area is wanted one may close the path by extending the area along x- and y-axis etc.
  pass

def saveSvgFile():
  # Save the svg file with the same name as the fig file.
  pass

