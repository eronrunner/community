"""
  Handle source files path for any resources
"""

import pathlib

# Specify root app path
_ROOT = str(pathlib.Path(__file__).parent)
_ROOT_RESOURCES = "resources"

def get_resource(*path):
  return _ROOT.join(*path)

