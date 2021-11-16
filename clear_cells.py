'''
Take a jupyter notebook file, and clear all the code cells.
Use:
python clear_cells.py <file.ipynb>

if you specify a second arguments, the source file will not change
but by default, the source file will be cleared from code cells.
'''

# TODO: Managing exceptions, cleaning code.

import sys
import nbformat as nbf

nb_args = len(sys.argv)

if nb_args >= 2 and sys.argv[1][-6:] == '.ipynb':
    src_file = sys.argv[1]
    ntbk = nbf.read(src_file, nbf.NO_CONVERT)
    new_ntbk = ntbk
    new_ntbk.cells = [cell if cell.cell_type == "markdown" else nbf.v4.new_code_cell() for cell in ntbk.cells ]
    if nb_args >= 3 :
        output_file = ''
        if sys.argv[2][-6:] == '.ipynb':
            output_file = sys.argv[2]
        else:
            output_file = sys.argv[2] + ".ipynb"
        nbf.write(new_ntbk, output_file, version=nbf.NO_CONVERT)
    else:
        nbf.write(new_ntbk, src_file, version=nbf.NO_CONVERT)