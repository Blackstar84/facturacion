from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy

# Create your views here.

class MixinFormInvalid:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        # Esto es para validar si el formulario se envía por medio de Ajax
        #if self.request.is_ajax():
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse(form.errors, status=400)
        else:
            return response


class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin, MixinFormInvalid):
    login_url = 'bases:login'
    raise_exception = False
    redirect_field_name = 'redirect_to'

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url = 'bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'

class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url= 'bases:login'
    template_name = "bases/sin_privilegios.html"
