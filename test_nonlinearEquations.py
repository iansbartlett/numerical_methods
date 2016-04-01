# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:04:41 2016

@author: iansbartlett
"""
import nonlinearEquations as nonlin

import numpy as np
import scipy as sp

def test_nonlinear_Equations(tol=1e-8, printFlag=False):
    
    test_bisection_methods(tol,printFlag)
    pass    


#Test single-function functions

def test_bisection(testFunctions, ranges,tol, printFlag):
    """
    Test my bisection method by comparing with the output of the scipy function.
    
    If printFlag is set to True, print both fuction outputs and the difference.
    
    Returns True if the difference is less than tol, False otherwise
    """
    
    for i in range(len(testFunctions)):
        scipyValue = sp.optimize.bisect(testFunctions[i],ranges[i,0],ranges[i,1])
        nonlinValue =
    pass

def test_fixed_point(testFunctions, tol, printFlag):
    """
    Test my fixed point method by comparing with the output of the scipy function.
    
    If printFlag is set to True, print both fuction outputs and the difference.
    
    Returns True if the difference is less than tol, False otherwise
    """    
    pass

def test_newton_rhapson(testFunctions, tol, printFlag):
    """
    Test my Newton-Rhapson method by comparing with the output of the scipy function.
    
    If printFlag is set to True, print both fuction outputs and the difference.
    
    Returns True if the difference is less than tol, False otherwise
    """    
    pass

def test_secant(testFunctions, tol, printFlag):
    """
    Test my secant method by comparing with the output of the scipy function.
    
    If printFlag is set to True, print both fuction outputs and the difference.
    
    Returns True if the difference is less than tol, False otherwise
    """    
    pass

#Test system functions


def test_bisection_system(testFunctions,tol, printFlag):
    """
    Test my bisection method by comparing with the output of the scipy function.
    
    If printFlag is set to True, print both fuction outputs and the difference.
    
    Returns True if the difference is less than tol, False otherwise
    """
    pass

def test_fixed_point_system(testFunctions, tol, printFlag):
    """
    Test my fixed point method by comparing with the output of the scipy function.
    
    If printFlag is set to True, print both fuction outputs and the difference.
    
    Returns True if the difference is less than tol, False otherwise
    """    
    pass

def test_newton_rhapson_system(testFunctions, tol, printFlag):
    """
    Test my Newton-Rhapson method by comparing with the output of the scipy function.
    
    If printFlag is set to True, print both fuction outputs and the difference.
    
    Returns True if the difference is less than tol, False otherwise
    """    
    pass

def test_secant_system(testFunctions, tol, printFlag):
    """
    Test my secant method by comparing with the output of the scipy function.
    
    If printFlag is set to True, print both fuction outputs and the difference.
    
    Returns True if the difference is less than tol, False otherwise
    """    
    pass
