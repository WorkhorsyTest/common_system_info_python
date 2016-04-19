# common_system_info_python

Getting common info from different Operating Systems using Python:

FIXME: Add a way to get release info and host name:
socket.gethostname()

Use:
~~~python
platform.machine() # CPU
platform.system() # OS
platform.uname() # Distribution
~~~

Don't Use:
~~~python
platform.processor() # CPU
platform.dist() # OS
sys.platform # OS
os.name # Distribution
os.uname() # Distribution
~~~
