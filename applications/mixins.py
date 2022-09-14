from django.views.generic.detail import SingleObjectMixin
from .models import Application, Content, Status
from django.contrib.auth.models import Group


class ApplicationsMixin(SingleObjectMixin):
    model = Application

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        context['apps'] = Application.objects.all()
        context['user'] = self.request.user
        context['group'] = Group.objects.get(user=self.request.user.pk)


        if context['group'].name == 'Администрация':
            pod = Status.objects.all()
        elif context['group'].name == 'OTK':
            pod = Status.objects.filter(name__in=['Бух готово', 'ОТК частичная готовность', 'Отгружено'])
        elif context['group'].name == 'Бухгалтера':
            pod = Status.objects.filter(name__in=['Бух на рассмотрении',])
        elif context['group'].name == 'Кладовщики':
            pod = Status.objects.filter(name__in=['ОТК готово', 'ОТК частичная готовность'])
        elif context['group'].name == 'Коммерция директора':
            pod = Status.objects.all()
        elif context['group'].name == 'Менеджеры':
            pod = Status.objects.all()
        elif context['group'].name == 'Начальники производства':
            pod = Status.objects.filter(name__in=['ОТК готово', 'Бух готово', 'ОТК частичная готовность'])
        elif context['group'].name == 'КБ':
            pod = Status.objects.filter(name__in=['ОТК готово', ])
        elif context['group'].name == 'Паспортист':
            pod = Status.objects.filter(name__in=['ОТК готово', ])
        elif context['group'].name == 'Электрики':
            pod = Status.objects.filter(name__in=['ОТК готово', ])

        if context['group'].name == 'Менеджеры':
            context['apps'] = Application.objects.filter(status__in=(pod), user_manager=self.request.user)
        elif context['group'].name == 'Коммерция директора':
            context['apps'] = Application.objects.filter(status__in=(pod), boss=self.request.user)
        else:
            context['apps'] = Application.objects.filter(status__in=(pod))
        return context



