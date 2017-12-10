from unittest import TestCase
from uw_iasystem.dao import IASystem_DAO, IASystem_UW_DAO, IASystem_UWB_DAO,\
    IASystem_UWT_DAO, IASystem_UWEO_AP_DAO, IASystem_UWEO_IELP_DAO


class IASystemDaoTest(TestCase):

    def test_get_dao(self):
        self.assertEqual(len(IASystem_DAO(None)), 5)
        self.assertTrue(isinstance(IASystem_DAO("Seattle")[0],
                                   IASystem_UW_DAO))
        self.assertTrue(isinstance(IASystem_DAO("Bothell")[0],
                                    IASystem_UWB_DAO))
        self.assertTrue(isinstance(IASystem_DAO("Tacoma")[0],
                                    IASystem_UWT_DAO))
        self.assertTrue(isinstance(IASystem_DAO("PCE_AP")[0],
                                    IASystem_UWEO_AP_DAO))
        self.assertTrue(isinstance(IASystem_DAO("PCE_OL")[0],
                                    IASystem_UWEO_AP_DAO))
        self.assertTrue(isinstance(IASystem_DAO("PCE_IELP")[0],
                                    IASystem_UWEO_IELP_DAO))
        self.assertEqual(len(IASystem_DAO("pce")), 2)
