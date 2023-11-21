import unittest
from language_target import LanguageTarget


class TestLanguageTarget(unittest.TestCase):

    def test_random_number_int_sample_is_int(self):
        language_target = LanguageTarget()
        result = language_target._int_sample
        self.assertIsInstance(result, int)

    def test_base_number_is_equal_language_len(self):
        language_target = LanguageTarget()
        language_list_len = len(language_target.LANGUAGES)
        self.assertEqual(
            language_target._get_base(),
            language_list_len
        )

if __name__ == "__main__":
    unittest.main()