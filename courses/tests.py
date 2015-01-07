from django.test import TestCase, Client
from courses.views import Course
from coaches.views import Coach
from datetime import date


class CourseTests(TestCase):

    def test_course_create(self):
        teacher = Coach.objects.create(
            name='name',
            surname='surname',
            birth_date=date(1988, 3, 1),
            email='teacher@test.com',
            phone='1111111',
        )

        course_1 = Course.objects.create(
            course_name='course_1',
            start_date=date(1989, 1, 1),
            end_date=date(1990, 1, 1),
            teacher=teacher,
            slug='1',
        )

        course_2 = Course.objects.create(
            course_name='course_2',
            start_date=date(1989, 1, 1),
            end_date=date(1990, 1, 1),
            teacher=teacher,
            slug='2',
        )

        self.assertEqual(Course.objects.all().count(), 2)

    def test_page(self):
        client = Client()

        response = client.get('/courses/')
        self.assertEqual(response.status_code, 200)

        response = client.get('/courses/1')
        self.assertEqual(response.status_code, 404)

        teacher = Coach.objects.create(
            name='name',
            surname='surname',
            birth_date=date(1988, 3, 1),
            email='teacher@test.com',
            phone='1111111',
        )

        course_1 = Course.objects.create(
            course_name='course_1',
            start_date=date(1989, 1, 1),
            end_date=date(1990, 1, 1),
            teacher=teacher,
            slug='3',
        )

        response = client.get('/courses/1')
        self.assertEqual(response.status_code, 200)

        response = client.get('/courses/edit/1/')
        self.assertEqual(response.status_code, 200)

        response = client.get('/courses/create')
        self.assertEqual(response.status_code, 200)

        response = client.get('/courses/delete/1/')
        self.assertEqual(response.status_code, 200)