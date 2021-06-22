from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    # 'setUp' and 'tearDown' are built-in to unittext
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        if False:
            self.browser.quit()

    # Custom method to ensure browser opened to expected page
    def test_can_start_a_list_and_retrieve_it_later(self):

        # Start session with a new browser window at the site URL
        self.browser.get('http://localhost:8000')

        # Confirm that the web browser page title matches how it was coded
        self.assertIn('To-Do', self.browser.title)

        # Conform that the page has main heading matching text as coded
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Confirm there is an input field with expected placeholder value
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        )

        # Enter a value into the input field
        inputbox.send_keys('Find a feather')

        # Hit return on the input field
        inputbox.send_keys(Keys.ENTER)

        # Wait a moment for the page to update
        time.sleep(1)

        # After hitting enter the page loads showing the new value that was just entered.
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == 'Find a feather' for row in rows),
            "The new to-do item was not found in the output list."
        )

        # Fail on purpose as reminder to finish writing tests
        self.fail('TODO: Finish writing tests.')


# Only run tests if script invoked via CLI
if __name__ == '__main__':
    #unittest.main(warnings='ignore')
    unittest.main()

