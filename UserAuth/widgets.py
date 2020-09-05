import datetime
from django.forms.widgets import SelectDateWidget

class DynamicSelectDateWidget(SelectDateWidget):
    """
    return a dict of the year, month, and day, while removing invalid dates like February 31 and detecting leap years.
    """

    def format_value(self,value):
        year, month, day = None, None, None
        if isinstance(value,(datetime.date,datetime.datetime)):
            year, month, day = value.year, value.month, value.day

        elif isinstance(value,str):
            match = self.date_re.match(value)
            if match:
                year, month, day = [int(val) or '' for val in match.groups()]
            elif settings.USE_L10N:
                input_format = get_format('DATE_INPUT_FORMATS')[0]
                try:
                    d = datetime.datetime.strptime(value,input_format)
                except ValueError:
                    pass
                else:
                    year, month, day = d.year, d.month, d.day
        lower_months = ['april','june','september','november']
        if isinstance(value,(datetime.date,datetime.datetime)):
            if str(value.month).lower() in lower_months and value.day > 30:
                year, month, day = value.year, value.month, 30
            elif value.month in lower_months and value.day <= 30:
                year, month, day = value.year, value.month, value.day
            if value.year%4 == 0 and str(value.month).lower() == 'February':
                2