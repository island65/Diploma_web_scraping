import unittest

from src.merge_files import merge_files


class TestMergeFiles(unittest.TestCase):
    def test_merge_files(self):
        self.assertEqual(merge_files('test.csv', 'test_details.csv', 'test_merged.csv'), None)


if __name__ == '__main__':
    unittest.main()
