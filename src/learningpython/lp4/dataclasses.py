from dataclasses import dataclass,field
import datetime
from datetime import datetime as LocalDateTime

@dataclass(order=True)
class Person:
	"""A person with a first and last name."""
	first_name: str
	last_name: str

	def get_full_name(self) -> str:
		"""Returns the full name of the person."""
		return " ".join([self.first_name, self.last_name])
	
	def get_full_name_via_str_join(self) -> str:
		return str.join(" ", [self.first_name, self.last_name])
	
@dataclass(frozen=True)
class ImmutablePerson:
	"""An immutable person with a first and last name."""
	first_name: str
	last_name: str

	def get_full_name(self) -> str:
		"""Returns the full name of the person."""
		return f"{self.first_name} {self.last_name}"

@dataclass
class ComparablePerson:
	"""A person with comparison methods based on their names."""
	first_name: str
	last_name: str
	dob: datetime.date  # date of birth 

	def get_full_name(self) -> str:
		"""Returns the full name of the person."""
		return f"{self.first_name} {self.last_name}"
	
	def __lt__(self, other: 'ComparablePerson') -> bool:
		if self.last_name == other.last_name:
			if self.first_name == other.first_name:
				return self.dob < other.dob
			return self.first_name < other.first_name
		return self.last_name < other.last_name
	
	def __eq__(self, other: object) -> bool:
		if not isinstance(other, ComparablePerson):
			return NotImplemented
		return (self.first_name == other.first_name and
				self.last_name == other.last_name and
				self.dob == other.dob)
	
	def __le__(self, other: 'ComparablePerson') -> bool:
		return self < other or self == other
	
	def __gt__(self, other: 'ComparablePerson') -> bool:
		return not (self <= other)
	
	def __ge__(self, other: 'ComparablePerson') -> bool:
		return not (self < other)
	
	def __ne__(self, other: object) -> bool:
		if not isinstance(other, ComparablePerson):
			return NotImplemented
		return not self == other
	
@dataclass(kw_only=True)
class KeywordOnlyPerson:
	first_name: str
	last_name: str

	def get_full_name(self) -> str:
		return f"{self.first_name} {self.last_name}"

@dataclass(slots=True)
class SlottedPerson:
	first_name: str
	last_name: str

	def get_full_name(self) -> str:
		return f"{self.first_name} {self.last_name}"
	
@dataclass
class LogEntry:
	message: str
	datetime: LocalDateTime = field(default_factory=LocalDateTime.now)

@dataclass
class Guess:
	prediction: str
	actual: str = field(init=False)

@dataclass
class ComparableLogEntry:
	message: str
	datetime: LocalDateTime = field(default_factory=LocalDateTime.now, compare=False)
