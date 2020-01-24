from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


class ObjectCreateMixin:
    model_form = None
    template = None
    redirect_url = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(reverse(self.redirect_url))
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None
    redirect_url = None

    def get(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form,
                                                       self.model.__name__.lower(): obj,
                                                       })

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        bound_form = self.model_form(request.POST, instance=obj)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(reverse(self.redirect_url))
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})
