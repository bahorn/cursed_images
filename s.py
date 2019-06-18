#!/usr/bin/env python
import random

def cursed(fname, oname):
    img = pdb.gimp_file_load(fname, fname)
    layer = img.layers[0]
    # Create it here
    pdb.gimp_color_balance(layer, 2, True, 100, -75, -75)
    pdb.plug_in_rgb_noise(img, layer, True, True, 0.1, 0.1, 0.1, 0)
    pdb.plug_in_whirl_pinch(img, layer, random.uniform(-50, 50), 0.1, 1.2)
    pdb.plug_in_edge(img, layer, 5.0, random.randint(1, 3), 0)
    pdb.gimp_brightness_contrast(layer, -110, 100)
    pdb.plug_in_wind(img, layer, 25, 0, random.randint(1, 5), 0, 1)
    # Save the file
    img.merge_visible_layers(NORMAL_MODE)
    pdb.gimp_file_save(img, img.layers[0], oname, oname)
    pdb.gimp_image_delete(img)


if __name__ == "__main__":
    import os
    import sys
    import subprocess
    if len(sys.argv) < 2:
        print("you must specify a function to execute!")
        sys.exit(-1)
    scrdir = os.path.dirname(os.path.realpath(__file__))
    scrname = os.path.splitext(os.path.basename(__file__))[0]
    shcode = "import sys;sys.path.insert(0, '" + scrdir + "');import " + \
        scrname + ";" + scrname + "." + sys.argv[1] + str(tuple(sys.argv[2:]))
    shcode = "gimp-console -idf --batch-interpreter python-fu-eval -b \"" + \
        shcode + "\" -b \"pdb.gimp_quit(1)\""
    sys.exit(subprocess.call(shcode, shell=True))
else:
    from gimpfu import *
