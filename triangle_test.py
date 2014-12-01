import unittest
import urllib2 as urllib
from xml.etree import cElementTree as ET

URI = 'http://192.168.85.141/triangle.php'

class TriangleServiceTest(unittest.TestCase):
    def runTest(self):
        xml = ET.fromstring(urllib.urlopen(URI + '?legs=' + self.input).read())
        actual_result = xml.find('result')
        actual_triangle = actual_result.find('triangle').text
        actual_type = actual_result.find('type').text
        self.assertEqual(actual_triangle, self.expected_triangle, self.test_name + ' ' + self.input + ':' + 'Triangle tags mismatch: Expected:' + self.expected_triangle + ",Actual:" + actual_triangle)
        self.assertEqual(actual_type, self.expected_type, self.test_name + ' ' + self.input + ':' + ' Type tags mismatch: Expected:' + self.expected_type + ",Actual:" + actual_type)