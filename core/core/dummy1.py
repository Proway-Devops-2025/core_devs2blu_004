# dummy_data.py
from typing import Dict, Iterator, List
import random
import uuid
import datetime

class DummyDataGenerator:
    """
    Gera registros sintéticos tipo usuário/ordem para testes.
    Uso: gen = DummyDataGenerator(); next(gen.users(5))
    """
    FIRST_NAMES = ["Ana", "Bruno", "Carlos", "Beatriz", "Diego"]
    LAST_NAMES = ["Silva", "Pereira", "Oliveira", "Souza", "Alves"]
    PRODUCTS = ["camiseta", "caneca", "livro", "fone", "mochila"]

    def random_user(self) -> Dict:
        uid = str(uuid.uuid4())
        name = f"{random.choice(self.FIRST_NAMES)} {random.choice(self.LAST_NAMES)}"
        age = random.randint(15, 60)
        return {
            "id": uid,
            "name": name,
            "age": age,
            "email": f"{name.lower().replace(' ','.')}@exemplo.com"
        }

    def random_order(self, user_id: str = None) -> Dict:
        order_id = str(uuid.uuid4())
        user = user_id or str(uuid.uuid4())
        quantity = random.randint(1, 5)
        product = random.choice(self.PRODUCTS)
        price = round(random.uniform(10.0, 200.0), 2)
        created = datetime.datetime.utcnow().isoformat() + "Z"
        return {
            "order_id": order_id,
            "user_id": user,
            "product": product,
            "quantity": quantity,
            "total": round(price * quantity, 2),
            "created_at": created
        }

    def users(self, n: int) -> List[Dict]:
        return [self.random_user() for _ in range(n)]

    def orders(self, n: int, user_pool: List[Dict] = None) -> List[Dict]:
        user_ids = [u["id"] for u in (user_pool or self.users(max(1, n//2)))]
        return [self.random_order(user_id=random.choice(user_ids)) for _ in range(n)]


# Exemplo de uso rápido
if __name__ == "__main__":
    g = DummyDataGenerator()
    print("3 usuários:", g.users(3))
    print("5 pedidos:", g.orders(5))
