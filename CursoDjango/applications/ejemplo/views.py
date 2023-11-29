from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView , DetailView, CreateView , TemplateView, UpdateView, DeleteView
from .models import Usuario
from .forms import UsuarioForm

#CRUD = CREATE, READ, UPDATE Y DELETE


class PruebaView(TemplateView):
    template_name = 'inicio.html'


class PruebaListView(ListView):
    template_name = 'listausuario.html'
    context_object_name = 'listarusuario'
    model = Usuario

class PruebaCreateView(CreateView):
    template_name = 'createusuario.html'
    context_object_name = 'createusuario'
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('usuario_app:listarusuario')
    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.save
        return super(PruebaCreateView,self).form_valid(form)

class PruebaUpdateView(UpdateView):
    template_name = 'updateusuario.html'
    context_object_name = 'updateusuario'
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('usuario_app:listarusuario')
    def form_valid(self, form):
        return super(PruebaUpdateView,self).form_valid(form)
    
class PruebaDeleteView(DeleteView):
    model = Usuario
    template_name = 'deleteusuario.html'

    success_url = reverse_lazy('usuario_app:listarusuario')



