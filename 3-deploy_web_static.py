#!/usr/bin/python3
""" Script to creates and distributes an archive to your web servers.

"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['34.75.30.56', '54.234.166.77']
env.user = 'ubuntu'


def do_pack():
    """ This function generate an file with extension (.tgz) to compress
    a folder.

    """
    date = str(datetime.now())
    # The date is oganized
    date = date.replace("-", "").replace(" ", "").\
        replace(":", "").replace(".", "")
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


def do_deploy(archive_path):
    """ This function distributes an archive to your web servers.

    """
    # From the archive_path variable, the name of the archive is extracted
    file_name_tgz = archive_path.split('/')
    file_name = file_name_tgz[1].split('.')
    # Check if the file exists
    if not os.path.exists(archive_path):
        return False
    # Upload the file in the directory /tmp/
    upload_file = put(archive_path, "/tmp/")
    if upload_file.failed:
        return False
    # Create the path to uncompress the file
    create_path = run(
        "mkdir -p /data/web_static/releases/{}/".format(
            file_name[0]))
    if create_path.failed:
        return False
    # probar con create_path
    uncompress_file = run(
        "tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            file_name_tgz[1], file_name[0]))
    if uncompress_file.failed:
        return False
    # Delete the file
    delete_file = run("rm /tmp/{}".format(file_name_tgz[1]))
    if delete_file.failed:
        return False
    # Mover the file
    move_file = run(
        "mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}".format(
                file_name[0], file_name[0]))
    if move_file.failed:
        return False
    # Delete symbolic_link
    delete_symbolic_link = run("rm -rf /data/web_static/current")
    if delete_symbolic_link.failed:
        return False
    # Create new symbolic_link
    new_symbolic_link = run(
        "ln -s -f /data/web_static/releases/{}\
            /data/web_static/current".format(file_name[0]))
    if new_symbolic_link.failed:
        return False
    return True


def deploy():
    """ This function pass the result of the do_pack function
    to the do_deploy function.

    """
    result_do_pack = do_pack()
    if result_do_pack is None:
        return False
    return(do_deploy(result_do_pack))
