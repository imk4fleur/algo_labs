import unittest
import shutil

task1 = __import__('1')
task2 = __import__('2')
task3 = __import__('3')
task4 = __import__('4')
task6 = __import__('6')
task7 = __import__('7')
task8 = __import__('8')
task16 = __import__('16')

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
        check('1.2', task1, self)

    def test_task2(self):
        check('2.1', task2, self)
        check('2.2', task2, self)

    def test_task3(self):
        check('3.1', task3, self)

    def test_task4(self):
        check('4.1', task4, self)

    def test_task6(self):
        check('6.1', task6, self)
        check('6.2', task6, self)
        check('6.3', task6, self)
        check('6.4', task6, self)
        check('6.5', task6, self)
        check('6.6', task6, self)

    def test_task7(self):
        check('7.1', task7, self)
        check('7.2', task7, self)
        check('7.3', task7, self)
        check('7.4', task7, self)
        check('7.5', task7, self)
        check('7.6', task7, self)
        check('7.7', task7, self)


    def test_task8(self):
        check('8.1', task8, self)

    def test_task16(self):
        check('16.1', task16, self)

if __name__ == '__main__':
    unittest.main()
