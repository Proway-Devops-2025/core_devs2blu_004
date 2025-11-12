# dummy_service_mock.py
from typing import Any, Dict
import time


class DummyServiceError(Exception):
    """Erro simulado para o mock de serviço."""
    pass


class DummyAPIClient:
    """
    Mock de cliente de API com comportamento configurável.
    Pode simular falhas, atrasos e registrar chamadas.
    """

    def __init__(self, should_fail_next: bool = False, artificial_delay: float = 0.0):
        """
        :param should_fail_next: se True, a próxima chamada gerará erro
        :param artificial_delay: tempo de espera (em segundos) para simular latência
        """
        self.should_fail_next = should_fail_next
        self.artificial_delay = artificial_delay
        self.call_log = []  # lista de chamadas feitas (para asserções em testes)

    def _simulate_delay(self):
        """Simula atraso artificial."""
        if self.artificial_delay > 0:
            time.sleep(self.artificial_delay)

    def get_user(self, user_id: str) -> Dict[str, Any]:
        """
        Simula a busca de um usuário por ID.
        Pode falhar se should_fail_next=True.
        """
        self.call_log.append(("get_user", user_id))
        self._simulate_delay()

        if self.should_fail_next:
            self.should_fail_next = False
            raise DummyServiceError("Falha simulada em get_user")

        return {"id": user_id, "name": "Usuário Fictício", "active": True}

    def create_order(self, order_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simula a criação de um pedido.
        Pode falhar se should_fail_next=True.
        """
        self.call_log.append(("create_order", order_data))
        self._simulate_delay()

        if self.should_fail_next:
            self.should_fail_next = False
            raise DummyServiceError("Falha simulada em create_order")

        order_id = "mock-" + order_data.get("item", "sem-item")
        return {"order_id": order_id, "status": "created", **order_data}

    def enable_next_failure(self):
        """Configura para que a próxima chamada lance DummyServiceError."""
        self.should_fail_next = True

    def clear_log(self):
        """Limpa o registro de chamadas."""
        self.call_log.clear()


# Exemplo de uso em teste manual
if __name__ == "__main__":
    client = DummyAPIClient(artificial_delay=0.0)

    print(client.get_user("user-123"))
    print(client.create_order({"item": "caneca", "quantity": 2}))

    client.enable_next_failure()
    try:
        client.get_user("user-456")
    except DummyServiceError as error:
        print("Erro capturado (esperado):", error)

    print("Chamadas registradas:", client.call_log)
