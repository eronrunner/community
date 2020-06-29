"""
  Handle source files path for any resources
"""

import pathlib

# Specify root app path
_ROOT = str(pathlib.Path(__file__).parent)
_ROOT_RESOURCES = "resources"
_CREDENTIALS = "credentials"

def get_resource(*path):
  return "/".join(path)

def get_credentials(file_name):
  return "/".join([_ROOT, _ROOT_RESOURCES, _CREDENTIALS, file_name])

