#!/usr/bin/python3
""" Compress a folder to a file.tgz.

"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """ This function generate an file with extension (.tgz) to compress
    a folder.

    """
    date = str(datetime.now())
    # The date is oganized
    date = date.replace("-", "").replace(" ", "").replace(":", "").replace(".", "")
    # Condition to check if the folder exists
    if not os.path.exists('versions'):
        os.makedirs('versions')
    # The path of file is organized
    path_file = "./versions/web_static_{}.tgz".format(date)
    print("Packing web_static to {}".format(path_file))
    # Compress a folder to a file.tgz
    file_tgz = local("tar -czvf {} web_static".format(path_file))
    # Check if the archive has been correctly generated
    if file_tgz.failed:
        return None
    else:
        size_file = os.path.getsize(path_file)
        print("web_static packed: {} -> {}Bytes".format(path_file, size_file))
        return "./{}".format(file_tgz)