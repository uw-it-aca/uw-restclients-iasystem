"""
Contains IASystem DAO implementations.
"""

import logging
import os
from os.path import abspath, dirname
from restclients_core.dao import DAO


class IASystem_DAO(DAO):
    def service_name(self):
        return 'iasystem'

    def service_mock_paths(self):
        return [abspath(os.path.join(dirname(__file__), "resources"))]
