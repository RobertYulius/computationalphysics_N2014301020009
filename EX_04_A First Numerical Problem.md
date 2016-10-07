Exercise_03 : A First Numerical Problem
-



### Abstract
---
Use `Python` to solve a simple numerical problem: `Radioactive Decay`.


### Background
---
#### Radioactive Decay
 - A large number of nuclei:
 <br/><img src="http://latex.codecogs.com/gif.latex?\frac{dN}{dt}=-\frac{N}{\tau}" alt="" title="" /><br/>
 - The Taylor expansion for <img src="http://latex.codecogs.com/gif.latex?N%28t%29"" title="" />:
<br/>![](http://latex.codecogs.com/gif.latex?N%28%5CDelta%20t%29%3DN%280%29&plus;%5Cfrac%7BdN%7D%7Bdt%7D%5Ccdot%5CDelta%20t&plus;%5Cfrac%7B1%7D%7B2%7D%5Ccdot%5Cfrac%7Bd%5E2N%7D%7Bdt%5E2%7D&plus;...) <br/>
  Ignore the terms that involve second and higher powers of  <img src="http://latex.codecogs.com/gif.latex?%5CDelta%20t" alt="" title="" />:
  <br/>![](http://latex.codecogs.com/gif.latex?N%28%5CDelta%20t%29%5Capprox%20N%280%29&plus;%5Cfrac%7BdN%7D%7Bdt%7D%5Ccdot%5CDelta%20t) <br/>
 - Than
 <br/> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN%7D%7Bdt%7D%3D%5Clim_%7B%5CDelta%20t%5Crightarrow%200%7D%5Cfrac%7BN%28t&plus;%5CDelta%20t%29-N%28t%29%7D%7B%5CDelta%20t%7D%5Capprox%20%5Cfrac%7BN%28t&plus;%5CDelta%20t%29-N%28t%29%7D%7B%5CDelta%20t%7D) <br/>
 ![](http://latex.codecogs.com/gif.latex?N%28t&plus;%5CDelta%20t%29%5Capprox%20N%28t%29&plus;%5Cfrac%7BdN%7D%7Bdt%7D%5Ccdot%5CDelta%20t) <br/>
 - So
 <br/>![](http://latex.codecogs.com/gif.latex?N%28t&plus;%5CDelta%20t%29%5Capprox%20N%28t%29-%5Cfrac%7BN%28t%29%7D%7B%5Ctau%7D%5Ccdot%5CDelta%20t) 
 
####A Decay Problem with two types of nuclei
 - Two types of nuclei A and B. 
 - Now nuclei of type A decay into ones of type B, while nuclei of type B decay into ones of type A.
 - The corresponding rate equations are <br/>
<img src="http://latex.codecogs.com/gif.latex?\frac{dN_A}{dt}=\frac{N_B}{\tau}-\frac{N_A}{\tau}" alt="" title="" /> <br/>
<img src="http://latex.codecogs.com/gif.latex?\frac{dN_B}{dt}=\frac{N_A}{\tau}-\frac{N_B}{\tau}" alt="" title="" />  <br/>

 - For simplicity we have assumed that the two types of decay are characterized by the same time constant, τ.
 - Solve this system of equations for the numbers of nuclei,NA=100, NB=0, etc., and take τ=1s. 
 - Show that your numercial results are consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt should vanish.
 
### Problem Solving
--- 
 - The Taylor expansion for N:
 <br/>![](http://latex.codecogs.com/gif.latex?N%28%5CDelta%20t%29%5Capprox%20N%280%29&plus;%5Cfrac%7BdN%7D%7Bdt%7D%5Ccdot%5CDelta%20t) <br/>
 
 - Put <img src="http://latex.codecogs.com/gif.latex?\frac{dN_A}{dt}" alt="" title="" /> and <img src="http://latex.codecogs.com/gif.latex?\frac{dN_B}{dt}" alt="" title="" /> in it:
<br/> <img src="http://latex.codecogs.com/gif.latex?N_A%28%5CDelta%20t%29%5Capprox%20N%280%29&plus;%28\frac{N_B}{\tau}-\frac{N_A}{\tau}%29%5CDelta%20t" alt="" title="" /> <br/>
<br/> <img src="http://latex.codecogs.com/gif.latex?N_B%28%5CDelta%20t%29%5Capprox%20N%280%29&plus;%28\frac{N_A}{\tau}-\frac{N_B}{\tau}%29%5CDelta%20t" alt="" title="" /> <br/>




###Codes
---
```Python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pylab as pl
import time, os

class EX_1_5(object):

    def __init__(self, number_of_a = 100, number_of_b = 0, time_constant = 1, time_of_duration = 5, time_step = 0.05):
        # Unit of time is sec
        self.t = [0,]
        self.na = [number_of_a]
        self.nb = [number_of_b]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.stp =  int(time_of_duration // time_step +1)
        print("Initial number of A ->", number_of_a)
        print("Initial number of B ->", number_of_b)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)

    def calc(self):
        for i in range(self.stp):
            tmp_a = self.na[i] +(self.nb[i] - self.na[i]) / self.tau *self.dt
            tmp_b = self.nb[i] + (self.na[i] - self.nb[i]) / self.tau * self.dt
            self.t.append(round((self.t[i] + self.dt),2))
            self.na.append(tmp_a)
            self.nb.append(tmp_b)

    def show_results(self):
        pl.plot(self.t, self.na, color = "red", linewidth = 2.5, linestyle = "-", label = "Number of A")
        pl.plot(self.t, self.nb, color = "blue", linewidth = 2.5, linestyle = "-", label = "Number of B")
        pl.xlabel('Time ($s$)')
        pl.ylabel('Number of nuclei')
        pl.show()


    def store_results(self):

        if os.name == 'nt':
            myfile = open(r'D:\nuclei_decay_data.txt', 'a', encoding='utf - 8')
        elif os.name == 'posix':
            myfile = open('nuclei_decay_data.txt', 'a', encoding='utf-8')
        print('Calculation at:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), file = myfile)
        print('Time\tNA\t\tNB', file= myfile)

        for i in range(len(self.t)):
            print('%.2f\t%.2f\t%.2f' %(self.t[i], self.na[i], self.nb[i]), file = myfile)
        myfile.write('----------------------------------- End ---------------------------------------\n')
        myfile.close()
        print('Results saved.')

# eg1 = EX_1_5()
# eg1.calc()
# eg1.show_results()

eg2 = EX_1_5(number_of_a = 0, number_of_b = 100, time_constant = 1, time_of_duration = 5, time_step = 0.05)
eg2.calc()

eg2.show_results()
eg2.store_results()

```


###Acknowledgements!

- http://stackoverflow.com/questions/13207450/permissionerror-errno-13-in-python

- http://www.cnblogs.com/allenblogs/archive/2010/09/13/1824842.htm

> Written with [StackEdit](https://stackedit.io/).
