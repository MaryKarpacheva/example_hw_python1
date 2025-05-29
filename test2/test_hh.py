import pytest
from selene import browser, have, by



def test_2():
    browser.open('https://school.qa.guru')
    browser.element('[name="email"]').type('qagurubot@gmail.com')
    browser.element('[name="password"]').type('somepasshere').press_enter()
    browser.element('[class="page-header"]').should(have.text('Список тренингов'))
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('.logined-form').should(have.text('QA_GURU_BOT'))
    browser.close()

def test_2_wrong_login_password():
    browser.open('https://school.qa.guru')
    browser.element('[name="email"]').type('qagurubot@gmail.com')
    browser.element('[name="password"]').type('12345678').press_enter()
    browser.element('.btn-error').should(have.text('Неверный пароль'))
    browser.close()

def test_2_empty_password():
    browser.open('https://school.qa.guru')
    browser.element('[name="email"]').type('qagurubot@gmail.com')
    browser.element('[name="password"]').type('').press_enter()
    browser.element('.btn-error').should(have.text('Не заполнено поле Пароль'))
    browser.close()

def test_2_empty_login():
    browser.open('https://school.qa.guru')
    browser.element('[name="password"]').type('').press_enter()
    browser.element('.btn-error').should(have.text('Не заполнено поле E-Mail'))
    browser.close()