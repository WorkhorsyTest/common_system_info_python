# common_system_info_python

Getting common info from different Operating Systems using Python:

Use:
~~~python
platform.machine() # CPU info
platform.uname() # OS version
platform.system() # OS type
~~~

Don't Use:
~~~python
platform.processor() # CPU info
platform.dist() # OS info
sys.platform # OS type
os.name # OS type
os.uname() # OS version
~~~
