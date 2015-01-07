# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from coaches.views import Coach
from datetime import date


class CoachTests(TestCase):

    def test_coach_create(self):
        coach_1 = Coach.objects.create(
            name='name',
            surname='surname',
            birth_date=date(1990, 1, 1),
            email='email@mail.com',
            phone='1111111',
        )

        coach_2 = Coach.objects.create(
            name='name',
            surname='surname',
            birth_date=date(1990, 1, 1),
            email='email@mail.com',
            phone='22222222',
        )

        self.assertEqual(Coach.objects.all().count(), 2)

    def test_page(self):
        client = Client()

        response = client.get('/coaches/')
        self.assertEqual(response.status_code, 200)

        response = client.get('/coaches/1')
        self.assertEqual(response.status_code, 404)

        teacher_1 = Coach.objects.create(
            name='name',
            surname='surname',
            birth_date=date(1988, 3, 1),
            email='teacher@test.com',
            phone='1111111',
        )

        response = client.get('/coaches/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u'Персональные данные')
        self.assertContains(response, u'Дополнительная информация')

        response = client.get('/coaches/edit/1/')
        self.assertEqual(response.status_code, 200)

        response = client.get('/coaches/create')
        self.assertEqual(response.status_code, 200)

        response = client.get('/coaches/delete/1/')
        self.assertEqual(response.status_code, 200)

    def test_coaches_fields(self):
        coaches = Coach.objects.all()
        for coach in coaches:
            self.assertTrue(coach.name)
            self.assertTrue(coach.surname)
            self.assertTrue(coach.phone)