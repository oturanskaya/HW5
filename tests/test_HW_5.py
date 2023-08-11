import os

from selene import browser, command
from selene.support.conditions import be, have

def test_registration_form(setup_browser):
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')


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

    #browser.element('[#subjectsInput"]').perform(command.js.scroll_into_view)

    browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/fem_red.png'))
    browser.element('#currentAddress').type('Moscow, Red Square, 1')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').click()

    browser.element('.table').should(have.text('Olga Turanskaya'))
    browser.element('.table').should(have.text('tur@mail.ru'))
    browser.element('.table').should(have.text('14 February,1999'))
    browser.element('.table').should(have.text('Female'))
    browser.element('.table').should(have.text('7123456789'))
    browser.element('.table').should(have.text('English'))
    browser.element('.table').should(have.text('Sports'))
    browser.element('.table').should(have.text('Moscow, Red Square, 1'))
    browser.element('.table').should(have.text('NCR Delhi'))

    browser.element('#closeLargeModal').click()







