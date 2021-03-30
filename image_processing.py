import numpy

def grayscale(image):
    new_image=[]
    for rows in image:
        tmp=[]
        for pixel in rows:
            mean=0
            for color in pixel:
                mean+=color
            mean/=3
            tmp.append(mean)
        new_image.append(tmp)
    return numpy.array(new_image)

def bitmap(image,threshold):
    new_image=[]
    for rows in image:
        tmp=[]
        for pixel in rows:
            mean=0
            for color in pixel:
                mean+=color
            mean/=3
            tmp.append(255 if mean>threshold else 0)
        new_image.append(tmp)
    return numpy.array(new_image)

def increase_each_pixel(image,value):
    for y in range(len(image)):
        for x in range(len(image[0])):
            for z in range(len(image[0,0])):
                old=image[y,x,z]
                if value+old<256:
                    image[y,x,z]+=value
                else:
                    image[y,x,z]=255
    return image

def decrease_each_pixel(image,value):
    for y in range(len(image)):
        for x in range(len(image[0])):
            for z in range(len(image[0,0])):
                old=image[y,x,z]
                if old-value>-1:
                    image[y,x,z]-=value
                else:
                    image[y,x,z]=0
    return image

def mirror_horizontally(image):
    image_width=len(image[0])
    for y in range(len(image)):
        for x in range(int(image_width/2)):
            tmp=image[y,x].copy()
            image[y,x]=image[y,image_width-x-1]
            image[y,image_width-x-1]=tmp
    return image

def mirror_vertically(image):
    image_height=len(image)
    for y in range(int(image_height/2)):
        for x in range(len(image[0])):
            tmp=image[y,x].copy()
            image[y,x]=image[image_height-y-1,x]
            image[image_height-y-1,x]=tmp
    return image

def erosion(image,kernel_size=1):
    height=len(image)
    width=len(image[0])
    new_image=[]
    for y in range(height):
        new_row=[]
        for x in range(width):
            smallest=image[y,x]
            for i in range(1,kernel_size+1):
                if y-i>=0 and smallest>image[y-i,x]:
                    smallest=image[y-i,x]
                if x-i>=0 and smallest>image[y,x-i]:
                    smallest=image[y,x-i]
                if y+i<height and smallest>image[y+i,x]:
                    smallest=image[y+i,x]
                if x+i<width and smallest>image[y,x+i]:
                    smallest=image[y,x+i]
            new_row.append(smallest)
        new_image.append(new_row)
    return numpy.array(new_image)

def dilation(image,kernel_size=1):
    height=len(image)
    width=len(image[0])
    new_image=[]
    for y in range(height):
        new_row=[]
        for x in range(width):
            biggest=image[y,x]
            for i in range(1,kernel_size+1):
                if y-i>=0 and biggest<image[y-i,x]:
                    biggest=image[y-i,x]
                if x-i>=0 and biggest<image[y,x-i]:
                    biggest=image[y,x-i]
                if y+i<height and biggest<image[y+i,x]:
                    biggest=image[y+i,x]
                if x+i<width and biggest<image[y,x+i]:
                    biggest=image[y,x+i]
            new_row.append(biggest)
        new_image.append(new_row)
    return numpy.array(new_image)

def opening(image,kernel_size=1):
    return dilation(erosion(image,kernel_size),kernel_size)

def closing(image,kernel_size=1):
    return erosion(dilation(image,kernel_size),kernel_size)

def __apply_3x3_kernel(image,kernel):
    new_image=[]
    for y in range(1,len(image)-1):
        new_row=[]
        for x in range(1,len(image[0])-1):
            tmp=numpy.array(image[y-1:y+2,x-1:x+2])
            result=(tmp*kernel).sum()
            if result>255:
                result=255
            elif result<0:
                result=0
            new_row.append(result)
        new_image.append(new_row)
    return numpy.array(new_image)

def positive_laplace(image):
    return __apply_3x3_kernel(image,numpy.array([[0,1,0],[1,-4,1],[0,1,0]]))

def negative_laplace(image):
    return __apply_3x3_kernel(image,numpy.array([[0,-1,0],[-1,4,-1],[0,-1,0]]))

def edge_detection(image):
    return __apply_3x3_kernel(image,numpy.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]))

def blur(image):
    return __apply_3x3_kernel(image,numpy.array([[0.0625,0.125,0.0625],[0.125,0.25,0.125],[0.0625,0.125,0.0625]]))

def sharpen(image):
    return __apply_3x3_kernel(image,numpy.array([[0,-1,0],[-1,5,-1],[0,-1,0]]))

def bottom_sobel(image):
    return __apply_3x3_kernel(image,numpy.array([[-1,-2,-1],[0,0,0],[1,2,1]]))

def top_sobel(image):
    return __apply_3x3_kernel(image,numpy.array([[1,2,1],[0,0,0],[-1,-2,-1]]))

def right_sobel(image):
    return __apply_3x3_kernel(image,numpy.array([[-1,0,1],[-2,0,2],[-1,0,1]]))

def left_sobel(image):
    return __apply_3x3_kernel(image,numpy.array([[1,0,-1],[2,0,-2],[1,0,-1]]))

def identity(image):
    return __apply_3x3_kernel(image,numpy.array([[0,0,0],[0,1,0],[0,0,0]]))

def emboss(image):
    return __apply_3x3_kernel(image,numpy.array([[-2,-1,0],[-1,1,1],[0,1,2]]))