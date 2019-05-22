# -*- coding: utf8 -*-
# we should add test cases here because we can miss some cases while writing automation code or
# We can also record the result of test cases to test management tool

def test_cases(number):
    return testCases[number]

testCases = [
    #[severity, description]
    ['Regression', 'when user enter url, page should be loaded'],
    ['Regression', 'In Login page, When enter valid username/password user is able to login'],
    ['Regression', 'After login, user is able to create new Note. New Note should display in the Main page'],
]