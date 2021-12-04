from typing import Callable, Tuple


class MortgageOptimiser:
    def __init__(self, deposit: float, mortgage: float, free_cash=float) -> None:
        self.mortgage = mortgage
        self.deposit = deposit
        self.free_cash = free_cash

    @staticmethod
    def tax(price) -> float:
        if price < 300000:
            return 0

        if (price <= 500000) & (price > 300000):
            return (price - 300000) * 0.05

        else:
            return (price - 250000) * 0.05 + 2500
