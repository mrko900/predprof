import requests
import datetime


TOKEN = 'ppo_10_24312'


def get_dates():
    header = {'X-Auth-Token': TOKEN}
    r = requests.get('https://olimp.miet.ru/ppo_it_final/date', headers=header)
    return r.json()['message']


def get_data_date(day, month, year):
    header = {'X-Auth-Token': TOKEN}
    url = f'https://olimp.miet.ru/ppo_it_final?day={day}&month={month}&year={year}'
    r = requests.get(url, headers=header)
    return r.json()


def convert_date_from_str(date: str):
    a = datetime.datetime.strptime(date, '%d-%m-%y')
    return a.day, a.month, a.year


def convert_date_to_str(day, month, year):
    return datetime.datetime(day=day, month=month, year=year).strftime("%d-%m-%y")


def get_data(day, month, year):
    data = get_data_date(day, month, year)

    if data['message'] == 'Wrong date':
        return None
    return data['message']['flats_count']['data'], data['message']['windows_for_flat']['data'], [data['message']['windows']['data'][i] for i in data['message']['windows']['data'].keys()]


def get_data_about_all_days():
    dates = [convert_date_from_str(i) for i in get_dates()]
    dates = [(i[0], i[1], int(str(i[2])[2:])) for i in dates]
    return {dates[i]: get_data(*dates[i]) for i in range(len(dates))}
