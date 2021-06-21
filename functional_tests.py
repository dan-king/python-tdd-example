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

        self.browser.get('http://localhost:8000')

        #self.assertIn('Django', self.browser.title)
        self.assertIn('To-Do', self.browser.title)

        # Fail on purpose as reminder to finish writing tests
        self.fail('TODO: Finish writing tests.')


# Only run tests if script invoked via CLI
if __name__ == '__main__':
    #unittest.main(warnings='ignore')
    unittest.main()

