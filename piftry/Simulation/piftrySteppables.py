import CompuCell
import sys
from PlayerPython import *
from math import *
from random import random
from PySteppables import *
from PySteppablesExamples import MitosisSteppableBase

class NewSimulation4Steppable(SteppableBasePy):
    def start(self):
        x = X_POSITION
        y = Y_POSITION
        size = SIZE
        cell = self.newCell(self.S)
        self.cellField[x:x + size - 1, y:y + size - 1, 0] = cell  
        Size = 5
        x = (1,2,3)
        y = (5,6,7)
    def step(self,mcs):
        pass
    def finish(self):
        # Finish Function gets called after the last MCS
        pass
class NewSimulation3Steppable(SteppableBasePy):

    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def start(self):
        # any code in the start function runs before MCS=0
        pass
    def step(self,mcs):

        field=CompuCell.getConcentrationField(self.simulator,"Firstinhibitor")
        fielt=CompuCell.getConcentrationField(self.simulator,"Sactivator")
        fiell=CompuCell.getConcentrationField(self.simulator,"Secondinhibitor")
        comPt=CompuCell.Point3D()        
       # concentrationAI=field.get(comPt)
        #concentrationA=fielt.get(comPt) 
        for cell in self.cellList:
            if cell.type==self.UD or cell.type==self.G:
                if mcs > 0 and field[cell.xCOM,cell.yCOM,cell.zCOM]<0.5 and fiell[cell.xCOM,cell.yCOM,cell.zCOM]>0.5 and fielt[cell.xCOM,cell.yCOM,cell.zCOM]>20:
                    cell.type = self.OF
                if mcs > 0 and fiell[cell.xCOM,cell.yCOM,cell.zCOM]<0.5 and field[cell.xCOM,cell.yCOM,cell.zCOM]>0.5 and fielt[cell.xCOM,cell.yCOM,cell.zCOM]>20:
                    cell.type = self.OS
                    
                if mcs > 0 and fiell[cell.xCOM,cell.yCOM,cell.zCOM]<0.5 and field[cell.xCOM,cell.yCOM,cell.zCOM]<0.5 and fielt[cell.xCOM,cell.yCOM,cell.zCOM]>20:
                    if random()<0.5:
                        cell.type = self.OS
                    else:
                        cell.type = self.OF
        #concentration=field[int(round(cell.xCOM)),int(round(cell.yCOM)),int(round(cell.zCOM))]
        #type here the code that will run every _frequency MCS
        for cell in self.cellList:
            currentCellPosition = cell.xCM/float(cell.volume)
            currentCellPositiony = cell.yCM/float(cell.volume)
            firstinhi = field[cell.xCOM,cell.yCOM,cell.zCOM] 
            secondinhi = fiell[cell.xCOM,cell.yCOM,cell.zCOM] 
            sactivator = fielt[cell.xCOM,cell.yCOM,cell.zCOM] 
            print( "id=", cell.id, "posx= ",currentCellPosition, "posy= ",currentCellPositiony,"Fi= ", firstinhi, "Si= ", secondinhi, "Sac= ", sactivator)

    def finish(self):
        # Finish Function gets called after the last MCS
        pass
                


 
#class ExtraMultiPlotSteppable(SteppableBasePy):
 #   def __init__(self, _simulator, _frequency=1):
  #      SteppableBasePy.__init__(self, _simulator, _frequency)

   # def start(self):
    #    _config_options_1 = {'background': 'white111', 'legend': False}
     #   _config_options_2 = {'background': 'green', 'legend': False}

      #  self.Aactcon = self.addNewPlotWindow(_title='A-Activator concentration in time', _xAxisTitle='MonteCarlo Step (MCS)',
       #                                    _yAxisTitle='Concentration', _config_options=_config_options_1)
    #    self.Bactcon = self.addNewPlotWindow(_title='B-Activator concentration in time', _xAxisTitle='MonteCarlo Step (MCS)',
     #                                      _yAxisTitle='Concentration', _config_options=_config_options_2)                                   
  #      self.Aactcon.addPlot(_plotName='Aactcon')
    #    self.Bactcon.addPlot(_plotName='Bactcon')
  #      self.Ainhcon = self.addNewPlotWindow(_title='A-Inhibitor concentration in time', _xAxisTitle='MonteCarlo Step (MCS)',
   #                                        _yAxisTitle='Concentration', _config_options=_config_options_1)        
    #    self.Ainhcon.addPlot(_plotName='Ainhcon', _style='Dots', _color='red', _size=5)
     #   self.Binhcon = self.addNewPlotWindow(_title='B-Inhibitor concentration in time', _xAxisTitle='MonteCarlo Step (MCS)',
      #                                     _yAxisTitle='Concentration', _config_options=_config_options_1)        
       # self.Binhcon.addPlot(_plotName='Binhcon', _style='Dots', _color='red', _size=5)

  #  def step(self, mcs):
   #     field=CompuCell.getConcentrationField(self.simulator,"activator")
    #    comPt=CompuCell.Point3D()
     #   meanConA = 0.0
      #  meanConB = 0.0
        
  #      for cell in self.cellList:
   #         if cell.type==self.ACHECK: #Condensing cell
    #            comPt.x=int(round(cell.xCOM))
     #           comPt.y=int(round(cell.yCOM))
      #          comPt.z=int(round(cell.zCOM))


       #         concentrationA=field.get(comPt) 
        #        meanConA += concentrationA
                
                # get concentration at comPt
            
     #       self.Aactcon.addDataPoint("Aactcon", mcs, meanConA)
              
      #      if cell.type==self.BCHECK: #Condensing cell
        #        comPt.x=int(round(cell.xCOM))
       #         comPt.y=int(round(cell.yCOM))
         #       comPt.z=int(round(cell.zCOM))


      #          concentrationB=field.get(comPt) 
       #         meanConB += concentrationB 
                
                # get concentration at comPt
            
       #     self.Bactcon.addDataPoint("Bactcon", mcs, meanConB)

class ExtraPlotSteppable(SteppableBasePy):

    def start(self):
        _config_options_1 = {'background': 'white111', 'legend': False}
     #   _config_options_2 = {'background': 'green', 'legend': False}


        self.Activator = self.addNewPlotWindow(_title='Activator concentration', _xAxisTitle='montecarlostep',
                                           _yAxisTitle='Concentration', _config_options=_config_options_1)        
     #   self.Binhcon = self.addNewPlotWindow(_title='B-Inhibitor concentration in time', _xAxisTitle='MonteCarlo Step (MCS)',
      #                                     _yAxisTitle='Concentration', _config_options=_config_options_2)              
        self.Activator.addPlot(_plotName='Activator')
       # self.Binhcon.addPlot(_plotName='Binhcon')
       # Live plot for cell position
    #    self.pW1 = self.addNewPlotWindow(\_title = 'Location',\_xAxisTitle = 'MCS', _yAxisTitle = 'Cell position', \_xScaleType = 'linear', _yScaleType = 'linear' \)
     #   self.pW1.addPlot('Cell_id_11', _style='Dots', _color='red', _size=2)

# Live plot for integrin expression
#self.pW2 = self.addNewPlotWindow(\_title = 'Integrin',\_xAxisTitle = 'MCS', _yAxisTitle = 'Integrin density', \_xScaleType = 'linear', _yScaleType = 'linear' \)
#self.pW2.addPlot('Cell_id_810', _style='Dots', _color='green', _size=1) 

    def step(self, mcs):
        field=CompuCell.getConcentrationField(self.simulator,"Sactivator")
        comPt=CompuCell.Point3D()
        meanCon = 0.0
        
        for cell in self.cellList:
            if cell.id==1:
                comPt.x=int(round(cell.xCOM))
                comPt.y=int(round(cell.yCOM))
                comPt.z=int(round(cell.zCOM))


                con=field.get(comPt) 
                meanCon += con
            
            
                # get concentration at comPt
            
        self.Activator.addDataPoint("Activator", mcs, meanCon)
              
   #         if cell.type==self.BCHECK: #Condensing cell
    #            comPt.x=int(round(cell.xCOM))
     #           comPt.y=int(round(cell.yCOM))
      #          comPt.z=int(round(cell.zCOM))


       #         concentrationBI=field.get(comPt) 
        #        meanConBI += concentrationBI 
                
                # get concentration at comPt
            
         #   self.Binhcon.addDataPoint("Binhcon", mcs, meanConBI)

