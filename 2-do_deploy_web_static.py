#!/usr/bin/python3
# Fabric script generating .tgz archive from the web_static folder
from fabric.api import *

env.hosts = ["35.237.169.179", "35.237.190.7"]


def do_pack():
    '''
        pack: create .tgz and return archive path
    '''
    try:
        local("mkdir -p versions/")
        filename = "web_static_{}.tgz"\
            .format(datetime.now().strftime("%Y%m%d%H%M%S"))
        local("tar -cvzf versions/{} web_static".format(filename))
        print(os.path.realpath(os.path.realpath(filename)))
    except:
        return None


def do_deploy():
    '''
        deploy: distributes an archive to your web servers
    '''
    try:
        with cd("/tmp"):
            put("versions/web_static/*.tgz, /tmp")
        run("tar -zxvf /tmp/*.tgz -C /data/web_static/releases/")
        run("rm -r *.tgz")
        run("rm -r /data/web_static/current")
        run("ln -s /data/web_static/releases/ /data/web_static/current")
        return True
    except:
        return False
