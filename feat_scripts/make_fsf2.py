#!/usr/bin/env python

import os
import glob
import argparse
#import pdb


repl_dict={}
basedir='/Users/gracer/Desktop/data'
indir=os.path.join(basedir,'derivatives','task')
    
for dir in glob.glob(os.path.join(indir,'sub-*','grace_edit')):
    feats=glob.glob(os.path.join(dir,'%s*.feat'%(<NAMEOFTHEDIR>)))
    repl_dict.update({'SECOND':feats[1]})
    repl_dict.update({'FUNCRUN':feats[0]})
    sub=dir.split('/')[7]
    repl_dict.update({'SUB':sub})
    output=os.path.join(dir,'%s.gfeat'%(<NAMEOFTHEFOLDER>))
    repl_dict.update({'OUTPUT':output})
    print(repl_dict)
    with open(os.path.join(basedir,'design2.fsf'),'r') as infile:
        tempfsf=infile.read()
        for key in repl_dict:
            tempfsf = tempfsf.replace(key, repl_dict[key])
            with open(os.path.join(dir,'%s_second.fsf'%(<NAMEOFFILE>),'w') as outfile:
                outfile.write(tempfsf)
            outfile.close()
        infile.close()      


os.chdir('/Users/gracer/Google Drive/fMRI_workshop/scripts/feat_scripts')