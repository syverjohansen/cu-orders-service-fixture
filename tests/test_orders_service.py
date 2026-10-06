import unittest
from decimal import Decimal

from orders_service import Order, OrdersJob


class OrdersJobTest(unittest.TestCase):
    def test_run_pipeline_normalizes_ids_and_preserves_amounts(self) -> None:
        records = [Order(order_id=" order-1 ", amount=Decimal("12.50"))]

        result = OrdersJob().run_pipeline(records)

        self.assertEqual(result, {"order-1": Decimal("12.50")})


if __name__ == "__main__":
    unittest.main()
