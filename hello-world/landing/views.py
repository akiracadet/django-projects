from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = 'landing/home.html'


    def get(self, request):
        return render(request, self.template_name, context={})


class AboutView(View):
    template_name = 'landing/about.html'


    def get(self, request):
        return render(request, self.template_name, context={})


class ContactView(View):
    template_name = 'landing/contact.html'


    def get(self, request):
        return render(request, self.template_name, context={})
