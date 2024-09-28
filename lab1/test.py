import unittest
import shutil

task3 = __import__('3')
task5 = __import__('5')
task9 = __import__('9')
task14 = __import__('14')
task17 = __import__('17')
task18 = __import__('18')
task20 = __import__('20')

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


class TestLab1(unittest.TestCase):
    def test_task3(self):
        check('3.1', task3, self)
        check('3.2', task3, self)

    def test_task5(self):
        check('5.1', task5, self)
        check('5.2', task5, self)
        check('5.3', task5, self)

    def test_task9(self):
        check('9.1', task9, self)
        check('9.2', task9, self)

    def test_task14(self):
        check('14.1', task14, self)
        check('14.2', task14, self)

    def test_task17(self):
        check('17.1', task17, self)
        check('17.2', task17, self)

    def test_task18(self):
        check('18.1', task18, self)
        check('18.2', task18, self)

    def test_task20(self):
        check('20.1', task20, self)
        check('20.2', task20, self)


if __name__ == '__main__':
    unittest.main()