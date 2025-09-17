import pandas as pd
import os
import math
import json
from typing import Union

class RHEA:
    def __init__(self) -> None:
        self.curPath = os.path.realpath(os.path.dirname(__file__))
        
    
    @staticmethod
    def getBV(lattice):
        return math.sqrt(3)*lattice/2
    
    def getLC(self, temperature: int):
        assert temperature in [0, 300, 1200], "Now only has the lattice constant at 0K, 300K and 1200K!"
        path = os.path.join(self.curPath, "LatticeConstant.xlsx")
        sheet_name = f"{str(temperature)}K"
        LC = pd.read_excel(path, sheet_name=sheet_name, index_col=[0])
        return LC
    
    def getWCP_20K(self):
        path = os.path.join(self.curPath, "WCP", "WCP_20K.json")
        f = open(path)
        WCP = json.load(f)
        f.close()
        return WCP
    
    def getWCP_1M(self):
        path = os.path.join(self.curPath, "WCP", "WCP_1M.json")
        f = open(path)
        WCP = json.load(f)
        f.close()
        return WCP
    
    def get_USFE(self):
        path = os.path.join(self.curPath, "energy.xlsx")
        USFE = pd.read_excel(path, sheet_name="USFE", index_col=[0])
        return USFE
    
    def get_DAPBE(self):
        path = os.path.join(self.curPath, "energy.xlsx")
        DAPBE = pd.read_excel(path, sheet_name="DAPBE", index_col=[0])
        return DAPBE

    def get_Elastic_300K_Random(self):
        path = os.path.join(self.curPath, "EC_300K.xlsx")
        EC = pd.read_excel(path, index_col=[0], sheet_name='random')
        return EC
    
    def get_Elastic_300K_20K(self):
        path = os.path.join(self.curPath, "EC_300K.xlsx")
        EC = pd.read_excel(path, index_col=[0], sheet_name='20K')
        return EC
    
    def get_Elastic_300K_1M(self):
        path = os.path.join(self.curPath, "EC_300K.xlsx")
        EC = pd.read_excel(path, index_col=[0], sheet_name='1M')
        return EC
    
    def get_DisVel(self, dis_type: str, alloy: str, temperature: int) -> pd:
        assert dis_type in ["edge", 'screw'], "only support two dislocation types: edge or screw !"
        path = os.path.join(self.curPath, "dislocation_velocity", dis_type, f"{str(temperature)}K", f"{alloy}.csv")
        data = pd.read_csv(path)
        return data

    def get_DisVel_Induvidual(self, dis_type: str, temperature: int, state: str) -> str:
        assert dis_type in ["edge", 'screw'], "only support two dislocation types: edge or screw !"
        assert state in ["random", "20K", "1M"], "only support three states: random, 20K, 1M !"
        path = os.path.join(self.curPath, "dislocation_velocity", dis_type, f"{str(temperature)}K", "seperate", state)
        return path

    def get_B2(self, state: str) -> pd:
        assert state in ["20K", "200K", "1M"], "only support three states: random, 20K, 1M !"
        path = os.path.join(self.curPath, "B2.xlsx")
        data = pd.read_excel(path, sheet_name=state)
        return data
    
    def get_LatticeDistortion(self, temperature: int) -> pd:
        path = os.path.join(self.curPath, "latticeDistortion", f"LD_{temperature}K.xlsx")
        data = pd.ExcelFile(path)
        return data