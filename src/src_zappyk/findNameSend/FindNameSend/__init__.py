# -*- coding: utf-8 -*-
__author__ = 'zappyk'

PROJECT     = 'FindNameSend'
DESCRIPTION = 'Search name in files on path, Send email'
VERSION     = (0, 0, 1, 'beta', 1)
VERSION     = (0, 1, 0, 'rc'  , 1)
VERSION     = (0, 2, 0, 'rc'  , 1)

###########################################################
def get_project():
    return(PROJECT)
###########################################################
def get_description():
    return(DESCRIPTION)
###########################################################
#def get_version():
#   return(VERSION)
###########################################################
#def get_version(*arg, **kwargs):
#   from FindNameSend.src.version import get_version
#   return(get_version(*arg, **kwargs))
###########################################################
def get_version():
    from FindNameSend.src.version import get_version
    return(get_version())
