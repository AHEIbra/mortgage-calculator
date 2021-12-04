from loguru import logger


class MortgageCalculator:
    def __init__(
        self,
        property_price: int = 50000,
        deposit: float = 0.10,
        interest: int = 0.008,
        mortgage_duration: int = 25,
        cpi: float = 0.03,
        mortgage_fees: float = 2500,
        available_cash: float = None,
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
        self.mortgage_fees = mortgage_fees

        if not available_cash:
            logger.warning(
                "Available cash is not set, setting to deposit amount for now"
            )

        self.available_money = available_cash

    @property
    def deposit_amount(self) -> float:
        return self.deposit * self.property_price

    @property
    def available_cash(self) -> float:
        return self.available_money if self.available_money else self.deposit_amount

    @property
    def mortgage_amount(self) -> float:
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

    @property
    def final_cash_available(self) -> float:
        final_cash_available = (
            self.available_cash - self.sdlt - self.deposit_amount - self.mortgage_fees
        )

        if final_cash_available < 0:
            logger.warning("Warning final available cash amount is negative")

        return final_cash_available

    @property
    def total_mortgage_cost(self) -> float:
        return self.calculate_monthly_mortgage() * self.mortgage_duration_months

    @property
    def minimum_salary(self) -> float:
        return self.mortgage_amount / 4.5

    def calculate_monthly_mortgage(self) -> float:
        # Monthly payment = P[i(1+i)^n)]/[(q+i)^n - 1)
        return self.mortgage_amount * (
            (
                self.monthly_interest
                * (1 + self.monthly_interest) ** self.mortgage_duration_months
            )
            / (((1 + self.monthly_interest) ** self.mortgage_duration_months) - 1)
        )

    def summarise(self) -> str:
        house_price = self.property_price
        mortgage_amount = self.mortgage_amount
        deposit = self.deposit * 100
        deposit_amount = self.deposit_amount
        interest = self.interest * 100
        stamp_duty = self.sdlt
        cash_available = self.available_cash
        mortgage_fess = self.mortgage_fees
        monhtly_mortgage = self.calculate_monthly_mortgage()
        total_mortgage_cost = self.total_mortgage_cost
        cash_left_over = self.final_cash_available
        minimum_salary_mount = self.minimum_salary

        summarised_mortgage = f"""
        HOUSE PRICE: {house_price}
        DEPOSIT: {deposit}%
        DEPOSIT AMOUNT: {deposit_amount}
        MORTGAGE AMOUNT: {mortgage_amount}
        INTEREST: {interest}%
        ---------------------------------
        MONTHLY MORTGAGE PAYMENTS: {monhtly_mortgage}
        TOTAL MORTGAGE COST: {total_mortgage_cost}
        ---------------------------------
        CASH AVAILABLE FOR MORTGAGE: {cash_available}
        STAMP DUTY LAND TAX: {stamp_duty}
        MORTGAGE FEES: {mortgage_fess}
        CASH LEFT OVER: {cash_left_over}
        MINIMUM SALARY REQUIRED: {minimum_salary_mount}

        """

        return summarised_mortgage


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

    def summarise(self) -> str:
        house_price = self.property_price
        help_to_buy_equity = self.help_to_buy_equity * 100
        help_to_buy_amount = self.help_to_buy_equity_amount
        deposit = self.deposit * 100
        deposit_amount = self.deposit_amount
        mortgage_amount = self.mortgage_amount
        interest = self.interest * 100
        stamp_duty = self.sdlt
        cash_available = self.available_cash
        mortgage_fess = self.mortgage_fees
        monhtly_mortgage = self.calculate_monthly_mortgage()
        total_mortgage_cost = self.total_mortgage_cost
        cash_left_over = self.final_cash_available
        minimum_salary_amount = self.minimum_salary

        summarised_mortgage = f"""
        HOUSE PRICE: {house_price}
        DEPOSIT: {deposit}%
        DEPOSIT AMOUNT: {deposit_amount}
        HELP TO BUY EQUITY: {help_to_buy_equity}%
        HELP TO BUY EQUITY AMOUNT: {help_to_buy_amount}
        MORTGAGE AMOUNT: {mortgage_amount}
        INTEREST: {interest}%
        ---------------------------------
        MONTHLY MORTGAGE PAYMENTS: {monhtly_mortgage}
        TOTAL MORTGAGE COST: {total_mortgage_cost}
        ---------------------------------
        CASH AVAILABLE FOR MORTGAGE: {cash_available}
        STAMP DUTY LAND TAX: {stamp_duty}
        MORTGAGE FEES: {mortgage_fess}
        CASH LEFT OVER: {cash_left_over}
        MINIMUM SALARY REQUIRED: {minimum_salary_amount}

        """

        return summarised_mortgage


class OptimalMortgageCalculator:
    def __init__(
        self,
        total_annual_salary: float = 100000,
        savings: float = 50000,
        mortgage_fees: float = 2500,
    ) -> None:
        self.total_annual_salary = total_annual_salary
        self.savings = savings
        self.mortgage_fees = mortgage_fees

    @property
    def maximum_mortgage(self):
        return self.total_annual_salary * 4.5
