#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:13:15 2017

@author: gracer
"""
import glob
import os
import subprocess
import pdb

basedir='/Users/gracer/Desktop/data'

for nifti in glob.glob(os.path.join(basedir,'sub*','func','sub-*_task-bart_bold.nii.gz')):
    output=nifti.strip('.nii.gz')
    if os.path.exists(output+'_brain.nii.gz'):
        print(output+' exists, skipping')
    else:
        BET_OUTPUT=output+'_brain'
#        x=("/usr/local/fsl/bin/bet %s %s -F"%(nifti, BET_OUTPUT))
#        pdb.set_trace()
        subprocess.call(['bet','%s'%nifti,'%s'%output,'-F'])
#        pdb.set_trace()
