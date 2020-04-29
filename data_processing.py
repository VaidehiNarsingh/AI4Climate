import pandas as pd

def parse_sampling_date_to_month(sampling_dates):

    month_dict = {'Jan': 1, "January:": 1, 'Feb': 2, "February": 2, "Mar": 3, "March": 3,
                  "Apr": 4, "April": 4, "May": 5, "Jun": 6, "June": 6, "Jul": 7, "July": 7,
                  "Aug": 8, "August": 8, "Sep": 9, "September": 9, "Oct": 10, "October": 10,
                  "Nov": 11, "Novemeber": 11, "Dec": 12, "December": 12}

    sampling_months = sampling_dates.copy()
    for i in range(sampling_months.shape[0]):
        date = str(sampling_dates[i])

        # parse dates in format 1-Jan-2019
        if len(date.split('-')) == 3:
            month = date.split('-')[1]
            if month in month_dict.keys():
                month = month_dict[month]
            else:
                month = None

        # parse dates in format 1-Jan
        elif len(date.split('-')) == 2:
            month = date.split('-')[1]
            if month in month_dict.keys():
                month = month_dict[month]
            else:
                month = None

        # parse dates in format 01/15/2019
        elif len(date.split('/')) == 3:
            month = date.split('/')[0]
            if (month in [str(x) for x in range(1, 13)]) or \
               (month in ['0'+str(x) for x in range(1, 13)]):
                month = int(month)

            #parse dates in format 15/01/2019
            else:
                month = date.split('/')[1].strip('_')
                if (month in [str(x) for x in range(1, 13)]) or \
                        (month in ['0' + str(x) for x in range(1, 13)]):
                    month = int(month)

        #parse dates in format August
        elif date.strip('-') in month_dict.keys():
            month = month_dict[date.strip()]
        else:
            month = None

        sampling_months[i] = month
    return sampling_months


if __name__ == "__main__":
    # load the data and parse the dates
    dataframe = pd.read_csv('data.csv')

    # replace NA with None
    dataframe = dataframe.replace('NA', None)

    # add a column with sampling months
    dataframe["Sampling_month"] = parse_sampling_date_to_month(dataframe["Sampling_date"])

    print(dataframe[:25])
