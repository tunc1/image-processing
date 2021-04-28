from unittest import TestCase
import image_processing
import numpy

class ImageProcessingTest(TestCase):

    def test_grayscale(self):
        input=numpy.array([[[154,241,97],[231,159,36]],[[12,183,246],[78,132,222]]])
        expected=numpy.array([[164,142],[147,144]])
        output=image_processing.grayscale(input)
        self.assertTrue(numpy.array_equal(output,expected))