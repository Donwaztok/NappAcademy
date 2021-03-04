from datetime import date, datetime

class MyCalendar:
	def __init__(self, *args) -> None:
		self.datas = []
		self.add_holiday(*args)

	def add_holiday(self, *args) -> None:
		for data in args:
			if isinstance(data, date):
				self.datas.append(data)
			elif isinstance(data, str):
				try:
					d = datetime.strptime(data, '%d/%m/%Y').date()
					self.datas.append(d)
				except:
					pass
		self.datas = list(set(self.datas))

	def check_holiday(self, data) -> bool:
		d = None
		if isinstance(data, date):
			d = data
		elif isinstance(data, str):
			try:
				d = datetime.strptime(data, '%d/%m/%Y').date()
			except:
				pass
		return d in self.datas
