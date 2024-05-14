import unittest

from django.db import transaction

from secondapp.models import Customer, Movie, Rating


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    @transaction.atomic()
    def test_something2(self):
        c = Customer()
        c.name = 'Bahadir'
        c.email = 'bahadir@localhost'
        c.password = '<PASSWORD>'
        c.age = 27
        c.save()

        m = Movie()
        m.name = 'The Movie'
        m.release_date = '20/9/2024'
        m.description = 'This is the movie.'
        m.save()

    def test_txns(self):
        pass


if __name__ == '__main__':
    unittest.main()
