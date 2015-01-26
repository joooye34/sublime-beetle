# coding: utf-8
import sublime, sublime_plugin
import os,platform
from subprocess import Popen, PIPE

NODE_PATH = os.path.join(sublime.packages_path(), os.path.dirname(os.path.realpath(__file__)), 'run.js')
OUTPUT_VALID = "***beetle***"

class BeetleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    args = ['node', NODE_PATH, self.view.file_name()]
    try:
        p = Popen(args, stdout=PIPE, env=self.get_env(), shell= self.is_windows())
    except OSError:
        sublime.error_message('bettle error:Node.js not run!')
    stdout = p.communicate()[0]
    if not stdout: return
    code,data = self.get_output_list(stdout.decode('utf-8'))
    if code == 200 and data:
        region = sublime.Region(0, self.view.size())
        self.view.replace(edit, region, data)
    elif code:
        sublime.error_message('bettle error:' + data)

  def get_env(self):
    env = None
    if self.is_osx():
        env = os.environ.copy()
        env['PATH'] += ':/usr/local/bin'
    return env

  def is_osx(self):
    return platform.system() == 'Darwin'

  def is_windows(self):
    return platform.system() == 'Windows'

  def get_output_list(self, output):
    index = output.find(OUTPUT_VALID)
    code = int(output[:index])
    data = output[index + len(OUTPUT_VALID):len(output) -1]
    return [code, data]

  def clear_view(self):
    for region in self.view.sel():
        if region.empty(): continue
        originalBuffer = self.view.substr(region)

  def set_view(self, string):
    return ''


