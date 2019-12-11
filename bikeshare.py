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
    print('Hello! Let\'s explore some US bikeshare data!')
     # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

while city.lower() not in ['Chicago', 'New York City', 'Washington']:
    city = input('Which city would you like to explore? Chicago, New York City or Washington')
if city.lower() == 'chicago':
    return 'chicago.csv'
elif city.lower() == 'new york city':
    return 'new_york_city.csv'
elif city.lower() == 'washington':
    return 'washington.csv'
else:
    print ('You have not selected one of the options. Please type chicago, new york city or washington')

    # TO DO: get user input for month (all, january, february, ... , june)

months={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
while month_input.lower() not in months.key():
    month_input = input('Which month would you like to explore?')
month=months[month_input.lower()]
return('2016-{}'.format(month),'2016-{}'.format(month+1))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

this_month = get_month()[0]
month= int(this_month[5:])
valid_date = False
while valid_date== False:
    is_int = False
    day = input('Which day would you like to explore? Use numbers to indicate Monday 1')
    while is_int ==False:
        try:
            day = int(day)
            is_int=True
            print('-'*40)
            return city, month, day
        
            def load_data(city, month, day):                
                """
                Loads data for the specified city and filters by month and day if   applicable.
                Args:
                (str) city - name of the city to analyze
                (str) month - name of the month to filter by, or "all" to apply no month filter
                (str) day - name of the day of week to filter by, or "all" to apply no day filter
                Returns:
                df - Pandas DataFrame containing city data filtered by month and day
                """

                return df
            def time_stats(df):
                """Displays statistics on the most frequent times of travel."""

                print('\nCalculating The Most Frequent Times of Travel...\n')
                start_time = time.time()

    # TO DO: display the most common month

                months=['January','February','March','April','May','June','July','August','September','October','November','December']
                index=int(df['start_time'].dt.month.mode())
                most_common_month=months[index-1]
                print('The most common month for bike rentals is {}'.format(most_common_month))

    # TO DO: display the most common day of week

                days_of_the_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
                index=int(df['start_time'].dt.dayoftheweek.mode())
                most_common_day=dayoftheweek[index]
                print('The most common day for bike rentals is {}'.format(most_common_day))

    # TO DO: display the most common start hour

                most_common_hour=int(df['start_time'].dt.hour.mode())
                if most_common_hour==0:
                    am_pm= 'am'
                    common_hour_readable=12
                elif 1<= most_common_hour <13:
                    am_pm='am'
                    common_hour_readable=most_common_hour
                elif 13<= most_common_hour <24:
                    am_pm='pm'
                    common_hour_readable=most_common_hour -12
                print('The most common hour for bike rentals is {}{}'.format(common_hour_readable, am_pm))

                print("\nThis took %s seconds." % (time.time() - start_time))
                print('-'*40)

            def station_stats(df):
                """Displays statistics on the most popular stations and trip."""

                print('\nCalculating The Most Popular Stations and Trip...\n')
                start_time = time.time()

    # TO DO: display most commonly used start station

                common_start_station=df['start_station'].mode().to_string()
                print('The most commonly used start station is {}'.format(common_start_station))
    # TO DO: display most commonly used end station
                common_end_station=df['end_station'].mode().to_string()
                print('The most commonly used end station is {}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
                common_start_station=df['start_station'].mode().to_string()
                common_end_station=df['end_station'].mode().to_string()
                print('The most commonly used start station is {}'.format(common_start_station))
                print('The most commonly used end station is {}'.format(common_end_station))

                print("\nThis took %s seconds." % (time.time() - start_time))
                print('-'*40)

            def trip_duration_stats(df):
                """Displays statistics on the total and average trip duration."""

                print('\nCalculating Trip Duration...\n')
                start_time = time.time()

    # TO DO: display total travel time
                total_travel_time=df['trip duration'].sum()
                print('total travel time:\n')

    # TO DO: display mean travel time
                mean_travel_time=df['trip duration'].mean()
                print('\nmean travel time:{}seconds'.format(mean_travel_time))

                print('\nThis took %s seconds.' % (time.time() - start_time))
                print('-'*40)
  
            def user_stats(df):
                """Displays statistics on bikeshare users."""

                print('\nCalculating User Stats...\n')
                start_time = time.time()

    # TO DO: Display counts of user types
                user_type=df['User Type'].value_counts()
                print(user_type)

    # TO DO: Display counts of gender
                if 'gender' in df.columns:
                    gender_count=df['gender'].value_count()
                    print(gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
                if 'birth year' in df.columns:
                    earliest_birth_year=df['birth year'].min()
                    latest_birth_year=df['birth year'].max()
                    most_common_birth_year=df['birth year'].mode()[0]
                    print('Earliest birth year:'+ str(earliest_birth_year))
                    print('Latest birth year:' + str(latest_birth_year))
                    print('MOst common birth year:' + str(most_common_birth_year))

                    print("\nThis took %s seconds." % (time.time() - start_time))
                    print('-'*40)

            def main():
                while True:
                    city, month, day = get_filters()
                    df = load_data(city, month, day)

                    time_stats(df)
                    station_stats(df)
                    trip_duration_stats(df)
                    user_stats(df)

                restart = input('\nWould you like to restart? Enter yes or no.\n')
                if restart.lower() != 'yes':
                    break


                if __name__ == "__main__":
                    main()