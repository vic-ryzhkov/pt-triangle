from triangle_test import TriangleServiceTest
from triangle import getInput
from configobj import ConfigObj
import sys, getopt
import unittest

TEST_DATA_FILE = 'data.ini'

HELP_MESSAGE = """Usage: python run_triangle_test.py [OPTION][ARG]
OPTIONS:\n
-t <TYPE>, --type=<TYPE> - run <TYPE> tests (dynamic or static. Default: static)"""
if __name__ == '__main__':
    try: ## Check (and parse) options in argv (-t, -d, -a, -v)
        opts,args = getopt.getopt(sys.argv[1:], 't:',['type='])
    except:
        print HELP_MESSAGE
        sys.exit(-1)
    
    for o,a in opts:
        if o == '-t' or o =='--type':
            TEST_TYPE = a.lower()
            
    TEST_DATA = ConfigObj(TEST_DATA_FILE)
    triangles = TEST_DATA.sections
    suite = unittest.TestSuite()
    for triangle_type in triangles:
        expected_data = TEST_DATA[triangle_type]['Expected']
        expected_triangle = expected_data['Triangle']
        expected_type = expected_data['Type']
        input_data = TEST_DATA[triangle_type]['StaticData']
        for data in input_data:
            tt = TriangleServiceTest()
            tt.test_name = triangle_type + data
            tt.input = getInput(TEST_TYPE, triangle_type, data, input_data[data]) 
            tt.expected_triangle = expected_triangle
            tt.expected_type = expected_type
            suite.addTest(tt)
                   
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite) # Run suite!