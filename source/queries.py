# from datetime import datetime, timedelta
# import os, django
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
# django.setup()
# from issuetracker.models import Project, Task, Type
#
#
# # second task, thrid part...
# project = Project.objects.all()
# print(project.filter(task_project__description__icontains='Needs'))
#
# # second task, second part...
# type = Project.objects.filter(tittle__icontains='app').values('tittle')
# Type.objects.filter()
# print(Type.objects.filter(task_type__project__tittle__in=type).distinct())
#
#
# # second task, first part...
# dt = datetime.now()
#
# task = Task.objects.filter(status__status__icontains='done')
# end = datetime.now()
# start = end - timedelta(days=30)
#
# task_done = task.filter(created_at__range=(start, end))
#
# print(task_done)
