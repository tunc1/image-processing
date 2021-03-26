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

def increase_each_pixel(array,value):
    for y in range(len(array)):
        for x in range(len(array[0])):
            for z in range(len(array[0,0])):
                old=array[y,x,z]
                if value+old<256:
                    array[y,x,z]+=value
                else:
                    array[y,x,z]=255
    return array

def decrease_each_pixel(array,value):
    for y in range(len(array)):
        for x in range(len(array[0])):
            for z in range(len(array[0,0])):
                old=array[y,x,z]
                if old-value>-1:
                    array[y,x,z]-=value
                else:
                    array[y,x,z]=0
    return array