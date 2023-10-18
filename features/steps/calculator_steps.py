from behave import *
from src.Calculator import Calculator


@given('a calculator')
def step_impl(context):
    context.calculator = Calculator()


@when('I add {num1:d} and {num2:d}')
def step_impl(context, num1, num2):
    context.result = context.calculator.add(num1, num2)


@then('the result should be {expected:d}')
def step_impl(context, expected):
    assert context.result == expected



