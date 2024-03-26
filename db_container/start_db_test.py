import unittest
import start_db as test_module


"""
Test creating volume and database
"""
class TestContainer(unittest.TestCase):

    @classmethod
    def setUp(self):
        # Create the container object
        self.container = test_module.ContainerCreate()

    def test_volume_create(self):
        self.container.create_volume(volume_name='testcladis')
        # self.assertEqual(self.container.volume_name, 'testcladis')



"""
Test initialized databases
"""
class TestDB(unittest.TestCase):
    pass


# Only run if executing, not import
if __name__ == '__main__':

    unittest.main()
