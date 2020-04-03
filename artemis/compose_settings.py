# encoding: utf-8
# When using ArtemisNG with docker-compose, these parameters will always be the same

USE_ARTEMIS_NG = True

CITIES_DB = "dbname=cities user=navitia host=localhost password=password"

URL_JORMUN = "http://localhost:9191"

JORMUNGANDR_DB = (
    "dbname=jormungandr user=jormungandr host=localhost password=jormungandr"
)

URL_TYR = "http://localhost:9898"

KIRIN_API = "http://localhost:9292"

KIRIN_DB = "dbname=kirin user=navitia host=localhost password=navitia port=9494"

KIRIN_API = "http://localhost:9292"
