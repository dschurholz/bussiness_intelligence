from django.conf import settings
import MySQLdb

from api import constants

def get_db_connection(autocommit=False):
    """
    Creates a MySQLdb connection inside the provided project database,
    with permissions only for that specific database.
    """

    db = settings.DATABASES['default']

    connection = MySQLdb.connect(host=db.get('HOST'), port=int(db.get('PORT')),
                                 user=db.get('USER'), passwd=db.get('PASSWORD'),
                                 db=db.get('NAME'))
    if autocommit:
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return connection


def replace_spaces(string):
    return "_".join(string.split(" "))


def replace_underscore(string):
    return " ".join(string.split("_"))

def get_hier_order(hierarchies):
    hs = []
    for h in constants.HIER_ORDER:
        if h in hierarchies:
            hs.append(h)
    return hs