# coding: utf-8
import os, subprocess, sublime, sublime_plugin, platform

NODE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'run.js')

class BeetleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    isWindows = platform.system() == 'Windows'
    args = ['node', NODE_PATH, self.view.file_name()]
    # self.view.insert(edit, 0, NODE_PATH + '\n')
    p = subprocess.Popen(args, stdout=subprocess.PIPE, shell=isWindows).communicate()[0]
    # self.view.insert(edit, 0, "222222\n")
    if(p): sublime.error_message('bettle error:' + p)
