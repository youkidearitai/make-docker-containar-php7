# -*- coding: utf-8 -*-
from fabric.api import local, settings, abort, run, cd, env, hosts

def buildall():
    build_base()
    build_php7()

def build_base():
    local("sudo docker build -t youkidearitai/php7-tmcmaker:build -f Dockerfile.base .")

def build_php7():
    local("sudo docker build -t youkidearitai/php7-tmcmaker:latest .")

def push():
    local("sudo docker push youkidearitai/php7-tmcmaker")

# デプロイを行う
@hosts("tekitoh.sakura")
def deploy():
    # ssh_configを使えるようにする
    env.use_ssh_config = True

    # 文字通りcd
    with cd("/home/tekitoh/"):
        run("sudo docker pull youkidearitai/php7-tmcmaker")
        run("sudo docker build -t youkidearitai/php7-tmcmaker:php7-tmcmaker /home/tekitoh/")
        run("sudo systemctl stop php7-tmcmaker-docker.service")
        run("sudo systemctl start php7-tmcmaker-docker.service")

