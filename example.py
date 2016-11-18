#!/usr/bin/python3

"""
This is a sample script which uses libduplicity.py module.
"""

from libduplicity import DupTask

dt = DupTask("~/tmp/test-data",
  "scp://backup-test@backup01.testserver/data/backup-test")
dt.backup()

