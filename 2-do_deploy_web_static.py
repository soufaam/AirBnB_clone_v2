#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the
function do_deploy:"""
from fabric.api import run, env
from fabric import Connection
import os

env.user = 'ubuntu'
env.hosts = ["54.152.81.82", "3.94.185.211"]
env.ssh_key = "~/.ssh/school"
def do_deploy(archive_path):
   """Returns False if the file at the path archive_path doesn’t exist"""
   if not os.path.exists(archive_path):
      return False
   with Connection(env.hosts, user=env.user,
                      connect_kwargs={'key_filename':env.ssh_key}) as conn:
      res1 = conn.put(archive_path, " /tmp/")
      res2 = conn.run("sudo tar -xzf web_static_*.tgz /data/web_static/releases/")
      res3 = conn.run("sudo rm -rf /tmp/*.tgz")
      res4 = conn.run("sudo rm -rf /data/web_static/current")
      res5 = conn.run("sudo ln -s /data/web_static/releases/test/\
               /data/web_static/current")
      if not res1.return_code and res2.return_code and res3.return_code\
         and res4.return_code and res5.return_code:
         return True
      else:
         return False
