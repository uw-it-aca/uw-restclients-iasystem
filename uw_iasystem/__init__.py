import json
import logging
from restclients_core.exceptions import DataFailureException
from uw_iasystem.dao import IASystem_DAO
from uw_iasystem.exceptions import TermEvalNotCreated


logger = logging.getLogger(__name__)


def get_resource_by_campus(url, campus):
    return get_resource(url, campus)


def get_resource(url, campus):
    """
    Issue a GET request to IASystem with the given url
    and return a response in Collection+json format.
    :returns: http response with content in json
    """
    headers = {"Accept": "application/vnd.collection+json"}
    response = IASystem_DAO(campus).getURL(url, headers)

    logger.info("%s ==status==> %s" % (url, response.status))

    if response.status != 200:
        logger.error("%s ==data==> %s" % (url, response.data))
        raise DataFailureException(url, response.status, response.data)

    if '"error":' in response.data:
        content = json.loads(response.data)
        error_data = content.get('collection').get("error")
        logger.error("%s ==data==> %s" % (url, error_data))
        raise TermEvalNotCreated(url,
                                 error_data.get("code"),
                                 error_data.get("message"))

    return json.loads(response.data)
