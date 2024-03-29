# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from restclients_core.util.decorators import use_mock
from uw_iasystem.dao import (
    IASystem_UW_DAO, IASystem_UWB_DAO,
    IASystem_UWT_DAO, IASystem_UWEO_AP_DAO, IASystem_UWEO_IELP_DAO)


fdao_ias_override = use_mock(IASystem_UW_DAO(), IASystem_UWB_DAO(),
                             IASystem_UWT_DAO(), IASystem_UWEO_AP_DAO(),
                             IASystem_UWEO_IELP_DAO())
