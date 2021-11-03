import pytest

from src.calc.mortgage_calculator import MortgageCalculator, MortgageHelpToBuyCalculator


@pytest.fixture()
def fixture_mortgage_calculator():
    return MortgageCalculator(
        property_price=500000,
        deposit=0.10,
        interest=0.008,
        mortgage_duration=25,
        cpi=0.03,
    )


def test_monthly_mortgage_duration(fixture_mortgage_calculator):
    # When
    expected = 300

    # Then
    actual = fixture_mortgage_calculator.mortgage_duration_months

    actual == expected


def test_mortgage_amount(fixture_mortgage_calculator):
    # When
    expected = 450000

    # Then
    actual = fixture_mortgage_calculator.mortgage_amount

    actual == expected


def test_monthly_interest(fixture_mortgage_calculator):
    # When
    expected = 0.00067

    # Then
    actual = fixture_mortgage_calculator.monthly_interest

    actual == expected


def test_calculate_monthly_mortgage(fixture_mortgage_calculator):
    # When
    expected = 1655.49

    # Then
    actual = fixture_mortgage_calculator.calculate_monthly_mortgage()

    assert pytest.approx(actual, 0.01) == expected


def test_sdlt(fixture_mortgage_calculator):
    # When
    expected = 10000

    # Then
    actual = fixture_mortgage_calculator.sdlt

    assert actual == expected


def test_sdlt_upper():
    # When
    expected = 20000

    # then
    actual = MortgageCalculator(600000).sdlt

    assert actual == expected


def test_pass_in_non_float():
    with pytest.raises(ValueError):
        MortgageCalculator(deposit=2)


def test_pass_in_non_percentage():
    with pytest.raises(ValueError):
        MortgageCalculator(deposit=10)


def test_mortgage_help_to_buy_equity_amount():
    # When
    expected = 120000

    # Then
    actual = MortgageHelpToBuyCalculator(
        property_price=600000, help_to_buy_equity=0.2
    ).help_to_buy_equity_amount

    assert actual == expected


def test_mortgage_help_to_buy_calculator():
    # When
    expected = 330000

    # Then
    actual = MortgageHelpToBuyCalculator(
        property_price=600000, deposit=0.05, help_to_buy_equity=0.4
    ).mortgage_amount

    assert actual == expected


def test_pass_in_non_percentage_to_help_to_buy_equity():
    with pytest.raises(ValueError):
        MortgageHelpToBuyCalculator(help_to_buy_equity=10)
