from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View, ListView, DetailView, TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from . models import PersonInfo, User


class Home(LoginRequiredMixin, View):
    """ Handle what user sees on the home page """
    template_name = 'record_form/index.html'

    def get(self, request):
        record = PersonInfo.objects.count()
        if request.user.is_authenticated:
            user = User.objects.all().count()
        context = {'record': record, 'user': user}
        return render(request, self.template_name, context)


class PersonInfoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'record_form/creation_form.html'
    model = PersonInfo
    success_message = "Record successfully submitted"
    fields = ['full_name', 'date_of_birth',
              'gender', 'id_type', 'id_number', 'mobile_number', 'disability_type', 'community_name',
              'street_name', 'land_mark', 'house_number', 'caregiver_name', 'caregiver_number', 'passport_pic']


class PersonInfoList(LoginRequiredMixin, ListView):
    template_name = 'record_form/list_form.html'
    model = PersonInfo
    field_list = [
        'full_name', 'date_of_birth',
        'gender', 'mobile_number', 'disability_type',
        'caregiver_name', 'caregiver_number',
    ]
    queryset = PersonInfo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel_name'] = 'All Records'
        context['panel_title'] = 'View All Records'
        context['field_list'] = self.field_list
        return context


class PersonInfoDetail(LoginRequiredMixin, DetailView):
    template_name = 'record_form/detail_form.html'
    model = PersonInfo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel_name'] = 'Record Details'
        context['panel_title'] = 'View Details'
        return context


class PersonInfoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'record_form/update_form.html'
    model = PersonInfo
    fields = ['full_name', 'date_of_birth',
              'gender', 'id_type', 'id_number', 'mobile_number', 'disability_type', 'community_name',
              'street_name', 'land_mark', 'house_number', 'caregiver_name', 'caregiver_number', 'passport_pic']
