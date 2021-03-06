# -*- coding: utf-8 -*-
__author__ = 'zappyk'

import argparse, configparser

from lib_zappyk._log     import _log
from lib_zappyk._os_file import _pathAbs, _pathJoin, _fileExist, _pathSep, _pathExpanduser

from GoogleSheets               import *
from GoogleSheets.src.constants import *

_project_     = get_project()
_description_ = get_description()

name_conf = '%s-config.ini' % _project_
path_conf = _pathAbs(_pathJoin(['.']))
file_conf = _pathAbs(_pathJoin([path_conf, name_conf]))

name_logs = '%s-logger.ini' % _project_
path_logs = _pathAbs(_pathJoin(['.']))
file_logs = _pathAbs(_pathJoin([path_logs, name_logs]))

def_second_write_wait = str(SLEEP_MULTIPLE_LINE)+'.'+str(AFTER_MULTIPLE_LINE)

###############################################################################
class logger_conf(object):
    logs = None
    ###########################################################################
    def __init__(self, name=None):
        if not _fileExist(file_logs):
            print("File logger %s not found!" % (file_logs))

        self.logs = _log(name, file_logs)

###############################################################################
class parser_args(object):
    args = None
    ###########################################################################
    def __init__(self):
        parser = argparse.ArgumentParser(description=_description_)
    #CZ#pgroup = parser.add_mutually_exclusive_group()

    #CZ#pgroup.add_argument('-p'     , '--power'             , help='display a power of a given number' , type=int, choices=[1,2,3,4,5])
    #CZ#pgroup.add_argument('-s'     , '--square'            , help='display a square of a given number', type=int)
        parser.add_argument('-d'     , '--debug'             , help='increase output debug'             , action='count'                 , default=0)
        parser.add_argument('-v'     , '--verbose'           , help='output verbosity'                  , action='store_true')
        parser.add_argument('-a'     , '--action'            , help='action for Read/Write or Update'   , type=str, choices=['r','w','u'], required=True)
        parser.add_argument('-sfn'   , '--sht_filename'      , help='spreadsheet file open by NAME'     , type=str                       , default=None)
        parser.add_argument('-sfk'   , '--sht_file_key'      , help='spreadsheet file open by KEY'      , type=str                       , default=None)
        parser.add_argument('-sfu'   , '--sht_file_url'      , help='spreadsheet file open by URL'      , type=str                       , default=None)
        parser.add_argument('-wsn'   , '--wks_name'          , help='worksheet name open'               , type=str                       , default=None)
        parser.add_argument('-cfn'   , '--csv_filename'      , help='CSV file name on action Write/Read', type=str                       , default=None)
        parser.add_argument('-cdl'   , '--csv_delimiter'     , help='CSV file delimiter char fields'    , type=str                       , default=None)
        parser.add_argument('-cqc'   , '--csv_quotechar'     , help='CSV file quote char fields'        , type=str                       , default=None)
        parser.add_argument('-clt'   , '--csv_lineterminator', help='CSV file line terminator'          , type=str                       , default=None)
        parser.add_argument('-wrr'   , '--wks_rows_resize'   , help='worksheet rows resize after Write' , action='store_true')
        parser.add_argument('-wcu'   , '--wks_cell_update'   , help='worksheet cell update action Write', action='store_true')
        parser.add_argument('-aww'   , '--action_write_wait' , help='action wait through Write'         , action='store_true')
        parser.add_argument('-sww'   , '--second_write_wait' , help='second wait through Write'         , type=str                       , default=def_second_write_wait)
    #CZ#parser.add_argument('name'   , help='Name')
    #CZ#parser.add_argument('surname', help='Surname')

        args = parser.parse_args()

        self.args = args

###############################################################################
class parser_conf(object):
    conf = None
    ###########################################################################
    def __init__(self):
        conf = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

        if not _fileExist(file_conf):
            print("File configuration %s not found!" % (file_conf))
            conf = None
        else:
            conf.read(file_conf)
            conf = self.parser_conf_init(conf, 'Os', 'path_join', _pathSep())
            conf = self.parser_conf_init(conf, 'Os', 'path_home', _pathExpanduser('~'))

        self.conf = conf

    ###############################################################################
    def parser_conf_init(self, parser, section, option, value_new):
        value_old = parser.get(section, option, fallback=None)
        if value_old is None:
            parser.set(section, option, value_new)
        return(parser)
