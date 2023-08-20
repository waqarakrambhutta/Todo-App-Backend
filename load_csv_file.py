import csv
import os
from django.core.wsgi import get_wsgi_application
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
application = get_wsgi_application()


from tasks.models import Tasks


def load_tasks_data(csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            task_name = row[0]
            task_description = row[1]
            task = Tasks(task_name=task_name, task_description=task_description)
            task.save()

if __name__ == '__main__':
    csv_file_path = '/home/waqar/Django/TodoBackend/MOCK_DATA.csv'
    load_tasks_data(csv_file_path)
