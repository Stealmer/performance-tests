from clients.http.client import HTTPClient
from httpx import Response, QueryParams
from typing import TypedDict


class GetOperationsDict(TypedDict):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    accountId: str


class GetOperationsSummaryDict(GetOperationsDict):
    """
    Структура данных для получения статистики по операциям для определенного счета..
    """


class MakeFeeOperationDict(TypedDict):
    """
    Структура данных для создания операции комиссии.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTopUpOperationDict(MakeFeeOperationDict):
    """
    Структура данных для создания операции пополнения.
    """


class MakeCashbackOperationDict(MakeFeeOperationDict):
    """
    Структура данных для создания операции кэшбека.
    """


class MakeTransferOperationDict(MakeFeeOperationDict):
    """
    Структура данных для создания операции перевода.
    """


class MakePurchaseOperationDict(MakeFeeOperationDict):
    """
    Структура данных для создания операции покупки.
    """
    categoryId: str


class MakeBillPaymentOperationDict(MakeFeeOperationDict):
    """
    Структура данных для создания операции оплаты по счету.
    """


class MakeCashWithdrawalOperationDict(MakeFeeOperationDict):
    """
    Структура данных для создания операции снятия наличных средств.
    """


class OperationsHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение информации об операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f'/api/v1/operations/{operation_id}')

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение чека по операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operations_api(self, query: GetOperationsDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определенного счета

        :param query: Словарь с параметрами запроса.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get('/api/v1/operations', params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryDict) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определенного счета.

        :param query: Словарь с параметрами запроса.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get('/api/v1/operations-summary', params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationDict) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post('/api/v1/operations/make-fee-operation', json = request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationDict) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post('/api/v1/operations/make-top-up-operation', json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationDict) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post('/api/v1/operations/make-cashback-operation', json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationDict) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post('/api/v1/operations/make-transfer-operation', json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationDict) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post('/api/v1/operations/make-purchase-operation', json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post('/api/v1/operations/make-bill-payment-operation', json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationDict) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных денег.

        :param request: Словарь с параметрами запроса.
        :return: Объект httpx.Response.
        """
        return self.post('/api/v1/operations/make-cashback-operation', json=request)