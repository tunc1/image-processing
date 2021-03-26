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

def mirror_horizontally(array):
    image_width=len(array[0])
    for y in range(len(array)):
        for x in range(int(image_width/2)):
            tmp=array[y,x].copy()
            array[y,x]=array[y,image_width-x-1]
            array[y,image_width-x-1]=tmp
    return array


def mirror_vertically(array):
    image_height=len(array)
    for y in range(int(image_height/2)):
        for x in range(len(array[0])):
            tmp=array[y,x].copy()
            array[y,x]=array[image_height-y-1,x]
            array[image_height-y-1,x]=tmp
    return array