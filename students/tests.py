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

        response = client.get('/students/edit/1/')
        self.assertEqual(response.status_code, 200)

        response = client.get('/students/create')
        self.assertEqual(response.status_code, 200)

        response = client.get('/students/delete/1/')
        self.assertEqual(response.status_code, 200)