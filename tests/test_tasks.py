import unittest

import tasks

DATE = '20.12.01'


class DummySerializer:
    def load(self):
        return {}
    
    def save(self, obj):
        pass


class TestTasks(unittest.TestCase):
    def setUp(self):
        self.tasks = tasks.Tasks(DummySerializer())

    def test_read_empty(self):
        with self.assertRaises(KeyError) as context:
            self.tasks.read(DATE)

    def test_create_one_task(self):
        self.tasks.create(DATE, 'Make coffee')
        self.assertEqual(self.tasks.read(DATE), ['Make coffee'])

    def test_create_two_tasks(self):
        self.tasks.create(DATE, 'Make coffee')
        self.tasks.create(DATE, 'Wake up')
        self.assertEqual(self.tasks.read(DATE), ['Make coffee', 'Wake up'])

    def test_delete(self):
        self.tasks.create(DATE, 'Make coffee')
        self.tasks.delete(DATE, 0)
        self.assertEqual(self.tasks.read(DATE), [])

    def test_update(self):
        self.tasks.create(DATE, 'Make coffee')
        self.tasks.update(DATE, 0, 'Wake up')
        self.assertEqual(self.tasks.read(DATE), ['Wake up'])

