from .models import Records


def insert_in_database():
    with open('records/files.txt') as file:
        records = file.readlines()
        for record in records:
            record = record.rstrip().rstrip('.mp4')
            print(record)
            r = Records.objects.create(
                title=record,
                file=f'records/video/{record}.mp4',
                type='video',
                public=True,

            )
            r.save_with_slug()
