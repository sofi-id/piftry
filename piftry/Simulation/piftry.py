
import sys
from os import environ
from os import getcwd
import string

sys.path.append(environ["PYTHON_MODULE_PATH"])


import CompuCellSetup


sim,simthread = CompuCellSetup.getCoreSimulationObjects()
        
# add extra attributes here
     
CompuCellSetup.initializeSimulationObjects(sim,simthread)
# Definitions of additional Python-managed fields go here
        
#Add Python steppables here
steppableRegistry=CompuCellSetup.getSteppableRegistry()
        
from piftrySteppables import NewSimulation3Steppable
steppableInstance=NewSimulation3Steppable(sim,_frequency=1)
steppableRegistry.registerSteppable(steppableInstance)

from piftrySteppables import NewSimulation4Steppable
steppableInstance=NewSimulation3Steppable(sim,_frequency=1)
steppableRegistry.registerSteppable(steppableInstance)

#from NewSimulation3Steppables import BuildWall3DSteppable
#steppableInstance=BuildWall3DSteppable(sim,_frequency=1)
#steppableRegistry.registerSteppable(steppableInstance)

#from NewSimulation3Steppables import ExtraMultiPlotSteppable
#extraMultiPlotSteppable=ExtraMultiPlotSteppable(_simulator=sim,_frequency=1)
#steppableRegistry.registerSteppable(extraMultiPlotSteppable)

#from pedallaceration9Steppables import ExtraPlotSteppable
#extraPlotSteppable=ExtraPlotSteppable(_simulator=sim,_frequency=1)
#steppableRegistry.registerSteppable(extraPlotSteppable)

#from NewSimulation3Steppables import MitosisSteppable
#mitosisSteppable=MitosisSteppable(sim,10)
#steppableRegistry.registerSteppable(mitosisSteppable)

CompuCellSetup.mainLoop(sim,simthread,steppableRegistry)   