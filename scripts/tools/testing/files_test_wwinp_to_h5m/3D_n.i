Test file generates WW in a box for easy wwinp_to_h5m.py testing
1 1 0.0005 -1 imp:n =1
999 0 1    imp:n = 0

1 rpp -100 100 -100  100 -100 100

m1 1001 1
nps 1E8
prdmp 1E7 1E7 1 0 1E7
mode:n
sdef
f5:n 0 0 90 5
wwg:n 5 0 0
mesh origin= -100 -100 -100 ref= 0 0 0
c
       imesh = -99 -97  97 99 100
       iints = 1   1  11  1  1
c
       jmesh =   -50 60 100
       jints =   1  7  1
c
       kmesh = 100
       kints = 7
wwge:n 1E-9 5ILOG 1E-3
