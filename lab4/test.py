import unittest
import shutil

task1 = __import__('1')
task3 = __import__('3')
task4 = __import__('4')
task5 = __import__('5')
task6 = __import__('6')
task7 = __import__('7')
task8 = __import__('8')

def cmp_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i].strip() != arr2[i].strip():
            return False

    return True


def check(case, task, unittest):
    shutil.copyfile(f'tests/{case}_in.txt', 'input.txt')
    task.main()
    with open('output.txt') as output:
        result = output.read().split('\n')
    with open(f'tests/{case}_out.txt') as output:
        target = output.read().split('\n')
    unittest.assertTrue(cmp_arrays(target, result))


class TestLab2(unittest.TestCase):

    def test_task1(self):
        check('1.1', task1, self)

    def test_task3(self):
        check('3.1', task3, self)
        check('3.2', task3, self)
        check('3.3', task3, self)

    def test_task4(self):
        check('4.1', task4, self)

    def test_task5(self):
        check('5.1', task5, self)
        check('5.2', task5, self)

    def test_task6(self):
        check('6.1', task6, self)
        check('6.2', task6, self)

    def test_task7(self):
        check('7.1', task7, self)

    def test_task8(self):
        check('8.1', task8, self)

if __name__ == '__main__':
    unittest.main()