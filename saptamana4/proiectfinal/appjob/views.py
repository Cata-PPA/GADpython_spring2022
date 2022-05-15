from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from appjob.models import Jobs


class JobsViews(LoginRequiredMixin, ListView):
    model = Jobs
    template_name = 'appjob/jobs_index.html'
    paginate_by = 3


class CreateJobsView(LoginRequiredMixin, CreateView):
    model = Jobs
    fields = ['tip_job', 'url_job', 'title_job', 'description_job', 'how_to_apply']
    template_name = 'appjob/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:lista_joburi')


class UpdateJobsView(LoginRequiredMixin, UpdateView):
    model = Jobs
    fields = ['tip_job', 'url_job', 'title_job', 'description_job', 'how_to_apply']
    template_name = 'appjob/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:lista_joburi')


@login_required
def delete_job(request, pk):
    Jobs.objects.filter(id=pk).update(active=0)
    return redirect('jobs:lista_joburi')


@login_required
def activate_job(request, pk):
    Jobs.objects.filter(id=pk).update(active=1)
    return redirect('jobs:lista_joburi')
