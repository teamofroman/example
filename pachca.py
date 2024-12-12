import schemas
from exceptions import PachcaAPIException

BASE_API_SERVER = "https://api.pachca.com/api/shared/v1"


class Pachca:
    def __init__(self, auth_token: str):
        """Инициализирует объект"""
        self.client = ...

    async def getStatus(self) -> schemas.StatusResponce:
        """Получение текущего статуса.

        Метод для получения информации о своем статусе.
        """
        try:
            response_json = self.client(method="get")
        except PachcaAPIException as e:
            raise Exception(e)

        return schemas.StatusResponce.from_json(response_json)

    async def putStatus(self, data: schemas.StatusRequest) -> schemas.StatusResponce:
        """Установка нового статуса.

        Метод для установки себе нового статуса.

        data - Параметры нового статуса
        """
        try:
            response_json = self.client(method="put", data=data.to_json())
        except PachcaAPIException as e:
            raise Exception(e)

        return schemas.StatusResponce.from_json(response_json)
