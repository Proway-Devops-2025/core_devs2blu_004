# dummy_service_mock.py
from typing import Any, Dict, Optional
import time

class DummyServiceError(Exception):
    pass

class DummyAPIClient:
    """
    Mock de cliente API com comportamento configurável.
    Util: injetar em testes que esperam chamadas HTTP/serviço.
    """

    def __init__(self, fail_next: bool = False, latency: float = 0.0):
        # fail_next: se True, próxima chamada lançará erro
        # latency: segundos artificiais de atraso (simulação)
        self.fail_next = fail_next
        self.latency = latency
        self.calls = []  # registra chamadas para asserções nos testes

    def _maybe_sleep(self):
        if self.latency > 0:
            time.sleep(self.latency)

    def get_user(self, user_id: str) -> Dict[str, Any]:
        self.calls.append(("get_user", user_id))
        self._maybe_sleep()
        if self.fail_next:
            self.fail_next = False
            raise DummyServiceError("erro simulado: get_user")
        # resposta fake
        return {"id": user_id, "name": "Usuário Mock", "active": True}

    def create_order(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        self.calls.append(("create_order", payload))
        self._maybe_sleep()
        if self.fail_next:
            self.fail_next = False
            raise DummyServiceError("erro simulado: create_order")
        return {"order_id": "mock-" + payload.get("item", "x"), "status": "created", **payload}

    def set_fail_next(self, to: bool = True):
        self.fail_next = to

    def reset_calls(self):
        self.calls.clear()


# Exemplo de uso em teste (não requer requests)
if __name__ == "__main__":
    c = DummyAPIClient(latency=0.0)
    print(c.get_user("u-123"))
    print(c.create_order({"item":"camiseta","qty":2}))
    c.set_fail_next(True)
    try:
        c.get_user("u-124")
    except DummyServiceError as e:
        print("Erro capturado (esperado):", e)
    print("Chamadas registradas:", c.calls)
