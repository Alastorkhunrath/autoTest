from pages.sbis_main_page import SbisMainPage
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_main_page import *
from pages.tensor_about_page import *

def test_tensor_people_block(browser):
    sbis = SbisMainPage(browser)
    sbis.open("https://sbis.ru/")
    sbis.go_to_contacts()

    contacts = SbisContactsPage(browser)
    contacts.click_tensor_banner()

    # Переход на новую вкладку
    browser.switch_to.window(browser.window_handles[1])
    tensor = TensorMainPage(browser)
    assert tensor.is_block_present()

    tensor.click_more()
    assert "https://tensor.ru/about" in browser.current_url

    about = TensorAboutPage(browser)
    sizes = about.get_images_size()
    assert all(size == sizes[0] for size in sizes), "Не все картинки одинакового размера"


def test_region_change(browser):
    sbis = SbisMainPage(browser)
    sbis.open("https://sbis.ru/")
    sbis.go_to_contacts()

    contacts_page = SbisContactsPage(browser)
    try:
        assert contacts_page.get_region() == "Самарская обл.", "Регион не совпадает!"
    except AssertionError as e:
        print(e)

    try:
        assert contacts_page.is_partners_list_displayed(), "Список партнеров не отображается!"
    except AssertionError as e:
        print(e)
    

    contacts_page.change_region()
    try:
        assert contacts_page.get_region() == "Камчатский край", "Регион не изменился!"
    except AssertionError as e:
        print(e)
    
    try:
        assert "kamchatskij-kraj" in browser.current_url, "URL не содержит Камчатский край!"
    except AssertionError as e:
        print(e)
    try:
        assert "Камчатский край" in browser.title, "Title не содержит Камчатский край!"
    except AssertionError as e:
        print(e)
    try:
    
        assert contacts_page.is_partners_list_updated(), "Список партнеров не обновился!"
    except AssertionError as e:
        print(e)