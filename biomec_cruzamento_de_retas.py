# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 00:22:28 2023

@author: Victor Hugo Zani
"""
def calcular_coef_ang(xc,yc,xp,yp):
    mr=(yp-yc)/(xp-xc)
    return(mr)

def calcular_pos_x(xc_1,yc_1,xc_2,yc_2,mr_1,mr_2):
    return ((-(mr_2*xc_2)+yc_2+(mr_1*xc_1)-yc_1)/(mr_1-mr_2))

def calcular_pos_y(mr_1,x,xc_1,yc_1):
    return ((mr_1*x) -(mr_1*xc_1)+yc_1)
    

xc1=float(input("Entre com as cordenas em x da camera 1: "))
yc1=float(input("Entre com as cordenas em y da camera 1: "))
xc2=float(input("Entre com as cordenas em x da camera 2: "))
yc2=float(input("Entre com as cordenas em y da camera 2: "))
xp1=float(input("Entre com as cordenas em x da projeção 1: "))
yp1=float(input("Entre com as cordenas em y da projeção 1: "))
xp2=float(input("Entre com as cordenas em x da projeção 2: "))
yp2=float(input("Entre com as cordenas em y da projeção 2: "))
mr1= calcular_coef_ang(xc1, yc1, xp1, yp1)
mr2= calcular_coef_ang(xc2, yc2, xp2, yp2)
X=calcular_pos_x(xc1, yc1, xc2, yc2, mr1, mr2)
Y=calcular_pos_y(mr1, X, xc1, yc1)
