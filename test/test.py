
import os, subprocess

NODE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../run.js')
args = ['node', NODE_PATH, 'this is path']
p = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False).communicate()[0]
print(p)
