from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
import json
import requests
from .models import UrlsChecker, Link
from .forms import UrlsCheckerForms, LinkForm, IntervalForm
from .utils import *


def checker_page(request):
    checker_list = UrlsChecker.objects.all()
    interval_form = IntervalForm(auto_id=False)
    response_data = {}
    checked_links = []
    post = request.POST
    if request.method == 'POST' and request.is_ajax():
        form_id = request.POST.get('form_id')
        links = request.POST.get('links')
        links_data = json.loads(links)

        if len(links_data):
            for link in links_data:
                if link['watch']:
                    url = link['url']
                    try:
                        res = requests.post(url)
                        status = str(res.status_code)
                        res.raise_for_status()
                    except Exception as err:
                        status = str(err)
                    link['status'] = status
                checked_links.append(link)

        response_data['links'] = checked_links
        response_data['form_id'] = form_id
        return JsonResponse(json.loads(json.dumps(response_data)), safe=False)

    return render(request, 'checker/index.html', context={
        'checker_list': checker_list,
        'POST': post,
        'interval_form': interval_form
    })


class CheckerCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = UrlsCheckerForms
    template = 'checker/checker_create_template.html'
    redirect_url = 'checker:checker_page_url'


class CheckerUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = UrlsChecker
    model_form = UrlsCheckerForms
    template = 'checker/checker_update_template.html'
    redirect_url = 'checker:checker_page_url'


class LinkCreate(LoginRequiredMixin, ObjectCreateMixin,  View):
    model_form = LinkForm
    template = 'checker/link_create_template.html'

    def get(self, request):
        form = self.model_form()
        self.redirect_url = request.META.get('HTTP_REFERER')
        return render(request, self.template, context={'form': form,
                                                       'redirect_url': self.redirect_url,
                                                       })

    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            self.redirect_url = request.GET.get('redirect')
            return HttpResponseRedirect(self.redirect_url)
        return render(request, self.template, context={'form': bound_form})
