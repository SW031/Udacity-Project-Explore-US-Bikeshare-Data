import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nFirst select a city you are interested in: "+
                     "Chicago, New York City or Washington?\n\n")
        city = city.lower()
        
        # invalid input handling for city
        if city not in ('new york city', 'chicago', 'washington'):
            print("Please enter a valid city.")
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\n\nWhich month would you like to analyze for " + city.title() + 
                      "? You can choose between January, February, March, " +
                      "April, May and June, or type all if you do not wish "+
                      "to specify a month.\n\n")
        month = month.lower()
        
        # invalid input handling for month
        if month not in ('january', 'february', 'march', 'april', 'may', 
                         'june', 'all'):
            print("Please enter a valid month.")
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n\nWhich day would you like to choose?" +
                    "You can choose between Monday, Tuesday, Wednesday," +
                    "Thursday, Friday, Saturday or Sunday, or type all if " +
                    "you do not wish to specify a day.\n\n")
        day = day.lower()
        
        # invalid input handling for month
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                       'saturday', 'sunday', 'all'):
            print("Please enter a valid day.")
            continue
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # read the dataframe of the selected city, using the pandas package
    df = pd.read_csv(CITY_DATA[city])
    
    # convert Start Time to a datetime object, for subsequent extraction of
    # month and weekday (and later, hour)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extraction of month and day
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    
    # filtering of dataset, based on selections
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]
    
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df, city, day, month):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_name = df['Month'].mode()[0]
    # Change number to months
    if month_name == 1:
        month_name = "January"
    elif month_name == 2:
        month_name = "February"
    elif month_name == 3:
        month_name = "March"
    elif month_name == 4:
        month_name = "April"
    elif month_name == 5:
        month_name = "May"
    elif month_name == 6:
        month_name = "June"
    print('The most common month in',city.title(),'is', month_name, '.\n\n')


    # TO DO: display the most common day of week
    popular_day = df['Day of Week'].mode()[0]
    print('The most common day of the week is', popular_day, '.\n\n')


    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour    
    print('The most common start hour for your selection is', 
          df['Start Hour'].mode()[0], 'o\'clock.\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station for your selection is', 
          df['Start Station'].value_counts().idxmax(), '.\n\n')


    # TO DO: display most commonly used end station
    print('The most common end station for your selection is', 
          df['End Station'].value_counts().idxmax(), '.\n\n')


    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + ' (start) and ' + df['End Station'] + ' (end).'
    print('The most common station combination for your selection is ', 
          df['Station Combination'].value_counts().idxmax(), '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_sum_sec = df['Trip Duration'].sum()
    trip_sum_h = round(trip_sum_sec / 60 / 60 ,0)
    print('The total travel time for your selection is', trip_sum_h, 'hours.\n\n')


    # TO DO: display mean travel time
    trip_mean_sec = df['Trip Duration'].mean()
    trip_mean_min = round(trip_mean_sec / 60  ,0)
    if trip_mean_min < 60:
        print('The mean travel time for your selection is', trip_mean_min, 'minutes.\n\n')
    else:
        trip_mean_h = round(trip_mean_min / 60 ,1)
        print('The mean travel time for your selection is', trip_mean_h, 'hours.\n\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertypes = df['User Type'].values
    ct_subscriber  = (usertypes == 'Subscriber').sum()
    ct_customer = (usertypes == 'Customer').sum()
    print('The number of subscribers in', city.title(), 'is:',ct_subscriber,'\n')
    print('The number of customers in', city.title(), 'is:',ct_customer,'\n')


    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    if city.title() != 'Washington':
        # counts of gender
        # convert gender to an NumPy array for subseqent counts
        gender = df['Gender'].values
        
        # count the occurences of the different user types
        ct_male  = (gender == 'Male').sum()
        ct_female = (gender == 'Female').sum()
        
        print('The number of male users in', city.title(), 'is:',ct_male,'\n')
        print('The number of female users in', city.title(), 'is:',ct_female,'\n')
        
        # year of birth
        birthyear = df['Birth Year'].values
        
        # get unique birth years and exclude NaNs
        birthyear_unique = np.unique(birthyear[~np.isnan(birthyear)])
        
        latest_birthyear = birthyear_unique.max()
        earliest_birthyear = birthyear_unique.min()
        
        print('The most recent birth year of users in', city.title(), 'is:',
              latest_birthyear ,'\n')
        print('The earliest birth year of users in', city.title(), 'is:',
              earliest_birthyear,'\n')   
        
        # display most common birth year
        print('The most common birth year of users in', city.title(), 'is:', 
              df['Birth Year'].value_counts().idxmax(), '\n')
    
    else:
        # print message if Washington was chosen as city
        print('Sorry. Gender and birth year information are not available for Washington!')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# new function for raw data display    
def raw_data(df):
    """ Displays 5 lines of raw data at a time when yes is selected."""
    # define index i, start at line 1
    i = 1
    while True:
        rawdata = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if rawdata.lower() == 'yes':
            # print current 5 lines
            print(df[i:i+5])
            
            # increase index i by 5 to print next 5 lines in new execution
            i = i+5
            
        else:
            # break when no is selected
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,city,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        # additonal function to display raw data
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
