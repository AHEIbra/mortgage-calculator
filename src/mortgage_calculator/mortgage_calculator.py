class MortgageCalculator:
    def __init__(
        self,
        property_price: int = 50000,
        deposit: float = 0.10,
        interest: int = 0.008,
        mortgage_duration: int = 25,
        cpi: float = 0.03,
    ) -> None:
        if (not all(isinstance(var, float) for var in [deposit, interest, cpi])) or (
            all(var > 1 for var in [deposit, interest, cpi])
        ):
            raise ValueError('Value must be a percentage!')

        self.property_price = property_price
        self.deposit = deposit
        self.interest = interest
        self.mortgage_duration = mortgage_duration
        self.cpi = cpi

    @property
    def deposit_amount(self) -> float:
        return self.deposit * self.property_price

    @property
    def mortgage_amount(self) -> int:
        return self.property_price - self.deposit_amount

    @property
    def mortgage_duration_months(self) -> int:
        return self.mortgage_duration * 12

    @property
    def monthly_interest(self) -> float:
        return self.interest / 12

    @property
    def sdlt(self) -> float:
        if self.property_price < 300000:
            return 0

        if (self.property_price <= 500000) & (self.property_price > 300000):
            return (self.property_price - 300000) * 0.05

        else:
            return (self.property_price - 250000) * 0.05 + 2500

    def calculate_monthly_mortgage(self) -> float:
        # Monthly payment = P[i(1+i)^n)]/[(q+i)^n - 1)

        return self.mortgage_amount * (
            (
                self.monthly_interest
                * (1 + self.monthly_interest) ** self.mortgage_duration_months
            )
            / (((1 + self.monthly_interest) ** self.mortgage_duration_months) - 1)
        )


class MortgageHelpToBuyCalculator(MortgageCalculator):
    def __init__(self, help_to_buy_equity: float = 0.4, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if (not isinstance(help_to_buy_equity, float)) and (help_to_buy_equity > 1):
            raise ValueError('help_to_buy_equity must be a float less than 1')

        self.help_to_buy_equity = help_to_buy_equity

    @property
    def help_to_buy_equity_amount(self) -> float:
        return self.property_price * self.help_to_buy_equity

    @property
    def mortgage_amount(self) -> float:
        return (
            self.property_price - self.deposit_amount - self.help_to_buy_equity_amount
        )
