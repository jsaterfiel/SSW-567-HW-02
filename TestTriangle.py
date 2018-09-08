# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

__SCALENE__ = 'Scalene'
__EQUILATERAL__ = 'Equilateral'
__RIGHT__ = 'Right'
__ISOSCELES__ = 'Isoceles'
__NOT_A_TRIANGLE__ = 'NotATriangle'
__INVALID_INPUT__ = 'InvalidInput'

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual( classifyTriangle(3, 4, 5), __RIGHT__, '3, 4, 5 is a Right triangle' )

    def testRightTriangleB(self): 
        self.assertEqual( classifyTriangle(5, 3, 4), __RIGHT__, '5, 3, 4 is a Right triangle' )
    
    def testRightTriangleC(self): 
        self.assertEqual( classifyTriangle(4, 5, 3), __RIGHT__, '4, 5, 3 is a Right triangle' )

    def testRightTriangleD(self): 
        self.assertEqual( classifyTriangle(5, 12, 13), __RIGHT__, '5, 12, 13 is a Right triangle' )

    def testRightTriangleE(self): 
        self.assertEqual( classifyTriangle(24, 7, 25), __RIGHT__, '24, 7, 25 is a Right triangle' )
    
    def testRightTriangleLargeA(self): 
        self.assertEqual( classifyTriangle(32, 255, 257), __RIGHT__, '32, 255, 257 is a Right triangle' )

    def testRightTriangleLargeB(self): 
        self.assertEqual( classifyTriangle(255, 257, 32), __RIGHT__, '255, 257, 32 is a Right triangle' )

    def testRightTriangleLargeC(self): 
        self.assertEqual( classifyTriangle(257, 32, 255), __RIGHT__, '257, 32, 255 is a Right triangle' )
        
    def testEquilateralTrianglesSmall(self): 
        self.assertEqual( classifyTriangle(1, 1, 1), __EQUILATERAL__, '1, 1, 1 should be equilateral' )
    
    def testEquilateralTrianglesMed(self): 
        self.assertEqual( classifyTriangle(10, 10, 10), __EQUILATERAL__, '10, 10, 10 should be equilateral' )

    def testEquilateralTrianglesLarge(self): 
        self.assertEqual( classifyTriangle(1000, 1000, 1000), __EQUILATERAL__, '1000, 1000, 1000 should be equilateral' )

    def testScaleneA(self):
        self.assertEqual( classifyTriangle(4, 5, 6), __SCALENE__, '4, 5, 6 should be scalene' )

    def testScaleneB(self):
        self.assertEqual( classifyTriangle(5, 6, 4), __SCALENE__, '5, 6, 4 should be scalene' )

    def testScaleneC(self):
        self.assertEqual( classifyTriangle(6, 4, 5), __SCALENE__, '6, 4, 5 should be scalene' )
    
    def testScaleneLargeA(self):
        self.assertEqual( classifyTriangle(600, 400, 500), __SCALENE__, '600, 400, 500 should be scalene' )

    def testScaleneLargeB(self):
        self.assertEqual( classifyTriangle(400, 500, 600), __SCALENE__, '400, 500, 600 should be scalene' )

    def testScaleneLargeC(self):
        self.assertEqual( classifyTriangle(500, 600, 400), __SCALENE__, '500, 600, 400 should be scalene' )

    def testIsoscelesA(self):
        self.assertEqual( classifyTriangle(3, 4, 4), __ISOSCELES__ , '3, 4, 4 should be isosceles' )

    def testIsoscelesB(self):
        self.assertEqual( classifyTriangle(4, 3, 4), __ISOSCELES__ , '4, 3, 4 should be isosceles' )

    def testIsoscelesC(self):
        self.assertEqual( classifyTriangle(4, 4, 3), __ISOSCELES__ , '4, 4, 3 should be isosceles' )
    
    def testIsoscelesLargeA(self):
        self.assertEqual( classifyTriangle(400, 400, 300), __ISOSCELES__ , '400, 400, 300 should be isosceles' )
    
    def testIsoscelesLargeB(self):
        self.assertEqual( classifyTriangle(300, 400, 400), __ISOSCELES__ , '300, 400, 400 should be isosceles' )

    def testIsoscelesLargeC(self):
        self.assertEqual( classifyTriangle(400, 300, 400), __ISOSCELES__ , '400, 300, 400 should be isosceles' )

    def testNotATriangleA(self):
        self.assertEqual( classifyTriangle(2, 3, 10), __NOT_A_TRIANGLE__ , '2, 3, 10 is not a triangle' )

    def testNotATriangleB(self):
        self.assertEqual( classifyTriangle(2, 10, 3), __NOT_A_TRIANGLE__ , '2, 10, 3 is not a triangle' )

    def testNotATriangleC(self):
        self.assertEqual( classifyTriangle(10, 2, 3), __NOT_A_TRIANGLE__ , '10, 2, 3 is not a triangle' )

    def testBadInputsFloatA(self):
        self.assertEqual( classifyTriangle(1, 0.25, 3), __INVALID_INPUT__ , '1, 0.25, 3 is invalid input' )
    
    def testBadInputsFloatB(self):
        self.assertEqual( classifyTriangle(0.25, 1, 3), __INVALID_INPUT__ , '0.25, 1, 3 is invalid input' )
    
    def testBadInputsFloatC(self):
        self.assertEqual( classifyTriangle(1, 3, 0.25), __INVALID_INPUT__ , '1, 3, 0.25 is invalid input' )
    
    def testBadInputsNegA(self):
        self.assertEqual( classifyTriangle(-1, 4, 4), __INVALID_INPUT__ , '-1, 4, 4 is invalid input' )

    def testBadInputsNegB(self):
        self.assertEqual( classifyTriangle(4, -1, 4), __INVALID_INPUT__ , '4, -1, 4 is invalid input' )

    def testBadInputsNegC(self):
        self.assertEqual( classifyTriangle(4, 4, -1), __INVALID_INPUT__ , '4, 4, -1 is invalid input' )

    def testBadInputsObjA(self):
        self.assertEqual( classifyTriangle(False, 2, 1), __INVALID_INPUT__ , 'False, 2, 1 is invalid input' )

    def testBadInputsObjB(self):
        self.assertEqual( classifyTriangle(4, False, 1), __INVALID_INPUT__ , '4, False, 1 is invalid input' )

    def testBadInputsObjC(self):
        self.assertEqual( classifyTriangle(4, 2, True), __INVALID_INPUT__ , '4, 2, True is invalid input' )
    
    def testBadInputsZeroA(self):
        self.assertEqual( classifyTriangle(4, 4, 0), __INVALID_INPUT__ , '4, 4, 0 is invalid input' )
    
    def testBadInputsZeroB(self):
        self.assertEqual( classifyTriangle(4, 0, 4), __INVALID_INPUT__ , '4, 0, 4 is invalid input' )
    
    def testBadInputsZeroC(self):
        self.assertEqual( classifyTriangle(0, 4, 4), __INVALID_INPUT__ , '0, 4, 4 is invalid input' )

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

