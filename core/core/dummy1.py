# dummy_data.py
from typing import Dict, List
import random
import uuid
import datetime


class DummyDataGenerator:
    """
    Gera registros sintéticos tipo usuário e pedido para testes.
    Uso:
        gen = DummyDataGenerator()
        gen.users(5)
        gen.orders(10)
    """

    FIRST_NAMES = ["Ana", "Bruno", "Carlos", "Beatriz", "Diego"]
    LAST_NAMES = ["Silva", "Pereira", "Oliveira", "Souza", "Alves"]
    PRODUCTS = ["camiseta", "caneca", "livro", "fone", "mochila"]

    def generate_user(self) -> Dict:
        user_id = str(uuid.uuid4())
        name = f"{random.choice(self.FIRST_NAMES)} {random.choice(self.LAST_NAMES)}"
        age = random.randint(15, 60)
        return {
            "id": user_id,
            "name": name,
            "age": age,
            "email": f"{name.lower().replace(' ','.')}@exemplo.com"
        }

    def generate_order(self, user_id: str) -> Dict:
        order_id = str(uuid.uuid4())
        product_name = random.choice(self.PRODUCTS)
        quantity = random.randint(1, 5)
        unit_price = round(random.uniform(10.0, 200.0), 2)
        total_price = round(unit_price * quantity, 2)
        created_at = datetime.datetime.utcnow().isoformat() + "Z"

        return {
            "order_id": order_id,
            "user_id": user_id,
            "product": product_name,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_price": total_price,
            "created_at": created_at
        }

    def users(self, amount: int) -> List[Dict]:
        return [self.generate_user() for _ in range(amount)]

    def orders(self, amount: int, users_list: List[Dict] = None) -> List[Dict]:
        """
        Gera uma lista de pedidos sintéticos.
        - amount: número de pedidos
        - users_list: lista de usuários existentes (opcional)
        """
        if not users_list:
            users_list = self.users(max(1, amount // 2))

        user_ids = [user["id"] for user in users_list]
        return [self.generate_order(user_id=random.choice(user_ids)) for _ in range(amount)]


# Exemplo de uso rápido
if __name__ == "__main__":
    generator = DummyDataGenerator()
    print("Usuários (3):", generator.users(3))
    print("Pedidos (5):", generator.orders(5))
