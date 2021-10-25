import datetime
from .models import Records
from django.utils.timezone import get_current_timezone


def insert_in_database():
    with open('records/files.txt') as file:
        records = file.readlines()
        for record in records:
            record = record.rstrip().rstrip('.mp4')
            date = get_datetime(record[-10:])
            # record = record[:-10]
            print(record)
            r = Records.objects.create(
                title=record,
                file=f'records/video/{record}.mp4',
                type='video',
                public=True,
                date=date,
                time_create=date,
                time_update=date,

            )
            r.save_with_slug()


def get_datetime(date: str) -> datetime:
    try:
        day, month, year = date.split('-')
    except Exception as e:
        # raise RuntimeError('Что-то не так с переданной строкой с датой')
        print(f'Что-то не так с переданной строкой с датой - Ошибка: {e}')
        # return datetime.datetime(year=0, month=0, day=0)
    else:
        return datetime.datetime(year=int(year), month=int(month), day=int(day))
