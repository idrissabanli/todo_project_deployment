from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateTaskForm
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

def content(request):
    return render(request, 'tasks.html')

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'task_list'
    # paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(assigned_to=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['my_tasks'] = self.model.objects.filter(owner=self.request.user)[:3]
        return context


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'create_task.html'
    # fields = '__all__'
    form_class = CreateTaskForm
    success_url = reverse_lazy('todo:tasks')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.owner = self.request.user
        task.save()
        return super().form_valid(form)


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        axtarilan_user = self.request.GET.get('search')
        if axtarilan_user:
            return User.objects.filter(is_superuser=False, username__icontains=axtarilan_user)
        return super().get_queryset()



class TaskViewSetAPI(ReadOnlyModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

