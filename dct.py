'''
Discete Cosine Transform
Author: Andrew Chalmers, 2014
    
This calculates the DCT at different frequencies in two dimensions. 
Some packages don't allow you to specify the specific basis (u,v), but
instead sum across the frequencies giving you the final result.

Useful applications for specifying a certain basis can be for educational
purposes (visualising the basis functions), or if you need to split the 
basises into a dictionary for learning.

I've left this unoptimised for clarity. 

Resources:
Image and video processing: From Mars to Hollywood with a stop at the hospital,
lecture 10. By Guillermo Sapiro from Duke University
'''

from math import cos,sqrt,pi
import numpy as n_
import pylab as p_
import matplotlib.cm as cm


def dct(x, y, v, u, n):
    # Normalisation
    def alpha(a):
        if a==0:
            return sqrt(1.0/n)
        else:
            return sqrt(2.0/n)
    
    return alpha(u)*alpha(v)*cos(((2*x+1)*(u*pi))/(2*n))*cos(((2*y+1)*(v*pi))/(2*n))
    
if __name__ == '__main__':
    print "Running DCT"
    n = 8 # Assume sqaure image, so we don't have different xres and yres
    
    # We can get different frequencies by setting u and v
    # Here, we have a max u and v to loop over and display
    # Feel free to adjust
    maxV = n 
    maxU = n
    
    imageSet = []
    for u in range(0, maxU):
        for v in range(0, maxV):
            basisImg = n_.zeros((n,n))
            for y in range(0, n):
                for x in range(0, n):    
                    basisImg[y,x] = dct(x, y, v, u, n)
            imageSet.append(basisImg)
    
    '''
    # Instead of looping, we can choose one basis(u,v)
    v = 0
    u = 0
    basisImg = n_.zeros((n,n))
    for y in range(0, n):
        for x in range(0, n):    
            basisImg[y,x] = dct(x, y, v, u, n)
    '''
    
    displayRows = maxV
    displayCols = maxU
    p_.figure("DCT")
    for i in range(0, len(imageSet)):
        p_.subplot(displayRows, displayCols, i+1)
        p_.axis('off')
        p_.imshow(imageSet[i],cmap = cm.Greys_r)
    p_.show()
    
    print "Complete" 
    
