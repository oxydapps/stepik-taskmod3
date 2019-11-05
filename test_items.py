link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_is_available(browser):
    browser.get(link)
    button = len(browser.find_elements_by_class_name("btn-add-to-basket"))
    assert button > 0, "button 'Add to basket' not found"
