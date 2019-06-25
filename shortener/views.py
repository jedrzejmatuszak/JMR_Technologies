from django.shortcuts import render, redirect
from django.views import View
from shortener.models import URL
from shortener.forms import URLForm
from django.views.generic import FormView


class URLView(FormView):
    template_name = 'get_url.html'
    form_class = URLForm
    success_url = 'get_url'

    def form_valid(self, form):
        url = form.cleaned_data['url']
        url = URL.objects.create(url=url)
        url.save()  # saves second time to give unique short-url
        return render(self.request, 'short-url.html', {'url': url})


class RedirectView(View):

    def get(self, request, url_no):
        url = URL.objects.get(short_url__contains=url_no)
        return redirect(url.url)
