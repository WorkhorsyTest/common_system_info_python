
import platform
import sys, os


print('CPU:')
print(platform.machine())
print(platform.processor())
print(', '.join(platform.architecture()))
print('')

print('OS:')
print(platform.system())
print(sys.platform)
print(os.name)
print('')

print('Distribution:')
print(', '.join(platform.dist()))
print(', '.join(platform.uname()))
print(platform.mac_ver())
print(', '.join(os.uname()))
print('')

