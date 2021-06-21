#from django.test import TestCase
from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):

    def test_rool_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
class SmokeTest(TestCase):
    def test_good_maths(self):
        self.assertEqual(1 + 1, 2)

#    def test_bad_maths(self):
#       self.assertEqual(1 + 1, 3)