#!/user/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
def normalize(inputMatrix):
    #对当前矩阵按行做normalize
    output = dict()
    for eachA in inputMatrix:
        tmp_output = dict()
        tmp_eachB = inputMatrix[eachA]
        sum = 0
        for eachB1 in tmp_eachB:
            temp_num = tmp_eachB[eachB1]
            sum = sum + temp_num
        if sum != 0:
            for eachB2 in tmp_eachB:
                tmp_num = tmp_eachB[eachB2]/sum
                tmp_output[eachB2] = tmp_num
            output[eachA] = tmp_output
        else:
            output[eachA] = tmp_eachB
    return output