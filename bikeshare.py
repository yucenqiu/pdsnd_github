import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city = input('Type in chicago, new york city, or washington: ').lower()
    
    while city not in ['chicago', 'new york city', 'washington', 'all']:
        city = input('Please type in chicago, new york city, or washington, or all: ').lower()
    
    month = input("Type in the the name of the month you want to view, january to june: ").lower()
    
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input('Please type in a month between January and June or type in all: ').lower()
    
    
    
    day = input("Type in one of the days of the week to view:").lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day = input('Please by in the name of a day in the week or all: ').lower()
    
    
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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['weekday'] == day.title()]
                
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is: {}'.format(most_common_month))
    
    # TO DO: display the most common day of week
    most_common_day = df['weekday'].mode()[0]
    print('The most common day is: {}'.format(most_common_day))
    
    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    most_common_hour = df['Start Hour'].mode()[0]
    print('The most common hour is: {}'.format(most_common_hour))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    most_common_start_station =  df['Start Station'].mode()[0]
    print('The most common starting station is {}'.format(most_common_start_station))
    
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common ending station is {}'.format(most_common_end_station))
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " " + df['End Station']
    most_common_trip = df['Trip'].mode()[0]
    print('The most common combination is: {}'.format(most_common_trip))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {} seconds'.format(total_travel_time))
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time is {} seconds'.format(mean_travel_time))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('The following displays the number of different users:')
    print(count_user_type)
    # TO DO: Display counts of gender
    if city != 'washington':
          count_gender = df['Gender'].value_counts()
          print('The following displays the number of users in each gender:')
          print(count_gender)
    
          # TO DO: Display earliest, most recent, and most common year of birth
          earliest_year_of_birth = df['Birth Year'].min()
          print('The earliest year of birth is: {}'.format(earliest_year_of_birth))
    
          most_recent_year_of_birth = df['Birth Year'].max()
          print('The most recent year of birth is: {}'.format(most_recent_year_of_birth))
    
          most_common_year_of_birth = df['Birth Year'].mode()[0]
          print('The most common year of birth is: {}'.format(most_common_year_of_birth))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    
    start_location = 0
    end_location = 5
    
    raw_data = input("Would you like to see the raw data?: ").lower()
    if raw_data == "yes":
        while end_location <= df.shape[0]:
            print(df.iloc[start_location:end_location])
            start_location += 5
            end_location += 5
            
            continue_display = input("Do you want to see 5 more lines of the data?: ").lower()
            if continue_display == "no":
                break
                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
        
if __name__ == "__main__":
	main()