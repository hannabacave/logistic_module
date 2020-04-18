import time

start=time.time()
def animate(i):
    """Animated zoom on the mandelbrot set
    :param i: the number of time the functions is to be used
    :type i: integer

    :return: An image with a zoom on the Mandelbrot set
    :rtype: object 
    """
    #The programm passes this function multiples times: it goes from i=0 to a value of i that we are going to chose in the document script.py. For each value of i, we print a different matrice. As i increases, the interval for min values and max values (for x and y) becomes smaller, visuallly it is like if we were zooming on the first picture (obtained by printing Z)
    if i == 0:
        im = plt.imshow(Z_2)
    if i == 1:
        im = plt.imshow(Z_3)
    if i == 2:
        im = plt.imshow(Z_4)
    if i == 3:
        im = plt.imshow(Z_5)
    if i == 4:
        im = plt.imshow(Z_6)
    if i == 5:
        im = plt.imshow(Z_7)
    if i == 6:
        im = plt.imshow(Z_8)
    if i == 7:
        im = plt.imshow(Z_9)
    if i == 8:
        im = plt.imshow(Z_10)
    if i == 9:
        im = plt.imshow(Z_11)
    if i == 10:
        im = plt.imshow(Z_12)
    return im,
end=time.time()
print("Temps passé pour éxécuter la fonction:  {0:.5f} s.".format(end - start))


