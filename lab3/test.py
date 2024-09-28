import unittest
import shutil

task2 = __import__('2')
task3 = __import__('3')
task7 = __import__('7')
task11 = __import__('11')
task12 = __import__('12')
task13 = __import__('13')

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

    def test_task2(self):
        check('2.1', task2, self)

    def test_task3(self):
        check('3.1', task3, self)
        check('3.2', task3, self)

    def test_task7(self):
        check('7.1', task7, self)
        check('7.2', task7, self)

    def test_task11(self):
        check('11.1', task11, self)
        check('11.2', task11, self)

    def test_task12(self):
        check('12.1', task12, self)
        check('12.2', task12, self)
        check('12.3', task12, self)

    def test_task13(self):
        check('13.1', task13, self)
        check('13.2', task13, self)

if __name__ == '__main__':
    unittest.main()
