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
platform.processor() # CPU: Wildly inconsistent results. Processor brand, name or usually nothing.
platform.mac_ver()
sys.platform # OS: Legacy cruft. Sometimes mixes OS release info in with the OS name E.G. win32, linux, linux4
os.name # Distribution: Not useful. Only provides 'posix', 'nt', 'ce', 'java'
os.uname() # Distribution: Truncates host name to 8 characters sometimes
~~~

Deprecated:
~~~python
platform.dist() # OS: Deprecated since version 3.5, will be removed in version 3.7
platform.linux_distribution() # Same as platform.dist()
~~~
