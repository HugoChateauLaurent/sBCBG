from LGneurons import *
import nest.raster_plot
import time

# params possible keys:
# - nb{MSN,FSI,STN,GPi,GPe,CSN,PTN,CMPf} : number of simulated neurons for each population
# - Ie{GPe,GPi} : constant input current to GPe and GPi
# - G{MSN,FSI,STN,GPi,GPe} : gain to be applied on LG14 input synaptic weights for each population

def main(showRasters=True,params={}):

  simDuration = 3000. # ms
  # nest.SetKernelStatus({"overwrite_files":True}) # Thanks to use of timestamps, file names should now 
                                                   #be different as long as they are not created during the same second

  #==========================
  # Creation of neurons
  #-------------------------
  print '\nCreating neurons\n================'

  nbSim['MSN'] = params['nbMSN'] if ('nbMSN' in params) else 2644.
  create('MSN')

  nbSim['FSI'] = params['nbFSI'] if ('nbFSI' in params) else 53.
  create('FSI')

  nbSim['STN'] = params['nbSTN'] if ('nbSTN' in params) else 8.
  create('STN')

  nbSim['GPe'] = params['nbGPe'] if ('nbGPe' in params) else 25.
  create('GPe')
  nest.SetStatus(Pop['GPe'],{"I_e":params['IeGPe'] if ('IeGPe' in params) else 13.})

  nbSim['GPi'] = params['nbGPi'] if ('nbGPi' in params) else 14.
  create('GPi')
  nest.SetStatus(Pop['GPi'],{"I_e":params['IeGPi'] if ('IeGPi' in params) else 9.})
  
  nbSim['CSN'] = params['nbCSN'] if ('nbCSN' in params) else 3000
  create('CSN', fake=True)
  
  nbSim['PTN'] = params['nbPTN'] if ('nbPTN' in params) else 100.
  create('PTN', fake=True)

  nbSim['CMPf'] = params['nbCMPf'] if ('nbCMPf' in params) else 9.
  create('CMPf', fake=True)

  print "Number of simulated neurons:", nbSim

  G = {'MSN': params['GMSN'] if ('GMSN' in params) else 3.9, # 3.9
       'FSI': params['GFSI'] if ('GFSI' in params) else 1.1,
       'STN': params['GSTN'] if ('GSTN' in params) else 1.35,
       'GPe': params['GGPe'] if ('GGPe' in params) else 1.3,
       'GPi': params['GGPi'] if ('GGPi' in params) else 1.3,
      }

  print "Gains on LG14 syn. strength:", G

  #-------------------------
  # connection of populations
  #-------------------------
  print '\nConnecting neurons\n================'
  print '* MSN Inputs'
  connect('ex','CSN','MSN', inDegree=100,gain=G['MSN'])
  connect('ex','PTN','MSN', inDegree=1,gain=G['MSN'])
  connect('ex','CMPf','MSN',inDegree=1,gain=G['MSN'])
  connect('in','FSI','MSN', inDegree=1,gain=G['MSN'])

  #connect('ex','CSN','MSN', inDegree=100,gain=G['MSN'])
  #connect('ex','PTN','MSN', inDegree=1,gain=G['MSN'])
  #connect('ex','CMPf','MSN',inDegree=nbSim['CMPf'],gain=G['MSN'])
  #connect('in','FSI','MSN', inDegree=nbSim['FSI'],gain=G['MSN'])

  print '* FSI Inputs'
  connect('ex','CSN','FSI', inDegree=50,gain=G['FSI'])
  connect('ex','PTN','FSI', inDegree=1,gain=G['FSI'])
  #connect('ex','STN','FSI', inDegree=nbSim['STN'],gain=G['FSI'])
  connect('ex','STN','FSI', inDegree=2,gain=G['FSI'])
  connect('in','GPe','FSI', inDegree=nbSim['GPe'],gain=G['FSI'])
  connect('ex','CMPf','FSI',inDegree=nbSim['CMPf'],gain=G['FSI'])

  print '* STN Inputs'
  connect('ex','PTN','STN', inDegree=min(25,nbSim['PTN']), gain=G['STN'])
  connect('ex','CMPf','STN',inDegree=min(84,nbSim['CMPf']), gain=G['STN'])
  connect('in','GPe','STN', inDegree=min(30,nbSim['GPe']), gain=G['STN'])

  print '* GPe Inputs'
  connect('ex','CMPf','GPe',inDegree=min(32/2,nbSim['CMPf']), gain=G['GPe'])
  connect('ex','STN','GPe', inDegree=min(107/2,nbSim['STN']), gain=G['GPe'])
  connect('in','MSN','GPe', inDegree=min(14723/2,nbSim['MSN']), gain=G['GPe'])
  connect('in','GPe','GPe', inDegree=min(32,nbSim['GPe']), gain=G['GPe'])

  print '* GPi Inputs'
  connect('in','MSN','GPi', inDegree=min(14723/2,nbSim['MSN']),gain=G['GPi'])
  connect('ex','STN','GPi', inDegree=min(107/2,nbSim['STN']),gain=G['GPi'])
  connect('in','GPe','GPi', inDegree=nbSim['GPe'],gain=G['GPi'])
  connect('ex','CMPf','GPi',inDegree=min(30,nbSim['CMPf']),gain=G['GPi'])

  #-------------------------
  # measures
  #-------------------------

  spkDetect={}
  expeRate={}

  execTime = time.localtime()
  timeStr = str(execTime[0])+'_'+str(execTime[1])+'_'+str(execTime[2])+'_'+str(execTime[3])+':'+str(execTime[4])+':'+str(execTime[5])

  for N in NUCLEI:
    spkDetect[N] = nest.Create("spike_detector", params={"withgid": True, "withtime": True, "label": timeStr+'_'+N, "to_file": True})
    nest.Connect(Pop[N], spkDetect[N])

  #-------------------------
  # Simulation
  #-------------------------
  #nest.ResetKernel()
  nest.Simulate(simDuration)

  for N in NUCLEI:  
    # print '\n Spike Detector n_events',nest.GetStatus(spkDetect, 'n_events')[0]
    expeRate[N] = nest.GetStatus(spkDetect[N], 'n_events')[0] / float(nbSim[N]*simDuration)
    print '\n*',N,'- Rate:',expeRate[N]*1000,'Hz'

  #-------------------------
  # Displays
  #-------------------------
  '''
  dSD = nest.GetStatus(spkDetect,keys="events")[0]
  evs = dSD["senders"]
  ts = dSD["times"]
  
  pylab.figure(testedNucleus+' spikes')
  pylab.plot(ts, evs, ".")

  pylab.show()
  '''
  if (showRasters):
    for N in NUCLEI:
      nest.raster_plot.from_device(spkDetect[N],hist=True,title=N)

    nest.raster_plot.show()

#---------------------------
if __name__ == '__main__':
  params = {'GMSN':3.8}
  main(showRasters=False,params=params)