#! /usr/bin/env python

from itaps import iBase,iMesh
import re
import sys

def reTagMesh( mesh):
    column=[]; count=0
    mats=mesh.getTagHandle("MATS")
    fracs=mesh.getTagHandle("FRACTIONS")
    matID=list(mats[mesh.rootSet])
    
    for num in matID :
        tag=mesh.createTag("mat_"+str(num),1,float)
        
        for i in fracs[mesh.getEntities(iBase.Type.region)] :
            column.append(i[count])    
        
        tag[mesh.getEntities(iBase.Type.region)]=column
        print "mat_"+str(num)+str(column)
        column=[]
        count=count+1
    return 
  
if __name__=='__main__':
     mesh = iMesh.Mesh()
     mesh.load( sys.argv[1] )
     reTagMesh(mesh)
     mesh.save('new_file.h5m')
