pt-triangle
===========
Description
-----------
Solution for PT Test Task.

Requirements
-----------
- Python 2.7.8
- ConfigObj - see https://pypi.python.org/pypi/configobj

Test Task
-----------
Web-application http://appsever/triangle.php handles legs parameter from GET request. 
legs is a three-element array, every element represents the triangle leg length - e.g. [1,1,1].
Application replies with XML:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<result>
	<triangle>True|False</triangle> <!-- True is it's triangle and False if it's not -->
	<type>0|1|2|3</type> <!-- 0 - triangle == False, 1 - triangle is isosceles, 2 - triangle is equilateral, 3 - triangle is "various" -->
</result>
```


Content
-----------
- ```data.ini``` - this file contains all test data in .ini format.
   1.  Every section represents type of triangle (NotTriangle, Isosceles, Equilateral, Various)
   2.  Every sections MUST contain Expected and StaticData subsections
     1. Expected subsection describes expected result: Content in XML response: Triangle and Type
     2. StaticData subsection describes data types and examples for static tests.
   3.  If you'd like to add new triangle type (e.g. )
- ```triangle.py``` - triangle generator for dynamic tests - all generator functions have the same name pattern:
  getTRIANGLE_TYPE(DATA_TYPE), where TRIANGLE_TYPE, DATA_TYPE must be specified in ```data.ini``` (as the section and one of the parameters in StaticData respectively)
- ```triangle_test.py``` - "Core" of all tests. It contains one test method only (overriden runTest)
- ```run_triangle_test.py``` - Suite "collector". It collects all test cases according to ```data.ini``` and type of test (dynamic or static).

Run Tests
----------
1. Set URI in triangle_test.py according to your environment.
2. If you want to run static test, just run ``` python run_triangle_test.py ``` (optionally with ```-t static```). For dynamic tests, run ```python run_triangle_test.py -t dynamic```

Extensibility
----------
To adapt this system for new functionality, you just need to manipulate ```data.ini``` and add respective handlers in ```triangle.py```. E.g., rectangular triangles detection has been just implemented:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<result>
	<triangle>True</triangle>
	<type>4</type>
</result>
```

So, we need to add section in ```data.ini``` and describe Expected result, copy/paste types of data and set new static values:
```ini
[Rectangular]
	[[Expected]]
	Triangle=True
	Type=4
	[[StaticData]]
	int=3,4,5
...
```
and add new generator function in ```triangle.py```:
```python
def getRectangular(leg_type):
  if(leg_type == 'int')
    a = getInt()
    b = getInt()
    c = a*a + b*b
  ...
```
Questions?
----------
Welcome - vic.ryzhkov@gmail.com
