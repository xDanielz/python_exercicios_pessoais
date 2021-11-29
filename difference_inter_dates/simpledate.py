from calendar import isleap


class SimpleDate:
    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day
        self._dd = {'year': year, 'month': month, 'day': day}
        self._dt = (year, month, day)

    def __getitem__(self, key):
        try:
            return self._dd[key]
        except KeyError:
            try:
                return self._dt[key]
            except IndexError:
                raise KeyError(key)

    def __sub__(self, other):
        return self.difference_inter_dates(other)

    @classmethod
    def fromdatetime(cls, objdate):
        day, month, year = objdate.day, objdate.month, objdate.year
        return cls(year, month, day)

    def difference_inter_dates(self, other) -> dict:
        difference = {}.fromkeys('years months weeks days total_days'.split(), 0)
        month_counter = [0]*12
        ffrom = min(self._dt, other._dt)
        to = max(self._dt, other._dt)
        year, month, day = ffrom
        while (year, month, day) != to:
            last_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if isleap(year):
                last_days[1] += 1
            difference['total_days'] += 1
            day += 1
            month_counter[month - 1] += 1
            if day == last_days[month-1] + 1:
                if month_counter[month - 1] + 1 != day:
                    difference['days'] += month_counter[month - 1]

                else:
                    difference['months'] += 1
                    if difference['months'] == 12:
                        difference['months'] = 0
                        difference['years'] += 1
                day = 1
                month += 1
                if month == 13:
                    month = 1
                    year += 1
                    month_counter = [0]*12
            if (year, month, day) == to:
                difference['days'] += month_counter[month - 1]
                for k, n in zip(['months', 'weeks'], (30, 7)):
                    if difference['days'] >= n:
                        x, y = divmod(difference['days'], n)
                        difference[k] += x
                        difference['days'] = y

        return difference
