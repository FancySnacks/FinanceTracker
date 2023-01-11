from typing import NewType

DATE = NewType('date', str)


# Represents a single value entry that is either classified as 'expense' or 'income'
class TrackerEntry:

    def __init__(self, name: str, category, value: float):
        """
        :param string name = name of entry as typed by the user
        :param category = list of categories this entry is labelled by
        :param float value = positive number if it's an income | negative if it's an expense
        """

        self.name = name
        self.category = category
        self.value = value



# Holds all entries of a single type (income or expense)
# Also holds all entries of children objects (see DateEntry class)
class EntryContainer:
    def __init__(self):
        self.entries: list[TrackerEntry] = []

    def add_entry(self, item: TrackerEntry) -> list[TrackerEntry]:
        self.entries.append(item)
        return self.entries

    def get_total(self) -> float:
        return sum([entry.value for entry in self.entries])



# Represents a single date object (month, week, day) that contains income and expense related to that period
class DateEntry:
    def __init__(self, date: DATE, parent = None):
        '''
        :param date: string representation of a single date unit (day, week, month or year)
        :param parent: DateEntry object of higher order in terms of date
        '''

        self.date = date
        self.parent: DateEntry = parent

        # Contains all date units of lesser order
        # (ex. a 'year' Date Entry will have children of 'month' type Date Entries)
        self.children: list[DateEntry] = []

        # Contains entries of all children that belong to this object
        self.expenseList = EntryContainer()
        self.incomeList = EntryContainer()

    def get_total_expenses(self) -> float:
        return self.expenseList.get_total()

    def get_total_income(self) -> float:
        return self.incomeList.get_total()