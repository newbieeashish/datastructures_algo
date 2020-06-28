'''Given a binary matrix A, we want to flip the image horizontally, 
then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is
reversed.  For example, flipping [1, 1, 0] horizontally 
 
results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and 
each 1 is replaced by 0. For example, inverting [0, 1, 1] results
in [1, 0, 0].'''

def flipAndInvertImage(imageA):

    for i in range(len(imageA)):
        imageA[i].reverse()
    
    for i in range(len(imageA)):
        for j in range(len(imageA[i])):
            if imageA[i][j] == 0:
                imageA[i][j] =1
            else:
                imageA[i][j] = 0
            
    return imageA


        





