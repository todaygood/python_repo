#!/bin/sh


curl -kv  http://localhost:5000/vm/list

curl -X POST -H "Content-Type: application/json" -d '{
  "name": "lottery",
  "cpu": 10
}' http://localhost:5000/vm/create


curl -kv  http://localhost:5000/vm/list

