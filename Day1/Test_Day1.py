import unittest
import Day1


class TestDay1(unittest.TestCase):
    def test_getFactorial(self):
        number = 8
        result = Day1.getFactorial(number)
        self.assertEquals(result, 40320)

    def test_getFactorialIncorrectInput(self):
        number = 'fjdakfdjla'
        result = Day1.getFactorial(number)
        self.assertIsInstance(result, TypeError)

    def test_getFactorialFloatInput(self):
        number = 5.40
        result = Day1.getFactorial(number)
        self.assertIsInstance(result, TypeError)

    def test_generateDictionary(self):
        number = 8
        result = Day1.generateDictionary(number)
        self.assertEquals(result, {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64})

    def test_generateDictionaryIncorrectInput(self):
        number = 'fjkdl;jafkl;'
        result = Day1.generateDictionary(number)
        self.assertIsInstance(result, TypeError)

    def test_generateDictionaryFloatInput(self):
        number = 4.30
        result = Day1.generateDictionary(number)
        self.assertIsInstance(result, TypeError)


if __name__ == '__main__':
    unittest.main()
