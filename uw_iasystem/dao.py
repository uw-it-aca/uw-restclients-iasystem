"""
Contains IASystem DAO implementations.
"""

import logging
import os
from os.path import abspath, dirname
from restclients_core.dao import DAO
from uw_iasystem.models import Evaluation


SERVICE_PREFIX = 'iasystem_'


class IASystem_UW_DAO(DAO):
    def service_name(self):
        return SERVICE_PREFIX + Evaluation.DOMAIN_SEA

    def service_mock_paths(self):
        return [abspath(os.path.join(dirname(__file__), "resources"))]


class IASystem_UWB_DAO(IASystem_UW_DAO):
    def service_name(self):
        return SERVICE_PREFIX + Evaluation.DOMAIN_BOT


class IASystem_UWT_DAO(IASystem_UW_DAO):
    def service_name(self):
        return SERVICE_PREFIX + Evaluation.DOMAIN_TAC


class IASystem_UWEO_AP_DAO(IASystem_UW_DAO):
    def service_name(self):
        return SERVICE_PREFIX + Evaluation.DOMAIN_EO_AP


class IASystem_UWEO_IELP_DAO(IASystem_UW_DAO):
    def service_name(self):
        return SERVICE_PREFIX + Evaluation.DOMAIN_EO_IELP


DAOs = [IASystem_UW_DAO(),
        IASystem_UWB_DAO(),
        IASystem_UWT_DAO(),
        IASystem_UWEO_AP_DAO(),
        IASystem_UWEO_IELP_DAO()]
DAO_DICT = {
    "seattle": [IASystem_UW_DAO()],
    "bothell": [IASystem_UWB_DAO()],
    "tacoma": [IASystem_UWT_DAO()],
    "pce": [IASystem_UWEO_AP_DAO(), IASystem_UWEO_IELP_DAO()]
    }


def IASystem_DAO(campus):
    if campus is None:
        return DAOs
    return DAO_DICT[campus]
