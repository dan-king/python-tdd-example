from selenium import webdriver

import unittest

class NewVisitorTest(unittest.TestCase):

    # 'setUp' and 'tearDown' are built-in to unittext
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
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

        # Fail on purpose as reminder to finish writing tests
        self.fail('TODO: Finish writing tests.')


# Only run tests if script invoked via CLI
if __name__ == '__main__':
    #unittest.main(warnings='ignore')
    unittest.main()

