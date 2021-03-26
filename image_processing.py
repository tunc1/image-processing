import numpy

def grayscale(array):
    new_array=[]
    for rows in array:
        tmp=[]
        for pixel in rows:
            mean=0
            for color in pixel:
                mean+=color
            mean/=3
            tmp.append(mean)
        new_array.append(tmp)
    return numpy.array(new_array)

def bitmap(array,threshold):
    new_array=[]
    for rows in array:
        tmp=[]
        for pixel in rows:
            mean=0
            for color in pixel:
                mean+=color
            mean/=3
            tmp.append(255 if mean>threshold else 0)
        new_array.append(tmp)
    return numpy.array(new_array)