def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    def to_divide(x):
        assert type(x) == int  or type(x) == float, "You can only use numbers."
        return x / n

    return to_divide


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):
        def setUp(self):
            self.divisions = {
                6: [3, 18],
                20: [5, 100],
                3: [18, 54],
                5: [3.0, 15.0],
                20.22: [5, 101.1],
            }

        def test_closure_make_division_by(self):
            for key, values in self.divisions.items():
                self.assertEqual(key, make_division_by(values[0])(values[1]))
        
        def tearDown(self):
            del(self.divisions)


    unittest.main()
    # run()
