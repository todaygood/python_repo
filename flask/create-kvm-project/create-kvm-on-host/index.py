#!flask/bin/python

from flask import Flask, jsonify, request
import redis
import logging
import json

logging.basicConfig(level=logging.DEBUG,
                    filename='./service.log',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
app = Flask(__name__)

vm_list= [
  { 'name': 'ntp-01', 'cpu': 2},
  { 'name': 'ntp-02', 'cpu': 2}
]


@app.route('/vm/list')
def get_vm_list():
    logging.info("log get_vm_list")
    print("print get_vm_list")
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


@app.route('/vm/create', methods=['POST'])
def create_vm():
  vm_list.append(request.get_json())
  return '', 204





#logging.critical("This is a critical Message")
#logging.error("This is a error Message")

#logging.root.setLevel(level=logging.INFO)
#logging.info("This is a info Message")

