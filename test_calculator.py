

import unittest
from salary_calculator import calculate_salary


class TestSalaryCalculator(unittest.TestCase):  # Fixed TestCase definition
    def test_gross_and_net_salary(self):

        hours_worked = 40
        hourly_rate = 25
        deductions = 100
        gross, net = calculate_salary(hours_worked, hourly_rate, deductions)
        self.assertEqual(gross, 1000)
        self.assertEqual(net, 900)

        deductions = 0
        gross, net = calculate_salary(hours_worked, hourly_rate, deductions)
        self.assertEqual(gross, 1000)
        self.assertEqual(net, 1000)




        hours_worked = 0
        gross, net = calculate_salary(hours_worked, hourly_rate, deductions)
        self.assertEqual(gross, 0)
        self.assertEqual(net, 0)


if __name__ == '__main__':
    unittest.main()
