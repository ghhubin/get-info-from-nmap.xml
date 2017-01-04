#!/usr/bin/evn python 
#coding:utf-8 
  
try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 
import sys 
  
try: 
  tree = ET.parse("61.183.0.22-39_20161219_150606.xml")     #打开xml文档 
  root = tree.getroot()         #获得root节点  
except Exception, e: 
  print "Error:cannot parse file:.xml."
  sys.exit(1) 
for host in root.findall('host'): #找到root节点下的所有host节点 
  addr = host.find('address').get('addr')   #子节点下节点address的值 
  state = host.find('status').get('state')      #子节点下属性name的值
  if state != 'up':
    continue
  ports = host.find('ports')
  for port in ports.findall('port'):
    p = ''
    service = ''
    p = port.get('portid')
    if  port.find('service').get('name'):
      service = port.find('service').get('name')
    print addr+'   '+p+'   '+service

