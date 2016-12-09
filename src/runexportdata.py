"""
runexportdata.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 09/12/2016
"""

from export import exportdata
from lib import com_config

conf = com_config.Config()
conf.setconfig()

exp = exportdata.ExportData()
exp.export()


