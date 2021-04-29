from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView

from django.urls import reverse_lazy

from . import models

from django.views.generic.edit import CreateView, UpdateView, DeleteView



class CinemaListView(LoginRequiredMixin, ListView): 
    model = models.Cinema
    template_name = 'cinema_list.html'
    login_url = 'login'


class CinemaDetailView(LoginRequiredMixin, DetailView): 
    model = models.Cinema
    template_name = 'cinema_detail.html'
    login_url = 'login'
    

class CinemaUpdateView(LoginRequiredMixin, UpdateView): 
    model = models.Cinema
    fields = ['title', 'address', ] 
    template_name = 'cinema_edit.html'
    login_url = 'login'


class CinemaDeleteView(LoginRequiredMixin, DeleteView): 
    model = models.Cinema
    template_name = 'cinema_delete.html'
    success_url = reverse_lazy('cinema_list')
    login_url = 'login'
    

class CinemaCreateView(LoginRequiredMixin, CreateView): 
    model = models.Cinema 
    template_name = 'cinema_new.html' 
    fields = ['title', 'address']
    login_url = 'login'

    def form_valid(self, form): 
        form.instance.author = self.request.user 
        return super(CinemaCreateView, self).form_valid(form)


class SeansCreateView(LoginRequiredMixin, CreateView): 
    """создание нового сеанса"""
    model = models.Seans 
    template_name = 'seans_new.html' 
    fields = ['cinema','seans','date','time',]    
    login_url = 'login'
    
    def form_valid(self, form): 
        form.instance.author = self.request.user 
        return super(SeansCreateView, self).form_valid(form)


class SeansUpdateView(LoginRequiredMixin, UpdateView): 
    model = models.Seans
    fields = ['cinema','seans','date','time',]    
    template_name = 'seans_edit.html'
    login_url = 'login'


class SeansDeleteView(LoginRequiredMixin, DeleteView): 
    model = models.Seans
    template_name = 'seans_delete.html'
    success_url = reverse_lazy('cinema_list')
    login_url = 'login'


