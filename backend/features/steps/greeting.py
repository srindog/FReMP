from behave import given, when, then
from app import greeting, mongo_greeting


@given('we arrive at the app')
def step_impl(context):
  pass

#greeting
@when('the default greeting is requested')
def step_impl(context):
  response = greeting()
  context.default_greeting = response['greeting']

@then('the default greeting says "{greeting}"')
def step_impl(context, greeting):
  assert context.greeting == greeting


#mongo greeting
@when('the mongo greeting is requested')
def step_impl(context):
  response = mongo_greeting()
  context.greeting = response['greeting']

@then('the mongo greeting says "{greeting}"')
def step_impl(context, greeting):
  assert context.greeting == greeting
