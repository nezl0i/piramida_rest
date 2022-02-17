import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()


class RESTAPI:
    def __init__(self, url, method='GET'):

        self.REST_API = None
        self.url = url
        self._method = method

        self._objectGuid: str = ''  # guid объекта
        self._classGuid: str = ''   # guid класса
        self._meterGuid: str = ''   # guid прибора учета
        self._pointGuid: str = ''   # guid точки учета
        self._eventGuid: str = ''   # guid события
        self._meterpointGuid: str = ''  # guid точки учета
        self._parameterGuid: str = ''   # guid параметра
        self._attributeName: str = ''   # guid аттрибута
        self._serialNumber: str = ''    # серийный номер прибора учета
        self._value: str = ''   # значение
        self._dt: str = ''  # время установки
        self._dtfrom: str = ''  # период, дни с
        self._dtto: str = ''  # период, дни по

    @property
    def objectGuid(self):
        return self._objectGuid

    @objectGuid.setter
    def objectGuid(self, v):
        self._objectGuid = v

    @property
    def classGuid(self):
        return self._classGuid

    @classGuid.setter
    def classGuid(self, v):
        self._classGuid = v

    @property
    def meterGuid(self):
        return self._meterGuid

    @meterGuid.setter
    def meterGuid(self, v):
        self._meterGuid = v

    @property
    def pointGuid(self):
        return self._pointGuid

    @pointGuid.setter
    def pointGuid(self, v):
        self._pointGuid = v

    @property
    def eventGuid(self):
        return self._eventGuid

    @eventGuid.setter
    def eventGuid(self, v):
        self._eventGuid = v

    @property
    def meterpointGuid(self):
        return self._meterpointGuid

    @meterpointGuid.setter
    def meterpointGuid(self, v):
        self._meterpointGuid = v

    @property
    def parameterGuid(self):
        return self._parameterGuid

    @parameterGuid.setter
    def parameterGuid(self, v):
        self._parameterGuid = v

    @property
    def attributeName(self):
        return self._attributeName

    @attributeName.setter
    def attributeName(self, v):
        self._attributeName = v

    @property
    def serialNumber(self):
        return self._serialNumber

    @serialNumber.setter
    def serialNumber(self, v):
        self._serialNumber = v

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v

    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, v):
        self._dt = v

    @property
    def dtfrom(self):
        return self._dtfrom

    @dtfrom.setter
    def dtfrom(self, v):
        self._dtfrom = v

    @property
    def dtto(self):
        return self._dtto

    @dtto.setter
    def dtto(self, v):
        self._dtto = v

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, v):
        self._method = v

    def __str__(self):
        return self.method

    def check_param(self, param):

        self.REST_API = {

            # GET
            # "summary": "Проверка соединения",
            # "description": "Проверка соединения возвращает pong если есть соединение с сервером"
            'PING': ['ping'],

            # GET
            # "summary": "Обновить кеш объектов",
            # "description": "Обновить кеш объектов - использовать если пирамида
            # не возвращает корректно обновленные атрибуты"
            'REFRESH': ['refresh'],

            # GET
            # "summary": "Получить перечень классов используемых Пирамида",
            # "description": "Возвращает перечень **всех** классов используемых в пирамиде,
            # вместе с атрибутами и их типами, операция ресурсоемкая"
            'CLASSES': ['classes'],

            # GET
            # "summary": "Получить информацию об объекте",
            # "description": "Возвращает информацию об объекте со всеми атрибутами"
            # PUT
            # "summary": "Обновление атрибутов объекта",
            # "description": "Обновление атрибутов объекта"
            # POST
            # "summary": "Добавление объекта",
            # "description": "Добавление объекта с названием в определенный класс"
            # DELETE
            # "summary": "Удалить объект",
            # "description": "Удалить объект по заданному guid"
            'OBJECT_GUID': ['object', self.objectGuid],

            # GET
            # "summary": "Получить информацию о классе (перечень атрибутов)",
            # "description": "Возвращает полную информацию о классе по его guid"
            'CLASS_GUID': ['class', self.classGuid],

            # GET
            # "summary": "Получить перечень объектов по заданному классу",
            # "description": "Возвращает перечень объектов по классу с заданным guid"
            'OBJECT_BY_CLASS': ['objectsbyclass', self.classGuid],

            # GET
            # "summary": "найти объект по значению атрибута",
            # "description": "находит объект по значению атрибута"
            'OBJECT_BY_ATTRIBUTE': ['objectbyattribute', self.classGuid, self.attributeName, self.value],

            # GET
            # "summary": "Получить перечень приборов учета",
            # "description": "Возвращает перечень **всех** приборов учета,
            # которые необходимо сохранять на клиенте, для дальнейшего использования, операция ресурсоемкая"
            'METERS': ['meters'],

            # GET
            # "summary": "Получить перечень точек учета",
            # "description": "Возвращает перечень **всех** точек учета, которые необходимо сохранять на клиенте,
            # для дальнейшего использования, операция ресурсоемкая"
            'METERPOINTS': ['meterpoints'],

            # GET
            # "summary": "Получить перечень типов оборудования",
            # "description": "Возвращает перечень **всех** типов оборудования"
            'EQUIPMENTTYPES': ['equipmenttypes'],

            # GET
            # "summary": "Получить перечень типов параметров для передачи данных с приборов/точек учета",
            # "description": "Возвращает перечень **всех** типов параметров для передачи данных с приборов/точек учета"
            'PARAMETERS': ['parameters'],

            # GET
            # "summary": "Получить перечень типов событий для передачи данных с приборов/точек учета",
            # "description": "Возвращает перечень **всех** типов событий для передачи данных с приборов/точек учета"
            'EVENTS': ['events'],

            # DELETE
            # "summary": "Удалить прибор учета",
            # "description": "Удалить прибору учета по-заданному guid"
            # GET
            # "summary": "Объект прибор учета",
            # "description": "Возвращает объект прибор учета со всеми атрибутами объекта и дополнительными свойствами"
            'METER_GUID': ['meter', self.meterGuid],

            # POST
            # "summary": "Добавление прибора учета",
            # "description": "Добавление прибора учета с названием в определенный класс"
            'METER': ['meter'],

            # GET
            # "summary": "Привязывает заданный прибор учета к точке учета с указанной даты",
            # "description": "Выполняет операцию аналогичную установке прибора учета через
            # пользовательский интерфейс с созданием вспомогательных объектов"
            'METER_TO_POINT': ['meter2point', self.meterGuid, self.pointGuid, self.dt],

            # DELETE
            # "summary": "Удалить данные по определенному параметру на заданной точке за указанный период",
            # "description": "удаление данных"
            # GET
            # "summary": "Получить данные по определенному параметру на заданной точки учета за указанный период",
            # "description": "получение данных"
            'METERPOINT_PARAMETERS': ['meterpointparameters', self.meterpointGuid, self.parameterGuid, self.dtfrom, self.dtto],

            # PUT
            # "summary": "Запись данных в точку учета",
            # "description": "записывает данные по заданному параметру в точку учета"
            'METERPOINT_PARAMETER': ['meterpointparameters', self.meterpointGuid, self.parameterGuid],

            # DELETE
            # "summary": "Удалить данные по определенному параметру на заданном приборе учета за указанный период",
            # "description": "удаление данных"
            # GET
            # "summary": "Получить данные по определенному параметру на заданном приборе учета за указанный период",
            # "description": "получение данных"
            'METER_PARAMETERS': ['meterparameters', self.meterGuid, self.parameterGuid, self.dtfrom, self.dtto],

            # PUT
            # "summary": "Запись данных в прибор учета",
            # "description": "записывает данные по заданному параметру в прибор учета"
            'METER_PARAMETER': ['meterparameters', self.meterGuid, self.parameterGuid],

            # GET
            # "summary": "найти прибор учета по серийному номеру",
            # "description": "находит прибор учета"
            'METER_BY_SERIAL': ['meterbyserial', self.serialNumber],

            # GET
            # "summary": "Получить данные по определенному параметру по заданному списку приборов учета
            # (передается в payload guid через запятую) за указанный период",
            # "description": "получение данных"
            'METERPOINT_BACH_PARAMETER': ['meterpointbymeterparametersbatch', self.parameterGuid, self.dtfrom, self.dtto],

            # GET
            # "summary": "Получить события по заданному прибору учета за указанный период",
            # "description": "получение событий"
            'METEREVENTS': ['meterevents', self.meterGuid, self.dtfrom, self.dtto],

            # GET
            # "summary": "Получить события по заданной точки учета за указанный период",
            # "description": "получение событий"
            'METERPOINTEVENTS': ['meterpointevents', self.meterpointGuid, self.dtfrom, self.dtto],

            # PUT
            # "summary": "Запись данных в прибор учета",
            # "description": "записывает события по заданному прибору учета"
            'METEREVENT': ['meterevents', self.meterGuid, self.eventGuid]
        }
        return self.REST_API.get(param)

    @staticmethod
    def check_response(request):

        print(f'Response - {request.status_code}')
        if request.status_code == 200:
            print(f'{request.json()}')
        else:
            print("Запрос не отработан. Проверьте параметры")

        return request.json()

    def get_value(self, payloads=None, param=None):

        request: any = None
        tmp = self.check_param(param)

        filename = '_'.join(tmp)
        path = os.path.join("log", f'{filename}.json')

        tmp.insert(0, self.url)
        data = '/'.join(tmp)
        print(data)

        if self.method == 'GET':
            request = requests.get(data)

        if self.method == 'POST':
            request = requests.post(data, json=payloads)

        if self.method == 'PUT':
            request = requests.put(data, json=payloads)

        if self.method == 'DELETE':
            request = requests.delete(data, json=payloads)

        response = self.check_response(request)
        with open(path, 'w', encoding="utf-8") as f:
            data = json.dumps(response, ensure_ascii=False)
            f.write(data)


if __name__ == '__main__':

    url = os.getenv('url')
    method = 'GET'

    rest = RESTAPI(url, method=method)

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

    payload = {'12.12.2019': '99999999'}

    rest.get_value(param='OBJECT_GUID', payloads=payload)
