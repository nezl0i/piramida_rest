from restapi_class import RESTAPI
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv('url')
method = 'GET'

rest = RESTAPI(url, method=method)

if __name__ == '__main__':

    rest.meterGuid = '05dec902-9b7e-4d31-a3f1-9e11d8fd53e2'
    rest.parameterGuid = 'd2c9783f-611c-47c7-83af-ce65c8da48fd'
    rest.objectGuid = '92f2a50f-e85b-4e18-b84b-6b27ad5bdccd'    # guid точки учета, параметра, прибора учета, события
    rest.classGuid = ''
    rest.pointGuid = ''
    rest.eventGuid = ''
    rest.meterpointGuid = ''
    rest.attributeName = ''
    rest.serialNumber = ''
    rest.value = ''
    rest.dt = ''
    rest.dtfrom = ''
    rest.dtto = ''

    # ONLY from method POST and PUT !
    payload = {'12.12.2019': '99999999'}

    rest.get_value(param='OBJECT_GUID', payloads=payload)
