#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 18:29:33 2021

@author: alper
"""

import cv2

img = cv2.imread("squid.jpg")

# UMBRELLA
umbrella = cv2.imread("umbrella.jpg")
umbrellagray = cv2.cvtColor(umbrella, cv2.COLOR_BGR2GRAY)
h0, w0 = umbrellagray.shape

# CIRCLE
circle = cv2.imread("circle.jpg")
circlegray = cv2.cvtColor(circle, cv2.COLOR_BGR2GRAY)
h1, w1 = circlegray.shape

# TRIANGLE
triangle = cv2.imread("triangle.jpg")
trianglegray = cv2.cvtColor(triangle, cv2.COLOR_BGR2GRAY)
h2, w2 = trianglegray.shape

# STAR
star = cv2.imread("star.jpg")
stargray = cv2.cvtColor(star, cv2.COLOR_BGR2GRAY)
h3, w3 = stargray.shape

shapes = ['umbrella','circle','triangle','star']
dimensions = [['h0','w0'],['h1','w1'],['h2','w2'],['h3','w3']]
colors = ['(250,50,50)','(0,150,0)','(0,0,255)','(0,200,255)']

i = 0

while i < len(shapes):
    res = cv2.matchTemplate(img, eval(shapes[i]), cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + eval(dimensions[i][0]), top_left[1] + eval(dimensions[i][1]))
    
    cv2.rectangle(img, top_left, bottom_right, eval(colors[i]), 3)
    cv2.putText(img=img,text=shapes[i],org=(int(top_left[0]), int(top_left[1]) - 7), fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.7,color=eval(colors[i]),thickness=2)
    imgOriginal = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    cv2.imshow("Squid", imgOriginal)
    i = i + 1
    cv2.waitKey(3000)

k = cv2.waitKey()

if k == ord('q'):
    cv2.destroyAllWindows()