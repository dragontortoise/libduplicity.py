#!/usr/bin/python3

"""
libduplicity.py - This is "libduplicity.py" module, and it provides
wrapper for duplicity command line program where you can import into
your python program so you don't have to deal with how to execute
external program yourself.
"""

import subprocess

class DupTask:
  def __init__(self, src, dest, is_encrypted=False):
    """
    Initialize DupTask.  The parameters are mapped with duplicity's
    command line arguments as follows:

      - is_encrypted : --no-encryption
      - src : source_directory
      - dest : target_url

    You can see the list of duplicity's command line arguments from
    'man duplicity'.
    """

    self.src = src
    self.dest = dest
    self.is_encrypted = is_encrypted

  def backup(self):
    if not self.is_encrypted:
      is_encrypted_cmd_opt = "--no-encryption"
    else:
      is_encrypted_cmd_opt = ""

    subprocess.call(["duplicity", is_encrypted_cmd_opt, self.src,
      self.dest])

