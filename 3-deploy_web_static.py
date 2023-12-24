#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the
function do_deploy:"""
from fabric.api import run, env, put, local
import os
""" Fabric script (based on"""
env.hosts = ["54.152.81.82", "3.94.185.211"]


def do_pack():
    """A function that generates a .tgz archive"""
    local("if ! [ -d versions ]; then mkdir versions; fi")
    output = local("date +%Y%m%d%M%S", capture=True)
    value = local(f'tar -cvzf ./versions/web_static_{output}.tgz\
 ./web_static', capture=True)
    return f"./versions/web_static_{output}.tgz"


def do_deploy(archive_path):
    """Returns False if the file at
    the path archive_path doesn’t exist"""
    if not os.path.isfile(archive_path):
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    output = local("date +%Y%m%d%M%S", capture=True)
    if put(archive_path, "/tmp/").failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}"
           .format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C\
            /data/web_static/releases/{}".format(file, name)).failed is True:
        return False
    if run("sudo rm -rf /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{} /data/web_static/current".
           format(name)).failed is True:
        return False
    if run("sudo service nginx restart").failed:
        return False
    return True


def deploy():
    """creates and distributes an archive
    to your web servers, using the function deploy:"""

    path = do_pack()
    print(path)
    status = do_deploy(path)
    return status
