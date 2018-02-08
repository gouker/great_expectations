import json
import os
import random
import unittest

import numpy as np

import great_expectations as ge
from great_expectations.dataset import PandasDataSet, MetaPandasDataSet
from .util import assertDeepAlmostEqual

def isprime(n):
    #https://stackoverflow.com/questions/18833759/python-prime-number-checker
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # all other even numbers are not primes
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


class CustomPandasDataSet(PandasDataSet):

    @MetaPandasDataSet.column_map_expectation
    def expect_column_values_to_be_prime(self, column):
        return column.map(isprime)


class TestCustomClass(unittest.TestCase):

    def test_custom_class(self):
        script_path = os.path.dirname(os.path.realpath(__file__))
        df = ge.read_csv(
            script_path+'/test_sets/Titanic.csv',
            dataset_class=CustomPandasDataSet
        )
        df.set_default_expectation_argument("output_format", "COMPLETE")

        self.assertEqual(
            df.expect_column_values_to_be_prime('Age'),
            {'exception_list':[30.0,25.0,0.92000000000000004,63.0,39.0,58.0,50.0,24.0,36.0,26.0,25.0,25.0,28.0,45.0,39.0,30.0,58.0,45.0,22.0,48.0,44.0,60.0,45.0,58.0,36.0,33.0,36.0,36.0,14.0,49.0,36.0,46.0,27.0,27.0,26.0,64.0,39.0,55.0,70.0,69.0,36.0,39.0,38.0,27.0,27.0,4.0,27.0,50.0,48.0,49.0,48.0,39.0,36.0,30.0,24.0,28.0,64.0,60.0,49.0,44.0,22.0,60.0,48.0,35.0,22.0,45.0,49.0,54.0,38.0,58.0,45.0,46.0,25.0,21.0,48.0,49.0,45.0,36.0,55.0,52.0,24.0,16.0,44.0,51.0,42.0,35.0,35.0,38.0,35.0,50.0,49.0,46.0,58.0,42.0,40.0,42.0,55.0,50.0,16.0,21.0,30.0,15.0,30.0,46.0,54.0,36.0,28.0,65.0,33.0,44.0,55.0,36.0,58.0,64.0,64.0,22.0,28.0,22.0,18.0,52.0,46.0,56.0,33.0,27.0,55.0,54.0,48.0,18.0,21.0,34.0,40.0,36.0,50.0,39.0,56.0,28.0,56.0,56.0,24.0,18.0,24.0,45.0,40.0,6.0,57.0,32.0,62.0,54.0,52.0,62.0,63.0,46.0,52.0,39.0,18.0,48.0,49.0,39.0,46.0,64.0,60.0,60.0,55.0,54.0,21.0,57.0,45.0,50.0,50.0,27.0,20.0,51.0,21.0,36.0,40.0,32.0,33.0,30.0,28.0,18.0,34.0,32.0,57.0,18.0,36.0,28.0,51.0,32.0,28.0,36.0,4.0,1.0,12.0,34.0,26.0,27.0,15.0,45.0,40.0,20.0,25.0,36.0,25.0,42.0,26.0,26.0,0.82999999999999996,54.0,44.0,52.0,30.0,30.0,27.0,24.0,35.0,8.0,22.0,30.0,20.0,21.0,49.0,8.0,28.0,18.0,28.0,22.0,25.0,18.0,32.0,18.0,42.0,34.0,8.0,21.0,38.0,38.0,35.0,35.0,38.0,24.0,16.0,26.0,45.0,24.0,21.0,22.0,34.0,30.0,50.0,30.0,1.0,44.0,28.0,6.0,30.0,45.0,24.0,24.0,49.0,48.0,34.0,32.0,21.0,18.0,21.0,52.0,42.0,36.0,21.0,33.0,34.0,22.0,45.0,30.0,26.0,34.0,26.0,22.0,1.0,25.0,48.0,57.0,27.0,30.0,20.0,45.0,46.0,30.0,48.0,54.0,64.0,32.0,18.0,32.0,26.0,20.0,39.0,22.0,24.0,28.0,50.0,20.0,40.0,42.0,21.0,32.0,34.0,33.0,8.0,36.0,34.0,30.0,28.0,0.80000000000000004,25.0,50.0,21.0,25.0,18.0,20.0,30.0,30.0,35.0,22.0,25.0,25.0,14.0,50.0,22.0,27.0,27.0,30.0,22.0,35.0,30.0,28.0,12.0,40.0,36.0,28.0,32.0,4.0,36.0,33.0,32.0,26.0,30.0,24.0,18.0,42.0,16.0,35.0,16.0,25.0,18.0,20.0,30.0,26.0,40.0,24.0,18.0,0.82999999999999996,20.0,25.0,35.0,32.0,20.0,39.0,39.0,6.0,38.0,9.0,26.0,4.0,20.0,26.0,25.0,18.0,24.0,35.0,40.0,38.0,9.0,45.0,27.0,20.0,32.0,33.0,18.0,40.0,26.0,15.0,45.0,18.0,27.0,22.0,26.0,22.0,20.0,32.0,21.0,18.0,26.0,6.0,9.0,40.0,32.0,26.0,18.0,20.0,22.0,22.0,35.0,21.0,20.0,18.0,18.0,38.0,30.0,21.0,21.0,21.0,24.0,33.0,33.0,28.0,16.0,28.0,24.0,21.0,32.0,26.0,18.0,20.0,24.0,24.0,36.0,30.0,22.0,35.0,27.0,30.0,36.0,9.0,44.0,45.0,22.0,30.0,34.0,28.0,0.33000000000000002,27.0,25.0,24.0,22.0,21.0,26.0,33.0,1.0,0.17000000000000001,25.0,36.0,36.0,30.0,26.0,65.0,42.0,32.0,30.0,24.0,24.0,24.0,22.0,18.0,16.0,45.0,21.0,18.0,9.0,48.0,16.0,25.0,38.0,22.0,16.0,33.0,9.0,38.0,40.0,14.0,16.0,9.0,10.0,6.0,40.0,32.0,20.0,28.0,24.0,28.0,24.0,20.0,45.0,26.0,21.0,27.0,18.0,26.0,22.0,28.0,22.0,27.0,42.0,27.0,25.0,27.0,20.0,48.0,34.0,22.0,33.0,32.0,26.0,49.0,1.0,33.0,4.0,24.0,32.0,27.0,21.0,32.0,20.0,21.0,30.0,21.0,22.0,4.0,39.0,20.0,21.0,44.0,42.0,21.0,24.0,25.0,22.0,22.0,39.0,26.0,4.0,22.0,26.0,1.5,36.0,18.0,25.0,22.0,20.0,26.0,22.0,32.0,21.0,21.0,36.0,39.0,25.0,45.0,36.0,30.0,20.0,21.0,1.5,25.0,18.0,63.0,18.0,15.0,28.0,36.0,28.0,10.0,36.0,30.0,22.0,14.0,22.0,51.0,18.0,45.0,28.0,21.0,27.0,36.0,27.0,15.0,27.0,26.0,22.0,24.0],'exception_index_list':[2,3,4,6,7,8,15,16,17,20,21,22,24,25,26,27,28,30,31,34,36,38,39,42,43,44,47,48,49,51,53,55,57,63,64,67,69,70,72,73,74,75,76,78,80,86,87,88,89,90,91,92,95,98,99,101,103,104,106,108,109,110,111,113,115,116,117,120,121,123,124,126,127,128,129,130,131,132,134,135,136,140,141,142,143,144,145,146,147,149,150,151,153,156,157,161,162,163,164,167,168,169,170,174,175,176,177,179,180,181,184,186,187,191,193,194,195,198,201,203,204,205,212,214,215,216,219,220,222,226,227,228,229,230,231,232,233,234,235,236,238,240,241,242,243,245,246,247,249,251,253,255,256,257,258,259,261,262,264,270,271,272,273,274,275,276,277,279,280,281,282,283,285,288,306,309,316,322,323,324,326,327,328,329,331,332,333,334,336,337,338,339,340,341,344,346,347,348,349,350,351,352,353,355,356,357,358,362,363,364,365,366,372,373,374,376,377,378,380,382,383,384,385,386,388,389,390,391,392,393,395,396,397,401,406,408,409,410,411,412,413,414,415,416,417,418,420,421,422,423,425,426,427,428,429,432,434,435,436,437,439,440,441,442,445,447,448,449,450,454,463,465,468,472,473,475,476,477,478,483,485,487,493,495,496,497,499,503,504,506,509,510,511,513,515,518,520,521,523,525,527,528,529,530,531,532,533,536,538,539,540,541,542,544,545,547,549,552,553,554,555,557,558,559,561,563,564,565,566,568,570,571,572,573,574,575,578,579,580,581,582,584,588,589,593,596,598,599,601,602,604,605,606,607,608,609,610,611,612,613,615,616,618,619,620,622,623,624,625,626,629,630,631,633,634,635,636,637,638,639,640,641,643,649,652,654,655,656,661,662,663,664,665,666,667,668,670,671,672,673,674,675,676,677,680,681,682,684,685,686,689,690,691,692,693,695,696,697,699,701,702,703,706,707,708,709,710,712,714,715,717,719,720,721,723,724,725,728,729,732,733,735,736,738,741,744,745,748,749,750,751,752,753,754,755,756,760,761,762,763,764,765,766,767,770,772,774,776,778,779,782,783,785,787,788,789,806,807,808,809,810,813,815,816,817,819,821,823,824,826,827,828,829,830,832,833,835,837,839,843,844,845,847,848,849,855,857,858,860,864,865,869,872,875,876,878,881,882,886,887,888,889,891,892,893,894,895,896,903,904,905,906,907,909,910,911,913,914,915,917,920,921,922,923,924,928,929,930,931,932,933,934,935,936,937,938,940,946,947,948,951,958,960,961,962,963,964,965,966,967,968,1181,1188,1258,1263,1264,1269,1272,1273,1274,1275,1276,1277,1278,1279,1283,1284,1291,1292,1293,1297,1298,1299,1301,1303,1304,1308,1309,1310,1311],'success':False}
        )

        primes = [3,5,7,11,13,17,23,31]
        df["primes"] = df.Age.map(lambda x: random.choice(primes))
        self.assertEqual(
            df.expect_column_values_to_be_prime("primes"),
            {'exception_list': [], 'exception_index_list': [], 'success': True}
        )

   # Ensure that Custom Data Set classes can properly call non-overridden methods from their parent class
    def test_base_class_expectation(self):
        df = CustomPandasDataSet({
            "aaa": [1, 2, 3, 4, 5],
            "bbb": [10, 20, 30, 40, 50],
            "ccc": [9, 10, 11, 12, 13],
        })


        self.assertEqual(
            df.expect_column_values_to_be_between("aaa", min_value=1, max_value=5)['success'],
            True
        )


class TestValidation(unittest.TestCase):
    def test_validate(self):

        with open("./tests/test_sets/titanic_expectations.json") as f:
            my_expectations_config = json.load(f)

        my_df = ge.read_csv(
            "./tests/test_sets/Titanic.csv",
            expectations_config=my_expectations_config
        )
        my_df.set_default_expectation_argument("output_format", "COMPLETE")

        results = my_df.validate(catch_exceptions=False)
        # print json.dumps(results, indent=2)

        with open('./tests/test_sets/expected_results_20170721.json') as f:
            expected_results = json.load(f)
            # print json.dumps(expected_results, indent=2)

        self.maxDiff = None
        #!!! This needs to be converted to unicode, I think

        # print json.dumps(results, indent=2)
        # print '-'*80
        # print json.dumps(expected_results, indent=2)
        # self.assertEqual(
        #     json.loads(json.dumps(results)),
        #     json.loads(json.dumps(expected_results))
        # )
        assertDeepAlmostEqual(self,
                              results,
                              expected_results
                              )

        #Now, change the results and ensure they are no longer equal
        results[0] = {}
        self.assertNotEqual(results,
                            expected_results
                            )


        validation_results = my_df.validate(only_return_failures=True)
        # print json.dumps(validation_results, indent=2)
        assertDeepAlmostEqual(
            self,
            validation_results,
            {"results": [{"exception_traceback": None, "expectation_type": "expect_column_values_to_be_in_set", "success": False, "exception_list": ["*"], "raised_exception": False, "kwargs": {"column": "PClass", "output_format": "COMPLETE", "values_set": ["1st", "2nd", "3rd"]}, "exception_index_list": [456]}]}
        )



class TestRepeatedAppendExpectation(unittest.TestCase):
    def test_validate(self):

        with open("./tests/test_sets/titanic_expectations.json") as f:
            my_expectations_config = json.load(f)

        my_df = ge.read_csv("./tests/test_sets/Titanic.csv")

        self.assertEqual(
            len(my_df.get_expectations_config()['expectations']),
            7
        )

        #For column_expectations, append_expectation should only replace expectations where the expetation_type AND the column match
        my_df.expect_column_to_exist("PClass")
        self.assertEqual(
            len(my_df.get_expectations_config()['expectations']),
            7
        )


if __name__ == "__main__":
    unittest.main()
