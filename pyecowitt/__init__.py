""" Nothing to see here """
import sys

__version__ = "0.21"

__uri__ = 'https://github.com/garbled1/pyecowitt'
__title__ = "pyecowitt"
__description__ = 'Interface Library for Ecowitt Protocol'
__doc__ = __description__ + " <" + __uri__ + ">"
__author__ = 'Tim Rightnour'
__email__ = 'root@garbled.net'
__license__ = "Apache 2.0"

__copyright__ = "Copyright (c) 2020,2021 Tim Rightnour"

from .ecowitt import (
    EcoWittSensor,
    EcoWittListener,
    WINDCHILL_OLD,
    WINDCHILL_NEW,
    WINDCHILL_HYBRID,
)

if __name__ == '__main__': print(__version__)
