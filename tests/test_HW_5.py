import os

from selene import browser
from selene.support.conditions import be, have

def test_registration_form(setup_browser):
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Olga')
    browser.element('#lastName').type('Turanskaya')
    browser.element('#userEmail').type('tur@mail.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('7123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select>option[value="1"]').click()
    browser.element('.react-datepicker__year-select>option[value="1999"]').click()
    browser.element('.react-datepicker__day--014').click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/fem_red.png'))
    browser.element('#currentAddress').type('Moscow, Red Square, 1')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').click()

    browser.element('.table-responsive').should(have.text('Olga' and 'Turanskaya' and 'tur@mail.ru' and '+7123456789'
                                                          and '14 January,1999' and 'English' and 'Sports' and 'Moscow, Red Square, 1'
                                                          and 'NCR Delhi'))

    browser.element('#closeLargeModal').click()







