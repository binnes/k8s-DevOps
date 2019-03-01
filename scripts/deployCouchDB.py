import json
import os
import sys
import string
import subprocess
import threading
import time
import socket


def log(txt):
    sys.stdout.write('{}\n'.format(txt)) ; sys.stdout.flush()

def runLocalCommand(cmd):
    ret = os.system('{}'.format(cmd))
    log('Ran local command <<{}>>, return code = {}'.format(cmd, ret))
    return ret

def runRemoteCommand(host, cmd):
    ret = os.system('ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -q pi@{} "{}"'.format(host, cmd)) 
    log('Ran remote command <<{}>> on host {}, return code = {}'.format(cmd, host, ret))
    return ret 

def runRemoteCommandWithReturn(host, cmd):
    sys.stdout.write('Running remote command <<{}>> on host {}\n'.format(cmd, host)) ; sys.stdout.flush()
    return subprocess.check_output('ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -q pi@{} "{}"'.format(host, cmd), shell=True, executable='/bin/bash').decode("utf-8").strip(string.whitespace)

with open('scripts/config.json') as f:
    config = json.load(f)


runRemoteCommand(config["kubernetes"]["kubectlHost"], "helm install --name couchdb --set persistentVolume.enabled=true,image.repository=treehouses/couchdb,helperImage.repository=timotto/rpi-couchdb-statefulset-assembler,helperImage.tag=latest,ingress.enabled=true,ingress.hosts[0]=couchdb.bik8s.home,adminUsername=admin,adminPassword=d0rset,service.type=LoadBalancer incubator/couchdb")
time.sleep(120)
runRemoteCommand(config["kubernetes"]["kubectlHost"], """kubectl exec --namespace default -it couchdb-couchdb-0 -c couchdb -- curl -s     http://127.0.0.1:5984/_cluster_setup     -X POST     -H "Content-Type: application/json"     -d '{"action": "finish_cluster"}' -u admin""")
                