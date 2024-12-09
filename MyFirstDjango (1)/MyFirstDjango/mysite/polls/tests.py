from django.test import TestCase, Client
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

from .models import Question

# Create your tests here.
class QuestionModelTests(TestCase):

    def setUp(self):
        Question.objects.create(question_text="Test question?", pub_date=datetime.datetime.now())

    def test_string_output(self):
        my_question = Question.objects.get(question_text="Test question?")
        self.assertEqual(str(my_question), "Test question?")


class ClientTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_polls_url(self):
        response = self.client.get("/polls/")
        self.assertEqual(response.status_code, 200)


class LoginTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.test_user = User.objects.create_user(
            username="MyTestName",
            email="email@email.com",
            password="testpassword"
        )

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        self.browser.get(self.live_server_url + "/accounts/login/")

        self.browser.implicitly_wait(5)
        username_input = self.browser.find_element(By.NAME, "username")
        username_input.send_keys("MyTestName")

        password_input = self.browser.find_element(By.NAME, "password")
        password_input.send_keys("testpassword")
        password_input.submit()

        time.sleep(5)





