"""
Contains IASystem DAO implementations.
"""

import logging
import os
from os.path import abspath, dirname
from restclients_core.dao import DAO
from django.conf import settings


def IASystem_DAO(campus):
    return {
        "seattle": IASystem_UW_DAO,
        "bothell": IASystem_UWB_DAO,
        "tacoma": IASystem_UWT_DAO
    }[campus]()


class IASystem_UW_DAO(DAO):
    def service_name(self):
        print os.path.join('iasystem', 'uw')
        return os.path.join('iasystem', 'uw')

    def service_mock_paths(self):
        return [abspath(os.path.join(dirname(__file__), "resources"))]


class IASystem_UWB_DAO(DAO):
    def service_name(self):
        return os.path.join('iasystem', 'uwb')

    def service_mock_paths(self):
        return [abspath(os.path.join(dirname(__file__), "resources"))]


class IASystem_UWT_DAO(DAO):
    def service_name(self):
        return os.path.join('iasystem', 'uwt')

    def service_mock_paths(self):
        return [abspath(os.path.join(dirname(__file__), "resources"))]
