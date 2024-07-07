from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.views.generic.edit import FormView, DeleteView


def get_all(request):
    tasks = Task.objects.all()  # достаем наши tasks через менеджер
    return render(
        request, "tasks/taskList.html", {"tasks": tasks}
    )  # рендерим наш queryset в html, а потом через for будем вытаскивать по 1 обьекты


class createTask(FormView):
    form_class = TaskForm  # обозначаем форму
    template_name = "tasks/taskForm.html"  # обозначаем template
    success_url = "task:all"  # передаем Url в случаии успеха

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class deleteTaks(DeleteView):
    model = Task
    success_url = "task:all"
