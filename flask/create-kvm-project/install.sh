#!/bin/sh

yum install -y redis

cp redis.conf  /etc/

systemctl enable redis
systemctl start redis

