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