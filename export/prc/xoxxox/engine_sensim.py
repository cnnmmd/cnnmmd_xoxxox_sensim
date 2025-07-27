import re
from xoxxox.shared import Custom

#---------------------------------------------------------------------------

class SenPrc:

  def __init__(self, config="xoxxox/config_sensim_000", **dicprm):
    diccnf = Custom.update(config, dicprm)
    self.dicsen = {}

  def status(self, config="xoxxox/config_sensim_000", **dicprm):
    diccnf = Custom.update(config, dicprm)
    if self.dicsen != diccnf["dicsen"]:
      self.dicsen = diccnf["dicsen"]
      self.txtsen = diccnf["except"]

  def infere(self, txtreq):
    txtsen = self.txtsen
    for k in self.dicsen.keys():
      if re.search(self.dicsen[k], txtreq):
        txtsen = k
    return txtsen
