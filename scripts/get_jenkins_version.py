#!/usr/bin/python

import jenkins

server = jenkins.Jenkins('http://52.91.47.41:8080', username='czeeb', password='29a9e2fddd9f6fc3973c8a8503f02aed')
version = server.get_version()
print version
