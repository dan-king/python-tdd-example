from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 3
class NewVisitorTest(LiveServerTestCase):

    # 'setUp' and 'tearDown' are built-in to unittext
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        if False:
            self.browser.quit()

    def wait_for_row_text_in_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                # If max time hasn't been reached then continue to try again a fraction later
                print(f"waiting longer: current wait: {time.time() - start_time}")
                time.sleep(MAX_WAIT/20)

    # Custom method to ensure browser opened to expected page
    #def test_can_start_a_list_and_retrieve_it_later(self):
    def test_can_start_a_list_for_one_user(self):

        # Start session with a new browser window at the site URL
        self.browser.get(self.live_server_url)
        #self.browser.get('http://localhost:8000')

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

        # ########################################
        # Add first entry
        # ########################################
        # Enter a value into the input field
        inputbox.send_keys('Find a feather')

        # Hit return on the input field
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_text_in_table('1. Find a feather')

        # Wait a moment for the page to update
        # time.sleep(1)

        # After hitting enter the page loads showing the new value that was just entered.
        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == '1. Find a feather' for row in rows),
        #     "The new to-do item was not found in the output list." +
        #     f"\nContents were\n {table.text}"
        # )
        #self.assertIn('1. Find a feather', [row.text for row in rows])

        # ########################################
        # Add second entry
        # ########################################
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Find a cap')
        inputbox.send_keys(Keys.ENTER)
        #time.sleep(1)
        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
        self.wait_for_row_text_in_table('1. Find a feather')
        self.wait_for_row_text_in_table('2. Find a cap')

    def test_multiple_users_can_start_lists_at_different_urls(self):

        self.browser.get(self.live_server_url)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Find a feather')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_text_in_table('1. Find a feather')

        # Note the new url of the first user
        user1_list_url = self.browser.current_url
        self.assertRegex(user1_list_url, '/lists/.+')

        # Simulate a second user by re-opening browser
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Enusre second user does not see list items of first user
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Find a feather', page_text)
        self.assertNotIn('Find a cap', page_text)

        # Second user enters new list items
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_text_in_table('1. Buy milk')

        # Note the new url of the second user
        user2_list_url = self.browser.current_url
        self.assertRegex(user2_list_url, '/lists/.+')

        # Ensure the lists of the two users are not equal
        self.assertNotEqual(user1_list_url, user2_list_url)

        # Confirm currently not looking at user 1 lists, but rather, user 2
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Find a feather', page_text)
        self.assertNotIn('Find a cap', page_text)

        # Fail on purpose as reminder to finish writing tests
        #self.fail('TODO: Finish writing tests.')



# #################################
# Not needed when running tests from the Django test runner
# #################################
# Only run tests if script invoked via CLI
#if __name__ == '__main__':
    #unittest.main(warnings='ignore')
    #unittest.main()

