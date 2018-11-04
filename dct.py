'''
Discrete Cosine Transform
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
https://www.youtube.com/watch?v=pZuaOjfsv0Y&list=PLZ9qNFMHZ-A79y1StvUUqgyL-O0fZh2rs&index=10
https://www.youtube.com/watch?v=_bltj_7Ne2c&list=PLZ9qNFMHZ-A79y1StvUUqgyL-O0fZh2rs&index=11
'''

import sys
from math import cos,sqrt,pi
import numpy as n_
import pylab as p_
import matplotlib.cm as cm

def dct(x, y, u, v, n):
    # Normalisation
    def alpha(a):
        if a==0:
            return sqrt(1.0/n)
        else:
            return sqrt(2.0/n)
    return alpha(u) * alpha(v) * cos(((2*x+1)*(u*pi))/(2*n)) * cos(((2*y+1)*(v*pi))/(2*n))

def getBasisImage(u, v, n):
    # for a given (u,v), make a DCT basis image
    basisImg = n_.zeros((n,n))
    for y in range(0, n):
        for x in range(0, n):
            basisImg[y,x] = dct(x, y, u, v, n)
    return basisImg

if __name__ == '__main__':
    print("Running DCT")

    # n (int): assume square image, so we don't have different xres and yres
    try:
        n = int(sys.argv[1])
    except:
        n = 8
    print("n: %d" % n)

    # We can get different frequencies by setting u and v
    print("Generating DCT basis images")
    imageSet = []
    for u in range(0, n):
        for v in range(0, n):
            basisImg = getBasisImage(u, v, n)
            imageSet.append(basisImg)

    print("Saving figure...")
    p_.figure("DCT")
    for i in range(0, len(imageSet)):
        p_.subplot(n, n, i+1)
        p_.axis('off')
        p_.imshow(imageSet[i],cmap = cm.Greys_r)
    p_.savefig('_dct_'+str(n)+'x'+str(n)+'_'+str(n)+'x'+str(n)+'.png')
    p_.show()

    print("Complete" )
    
