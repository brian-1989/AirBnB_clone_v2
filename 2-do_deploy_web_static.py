#!/usr/bin/python3
""" Distributes an archive to your web servers.

"""

from fabric.api import *
import os

env.hosts = ['54.234.166.77']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ This function distributes an archive to your web servers.

    """
    # Check if the file exists
    if not os.path.exists(archive_path):
        return False
    # From the archive_path variable, the name of the archive is extracted
    file_name_tgz = archive_path.split('/')
    file_name = file_name_tgz[1].split('.')
    # Upload the file in the directory /tmp/
    upload_file = put(archive_path, "/tmp/")
    if upload_file.failed:
        return False
    # Create the path to uncompress the file
    create_path = run(
        "mkdir -p /data/web_static/releases/{}".format(
            file_name[0]))
    if create_path.failed:
        return False
    # probar con create_path
    uncompress_file = run(
        "tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
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
            /data/web_static/releases/{}/".format(
                file_name[0], file_name[0]))
    if move_file.failed:
        return False
    # Delete symbolic_link
    delete_path = run(
        "rm -rf /data/web_static/releases/{}/web_static".format(
            file_name[0]))
    if delete_path.failed:
        return False
    delete_symbolic_link = run("rm -rf /data/web_static/current")
    if delete_symbolic_link.failed:
        return False
    # Create new symbolic_link
    new_symbolic_link = run(
        "ln -s /data/web_static/releases/{}\
            /data/web_static/current".format(file_name[0]))
    if new_symbolic_link.failed:
        return False
    return True
