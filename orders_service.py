from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable


@dataclass(frozen=True)
class Order:
    order_id: str
    amount: Decimal


class OrdersJob:
    """Process order records using ordinary Python methods."""

    def extract_orders(self, records: Iterable[Order]) -> list[Order]:
        return list(records)

    def transform_orders(self, orders: Iterable[Order]) -> list[Order]:
        return [
            Order(order_id=order.order_id.strip(), amount=order.amount)
            for order in orders
        ]

    def load_orders(self, orders: Iterable[Order]) -> dict[str, Decimal]:
        return {order.order_id: order.amount for order in orders}

    def run_pipeline(self, records: Iterable[Order]) -> dict[str, Decimal]:
        extracted = self.extract_orders(records)
        transformed = self.transform_orders(extracted)
        return self.load_orders(transformed)
