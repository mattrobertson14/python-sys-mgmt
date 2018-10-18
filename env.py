import os

print('USER: ' + os.environ['USER'])
print('PATH: ' + os.environ['PATH'])
print('FILE: ' + os.path.basename(__file__))
