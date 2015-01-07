# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from students.views import Student
from datetime import date


class StudentTests(TestCase):

    def test_student_create(self):
        student_1 = Student.objects.create(
            name='name',
            surname='surname',
            birth_date=date(1999, 1, 22),
            email='student_1@test.com',
            phone='11111111',
        )

        student_2 = Student.objects.create(
            name='name',
            surname='surname',
            birth_date=date(1888, 2, 20),
            email='student_2@test.com',
            phone='2222222',
        )

        self.assertEqual(Student.objects.all().count(), 2)

    def test_page(self):
        client = Client()

        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)

        student_1 = Student.objects.create(
            name='name',
            surname='surname',
            birth_date=date(1999, 1, 22),
            email='test@test.com',
            phone='11111111',
        )

        response = client.get('/students/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u'Персональные данные')
        self.assertContains(response, u'Дополнительно')
        self.assertContains(response, u'Дополнительная информация')

        response = client.get('/students/edit/1/')
        self.assertEqual(response.status_code, 200)

        response = client.get('/students/create')
        self.assertEqual(response.status_code, 200)

        response = client.get('/students/delete/1/')
        self.assertEqual(response.status_code, 200)

    def test_student_fields(self):
        students = Student.objects.all()
        for student in students:
            self.assertTrue(student.name)
            self.assertTrue(student.surname)
            self.assertTrue(student.email)
            self.assertTrue(student.phone)


from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class StudentsSeleniumTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(StudentsSeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(StudentsSeleniumTests, cls).tearDownClass()

    def test_courses(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/students/'))
        import time
        time.sleep(1)

        student_1 = Student.objects.create(
            name='name',
            surname='surname',
            birth_date=date(1999, 1, 22),
            email='student_1@test.com',
            phone='11111111',
        )

        self.selenium.get('%s%s' % (self.live_server_url, '/students/1'))
        time.sleep(1)

        self.selenium.find_element_by_xpath('//a[@id="add"]').click()
        time.sleep(1)

        name_input = self.selenium.find_element_by_id('id_name')
        name_input.send_keys('name')
        surname_input = self.selenium.find_element_by_id('id_surname')
        surname_input.send_keys('surname')
        birth_date_input = self.selenium.find_element_by_id('id_birth_date')
        birth_date_input.send_keys('2014-01-02')
        email_input = self.selenium.find_element_by_id('id_email')
        email_input.send_keys('test@test.com')
        phone_input = self.selenium.find_element_by_id('id_phone')
        phone_input.send_keys('1234567890')
        package_input = self.selenium.find_element_by_id('id_package_0')
        package_input.click()
        time.sleep(1)

        self.selenium.find_element_by_xpath('//button[@type="submit"]').submit()
        time.sleep(10)

        self.selenium.get('%s%s' % (self.live_server_url, '/students/edit/1/'))
        time.sleep(3)

        name_input = self.selenium.find_element_by_id('id_name')
        name_input.send_keys('_edit')
        surname_input = self.selenium.find_element_by_id('id_surname')
        surname_input.send_keys('_edit')
        package_input = self.selenium.find_element_by_id('id_package_0')
        package_input.click()
        time.sleep(10)

        self.selenium.find_element_by_xpath('//button[@type="submit"]').submit()
        time.sleep(20)