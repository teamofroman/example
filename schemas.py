class Status:
    """Статус пользователя.

    emoji - Emoji символ статуса
    title - Текст статуса
    expires_at - Срок жизни статуса (ISO-8601, UTC+0) в формате YYYY-MM-DDThh:mm:ss.sssZ
    """

    emoji: str
    title: str
    expires_at: str

    @classmethod
    def from_json(cls, json: str):
        """Создает объект на основе json."""
        new_obj = cls(...)
        return new_obj

    def to_json(self) -> str:
        """Преобразует объект в json."""
        new_json_str = ...
        return new_json_str


class StatusRequest:
    """Данные для установки статуса.

    status - Данные нового статуса
    """

    status: Status

    @classmethod
    def from_json(cls, json: str):
        """Создает объект на основе json."""
        new_obj = cls(...)
        return new_obj

    def to_json(self) -> str:
        """Преобразует объект в json."""
        new_json_str = ...
        return new_json_str


class StatusResponce:
    """Информация о текущем статусе.

    data - Данные статуса
    """

    data: Status

    @classmethod
    def from_json(cls, json: str):
        """Создает объект на основе json."""
        new_obj = cls(...)
        return new_obj

    def to_json(self) -> str:
        """Преобразует объект в json."""
        new_json_str = ...
        return new_json_str


class Error:
    """Представляет ошибку обработки запроса.

    key - Ключ параметра, в котором произошла ошибка
    value - Значение ключа, которое вызвало ошибку
    message - Ошибка текстом, который вы можете вывести пользователю
    code - Внутренний код ошибки (коды ошибок представлены в описании каждого метода)
    payload - Объект, который предоставляет любую дополнительную информацию (возможные дополнения представлены в описании каждого метода)
    """

    key: str
    value: str
    message: str
    code: str
    payload: object

    @classmethod
    def from_json(cls, json: str):
        """Создает объект на основе json."""
        new_obj = cls(...)
        return new_obj

    def to_json(self) -> str:
        """Преобразует объект в json."""
        new_json_str = ...
        return new_json_str


class ErrorResponce:
    """Ошибки, выявленные при обработке запроса.

    items - Массив ошибок
    """

    items: list[Error]

    @classmethod
    def from_json(cls, json: str):
        """Создает объект на основе json."""
        new_obj = cls(...)
        return new_obj

    def to_json(self) -> str:
        """Преобразует объект в json."""
        new_json_str = ...
        return new_json_str
