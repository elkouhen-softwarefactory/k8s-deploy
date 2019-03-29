#!/usr/bin/python


def removeBackSlash( inString ):
  return inString.replace('\\', '')


class FilterModule(object):
    def filters(self):
        return {
            'removeBackSlash': removeBackSlash
        }
