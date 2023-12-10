#!/usr/bin/python3
""" a Fabric script that generates a .tgz
archive from the contents of the web_static
folder of your AirBnB Clone repo"""
from fabric.api import local


def do_pack():
    """A function that generates a .tgz archive"""
    local("if ! [ -d versions ]; then mkdir versions; fi")
    output = local("date +%Y%m%d%M%S", capture=True)
    local(f'tar -cvzf ./versions/web_static_{output}.tgz ./web_static')
