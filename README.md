# common_system_info_python

Getting common info from different Operating Systems using Python 2 & 3:

FIXME: Add a way to get:
* release info
* host name: socket.gethostname()
* cpu bits

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
platform.mac_ver()
platform.linux_distribution()
sys.platform # OS
os.name # Distribution
os.uname() # Distribution
~~~
