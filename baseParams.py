# Simulation defaults
# these defaults can be overrided via a custom python parameter file or via the commandline (in this order: commandline arguments take precedence over customParams.py, which take precendence over the defaults defined here)
params   =       {'durationH':         '04', # used by Sango
                  'durationMin':       '00', # used by Sango
                  'nbnodes':            '1', # used by K
                  'nestSeed':           20, # nest seed (affects input poisson spike trains)
                  'pythonSeed':         10, # python seed (affects connection map)
                  'nbcpu':                1,
                  'whichTest': 'testFullBG',
                  'nbCh':                 1,
                  'LG14modelID':          9,
                  'nbMSN':            2644.,
                  'nbFSI':              53.,
                  'nbSTN':               8.,
                  'nbGPe':              25.,
                  'nbGPi':              14.,
                  'nbCSN':            3000.,
                  'nbPTN':             100.,
                  'nbCMPf':              9.,
                  'GMSN':              4.37,
                  'GFSI':               1.3,
                  'GSTN':              1.38,
                  'GGPe':               1.3,
                  'GGPi':                1.,
                  'IeMSN':              0.,
                  'IeFSI':              0.,
                  'IeSTN':              0.,
                  'IeGPe':              13.,
                  'IeGPi':              11.,
                  'inDegCSNMSN':       100.,
                  'inDegPTNMSN':         1.,
                  'inDegCMPfMSN':        1.,
                  'inDegFSIMSN':        30., # 30 : according to Humphries et al. 2010, 30-150 FSIs->MSN
                  'inDegMSNMSN':        70., # 70 = 210/3 : according to Koos et al. 2004, cited by Humphries et al., 2010, on avg 3 synpase per MSN-MSN connection
                  'inDegSTNMSN':         0.,
                  'inDegGPeMSN':         0.,
                  'inDegCSNFSI':        50.,
                  'inDegPTNFSI':         1.,
                  'inDegSTNFSI':         2.,
                  'inDegGPeFSI':        25.,
                  'inDegCMPfFSI':        9.,
                  'inDegFSIFSI':        15., # 15 : according to Humphries et al., 2010, 13-63 FSIs->FSI
                  'inDegPTNSTN':        25.,
                  'inDegCMPfSTN':        9.,
                  'inDegGPeSTN':        25.,
                  'inDegCMPfGPe':        9.,
                  'inDegSTNGPe':         8.,
                  'inDegMSNGPe':      2644.,
                  'inDegGPeGPe':        25.,
                  'inDegMSNGPi':      2644.,
                  'inDegSTNGPi':         8.,
                  'inDegGPeGPi':        23.,
                  'inDegCMPfGPi':        9.,
                  'cTypeCSNMSN':  'focused', # defining connection types for channel-based models (focused or diffuse)
                  'cTypePTNMSN':  'focused',
                  'cTypeCMPfMSN': 'focused',
                  'cTypeFSIMSN':  'diffuse', 
                  'cTypeMSNMSN':  'focused', 
                  'cTypeSTNMSN':  'diffuse',
                  'cTypeGPeMSN':  'diffuse', # diffuse ? focused ?
                  'cTypeCSNFSI':  'focused',
                  'cTypePTNFSI':  'focused',
                  'cTypeSTNFSI':  'diffuse',
                  'cTypeGPeFSI':  'focused',
                  'cTypeCMPfFSI': 'focused',
                  'cTypeFSIFSI':  'diffuse', 
                  'cTypePTNSTN':  'focused',
                  'cTypeCMPfSTN': 'focused',
                  'cTypeGPeSTN':  'diffuse', # or diffuse, to be in line with the 2008 model?
                  'cTypeCMPfGPe': 'focused',
                  'cTypeSTNGPe':  'diffuse',
                  'cTypeMSNGPe':  'focused',
                  'cTypeGPeGPe':  'diffuse', # diffuse or focused?
                  'cTypeMSNGPi':  'focused',
                  'cTypeSTNGPi':  'diffuse',
                  'cTypeGPeGPi':  'diffuse',
                  'cTypeCMPfGPi': 'focused',
                  'parrotCMPf' :      False,
                  }

