
import re


class Decomposer(object):
	"""docstring for Decomposer"""
	defaultStrategy = "Ohm"
	def __init__(self, settings):
		super(Decomposer, self).__init__()
		self.settings = settings
		print ("Decomposer.__init__()")

		default =self.settings.get(self.settings.get('input', 'defaultMethod', fallback='test'), 'decomposer', fallback=self.defaultStrategy)
		self.setStrategy(default)

	def decompose(self, rawData):
		data = []
		for line in rawData:
			data.append(self.strategy(line))
		return data

	def getAvailableStrategies(self):
		return ["None", "PDM7", "Ohm"]

	def setStrategy(self, strategy):
		print ("Decomposer.setStrategy('"+strategy+"')")
		if strategy == "None":
			self.strategy = decomposeStrategyNone
		elif strategy == "PDM7":
			self.strategy = decomposeStrategyPDM7
		elif strategy == "Ohm":
			self.strategy = decomposeStrategyOhmStandard1
		else:
			print ("Decomposer.setStrategy ERROR: not found ('"+strategy+"')")

			return False
		return True










#strategies for decomposing
def decomposeStrategyNone(text):
	return [0, "None", text, "d"]

def decomposeStrategyPDM7(text):
	return [0, "None", text, "d"]

def decomposeStrategyOhmStandard1(text):
	splited = text.split()
	kind = "d"
	if splited[1][0] == "E":
		kind = "e"
	elif splited[1][0] == "W":
		kind = "w"
	return [0, splited[2], text, kind]