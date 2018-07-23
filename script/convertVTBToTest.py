import os
import shutil

####################################
# This module converts  VTB test
#   to
###################################

###############################
#  Input
###############################
src_dir = r"E:\SourceCode\ObjectTracking\dataset\online\VisualTrackerBenchmark\Girl"
tar_dir = r"E:\SourceCode\ObjectTracking\dataset\testFormat\Girl"

###############################
#  Util
###############################
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def absoluteFilePaths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
###############################
#  main
###############################
def covnertVTBToTest():
    mkdir(tar_dir)

    image_src_dir = src_dir + "\\img"
    image_tar_dir = tar_dir + "\\img"
    mkdir(image_tar_dir)

    copytree(image_src_dir,image_tar_dir)

    filepath =  tar_dir + "\\images.txt"
    thefile = open(filepath, 'w')

    paths = absoluteFilePaths(image_tar_dir)
    for path in paths:
        print(path)
        thefile.write(path + "\n")

if __name__ == "__main__":
    covnertVTBToTest()
