import pytest

from src.calc.mortgage_calculator import MortgageCalculator


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