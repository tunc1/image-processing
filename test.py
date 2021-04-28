from unittest import TestCase
import image_processing
import numpy

class ImageProcessingTest(TestCase):

    def test_grayscale(self):
        input=numpy.array([[[154,241,97],[231,159,36]],[[12,183,246],[78,132,222]]])
        expected=numpy.array([[164,142],[147,144]])
        output=image_processing.grayscale(input)
        self.assertTrue(numpy.array_equal(output,expected))

    def test_bitmap(self):
        input=numpy.array([[[64,151,7],[231,159,36]],[[12,183,246],[48,102,192]]])
        expected=numpy.array([[0,255],[255,0]])
        output=image_processing.bitmap(input)
        self.assertTrue(numpy.array_equal(output,expected))

    def test_increase_each_pixel(self):
        input=numpy.array([[[64,151,7],[231,159,36]],[[12,183,246],[48,102,192]]])
        expected=numpy.array([[[94,181,37],[255,189,66]],[[42,213,255],[78,132,222]]])
        output=image_processing.increase_each_pixel(input,30)
        self.assertTrue(numpy.array_equal(output,expected))

    def test_decrease_each_pixel(self):
        input=numpy.array([[[64,151,7],[231,159,36]],[[12,183,246],[48,102,192]]])
        expected=numpy.array([[[34,121,0],[201,129,6]],[[0,153,216],[18,72,162]]])
        output=image_processing.decrease_each_pixel(input,30)
        self.assertTrue(numpy.array_equal(output,expected))