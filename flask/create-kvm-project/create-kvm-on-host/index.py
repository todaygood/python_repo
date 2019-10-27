#!/bin/python
from flask import Flask, jsonify, request
import redis
import json
import subprocess

app = Flask(__name__)

vm_list= [
  { 'name': 'ntp-01', 'cpu': 2},
  { 'name': 'ntp-02', 'cpu': 2}
]




@app.route('/vm/list')
def get_vm_list():
    app.logger.info("log get_vm_list")
    rc = redis.Redis(host='localhost',port=6379,db=0) 
    for vm in vm_list:
        rval = json.dumps(vm)
        rc.set(vm['name'],rval)
    
    true_vm_list=[]
    for vm in vm_list:
        true_vm=rc.get(vm['name'])
        rval = json.loads(true_vm)
        true_vm_list.append(rval)

    print(true_vm_list)
    return jsonify(true_vm_list)


vm_info_dict = {
        'on_host':'192.168.172.133',
        'name':'test0',
        'cpu':1,
        'memory':2,
        'data_disk':50,
        'template': 'http://centos7.qcow2',
        'ip1': '192.168.1.1',
        'ip1_mask':'255.255.255.0',
        'gateway': '192.168.1.254',
        'nic1_bridge': 'virbr0',
        'ip2': '172.16.1.3',
        'ip2_mask':'255.255.255.0',
        'nic2_bridge': 'br-vlan2000',
        'vm_state':'creating',
        'task_state':'creating',
        'xml_file': '/tmp/'
        }

@app.route('/vm/create', methods=['POST'])
def create_vm():
    vm_info_json = request.get_json()
    vm_info_dict = json.loads(vm_info_json)

    do_create_vm(vm_info_dict)

    vm_list.append(request.get_json())
    return '', 204

def generate_xml_from_spec(vm_info_dict):
    subprocess.call(virt-install --ram {{ kvm_vm_ram }} --vcpus {{ kvm_vm_vcpus }} --os-variant rhel7
    --disk path=/var/lib/libvirt/images/{{ kvm_vm_hostname }}.qcow2,device=disk,bus=virtio
    --network none --noautoconsole --vnc --name {{ kvm_vm_hostname }} --cpu host-model --autostart --dry-run --print-xml) 

def do_create_vm(vm_info_dict):
    pass




if __name__ == "__main__":
    handler = logging.FileHandler('service.log', encoding='UTF-8')

    handler.setLevel(logging.DEBUG)

    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')

    handler.setFormatter(logging_format)

    app.logger.addHandler(handler)


