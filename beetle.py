# coding: utf-8
import os, subprocess, sublime, sublime_plugin

NODE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'run.js')

class BeetleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.insert(edit, 0, "111111\n")
    isWindows = platform.system() == 'Windows'
    self.view.insert(edit, 0, "222222\n")
    args = ['node', NODE_PATH, slef.view.fiel_name()]
    self.view.insert(edit, 0, "333333\n")
    p = subprocess.Popen(args, stdout=subprocess.PIPE, shell=isWindows).communicate()[0]
    self.view.insert(edit, 0, "444444\n")
    if(p) sublime.error_message('bettle error:\n%s' % p.decode('utf-8'))



