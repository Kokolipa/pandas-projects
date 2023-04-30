#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:31:24 2023

@author: galbeeir
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np 

data = pd.read_csv('/Users/galbeeir/Desktop/Courses/CodeAcademy/Viaualisations/Power Bi - Transactions All .csv')

data.head()

%matplotlib inline

x = [1, 2, 3, 4]
y = [7 ,2, 5, 3]

plt.plot(x, y, color='green', label='line', linestyle='dashed')
plt.tick_params(axis = 'x', color='red', direction='out', labelsize='large',labelcolor='b',labelrotation=20 )
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Title')
plt.legend(bbox_to_anchor = (1, 1))
plt.show()

plt.savefig('my_line.png', dpi=120, bbox_inches='tight')