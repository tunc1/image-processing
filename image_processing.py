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

def erosion(array,kernel_size=1):
    height=len(array)
    width=len(array[0])
    new_array=[]
    for y in range(height):
        new_row=[]
        for x in range(width):
            smallest=array[y,x]
            for i in range(1,kernel_size+1):
                if y-i>=0 and smallest>array[y-i,x]:
                    smallest=array[y-i,x]
                if x-i>=0 and smallest>array[y,x-i]:
                    smallest=array[y,x-i]
                if y+i<height and smallest>array[y+i,x]:
                    smallest=array[y+i,x]
                if x+i<width and smallest>array[y,x+i]:
                    smallest=array[y,x+i]
            new_row.append(smallest)
        new_array.append(new_row)
    return numpy.array(new_array)

def dilation(array,kernel_size=1):
    height=len(array)
    width=len(array[0])
    new_array=[]
    for y in range(height):
        new_row=[]
        for x in range(width):
            biggest=array[y,x]
            for i in range(1,kernel_size+1):
                if y-i>=0 and biggest<array[y-i,x]:
                    biggest=array[y-i,x]
                if x-i>=0 and biggest<array[y,x-i]:
                    biggest=array[y,x-i]
                if y+i<height and biggest<array[y+i,x]:
                    biggest=array[y+i,x]
                if x+i<width and biggest<array[y,x+i]:
                    biggest=array[y,x+i]
            new_row.append(biggest)
        new_array.append(new_row)
    return numpy.array(new_array)

def opening(array,kernel_size=1):
    return dilation(erosion(array,kernel_size),kernel_size)

def closing(array,kernel_size=1):
    return erosion(dilation(array,kernel_size),kernel_size)

def __apply_3x3_kernel(array,kernel):
    new_array=[]
    for y in range(1,len(array)-1):
        new_row=[]
        for x in range(1,len(array[0])-1):
            tmp=numpy.array(array[y-1:y+2,x-1:x+2])
            result=(tmp*kernel).sum()
            if result>255:
                result=255
            elif result<0:
                result=0
            new_row.append(result)
        new_array.append(new_row)
    return numpy.array(new_array)

def edge_detection(array):
    return __apply_3x3_kernel(array,numpy.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]))

def blur(array):
    return __apply_3x3_kernel(array,numpy.array([[0.0625,0.125,0.0625],[0.125,0.25,0.125],[0.0625,0.125,0.0625]]))

def sharpen(array):
    return __apply_3x3_kernel(array,numpy.array([[0,-1,0],[-1,5,-1],[0,-1,0]]))

def bottom_sobel(array):
    return __apply_3x3_kernel(array,numpy.array([[-1,-2,-1],[0,0,0],[1,2,1]]))

def top_sobel(array):
    return __apply_3x3_kernel(array,numpy.array([[1,2,1],[0,0,0],[-1,-2,-1]]))

def right_sobel(array):
    return __apply_3x3_kernel(array,numpy.array([[-1,0,1],[-2,0,2],[-1,0,1]]))

def left_sobel(array):
    return __apply_3x3_kernel(array,numpy.array([[1,0,-1],[2,0,-2],[1,0,-1]]))