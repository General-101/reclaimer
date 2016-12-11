from traceback import format_exc
from os.path import dirname

# import Binilla first to make sure the constants are injected
from supyr_struct.apps.binilla.app_window import Binilla
from supyr_struct.defs.constants import *
from ..handler import GdlHandler
from .widget_picker import *


class GdlBinilla(Binilla):
    app_name = 'GDL Binilla'
    log_filename = 'gdl_binilla.log'

    config_path = dirname(__file__) + '%sgdl_binilla.cfg' % PATHDIV

    widget_picker = def_gdl_widget_picker

    def __init__(self, *args, **kwargs):
        self.debug = kwargs.pop('debug', self.debug)
        kwargs['handler'] = GdlHandler(debug=self.debug)
        Binilla.__init__(self, *args, **kwargs)
