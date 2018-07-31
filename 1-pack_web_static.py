#!/usr/bin/python3
# Fabric script generating .tgz archive from the web_static folder
from datetime import datetime
from fabric.api import *

env.hosts = ["localhost"]


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
