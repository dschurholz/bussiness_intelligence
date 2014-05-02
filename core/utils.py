from django.conf import settings
import MySQLdb


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
