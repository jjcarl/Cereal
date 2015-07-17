from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from main.models import Cereal, CerealMaker
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.template import RequestContext
from main.forms import CerealSearchForm, CreateCerealForm
from django.core.urlresolvers import reverse
from django.views.generic import FormView

from django.core.mail import send_mail


class MakerListView(ListView):
    model = CerealMaker
    template_name = "cerealmaker_list.html"
    context_object_name = "maker_list"


class CerealDetailView(DetailView):
    model = Cereal
    template_name = "cereal_detail.html"
    context_object_name = "cereal"


def first_view(request, starts_with=None):

    makers = CerealMaker.objects.all()
    text_string = ''

    for maker in makers:
        cereals = maker.cereal_set.filter(name__startswith='%s' % starts_with)
        for cereal in cereals:
            text_string += "<b>%s</b>, makes %s, which has the following "\
                "nutritional information:</br>Calories: %s, Protein: %sg, "\
                "Fat: %sg, Sodium: %smg, Fiber: %sg, Carbohydrates: %sg,</br>"\
                "Sugars: %sg, Potassium: %smg, Vitamins: %s, "\
                "Serving Size: %s cups</br>"\
                % (maker, cereal.name, cereal.calories, cereal.protein,
                    cereal.fat, cereal.sodium, cereal.fiber, cereal.carbs,
                    cereal.sugars, cereal.potassium, cereal.vitamins,
                    cereal.cups_per_serving)

    return HttpResponse(text_string)


def template_view(request):

    context = {}

    maker_cereal = {}

    makers = CerealMaker.objects.all()

    for maker in makers:
        cereals = maker.cereal_set.filter(name__startswith="")
        print cereals

        maker.manufacturer = {maker.manufacturer: cereals}

        maker_cereal.update(maker.manufacturer)

    context['makers'] = maker_cereal

    return render(request, 'template_view.html', context)


def detailed_view(request):

    context = {}

    maker_cereal = {}

    makers = CerealMaker.objects.all()

    for maker in makers:
        cereals = maker.cereal_set.all()
        print cereals

        maker.manufacturer = {maker.manufacturer: cereals}

        maker_cereal.update(maker.manufacturer)

    context['makers'] = maker_cereal

    return render(request, 'detailed_view.html', context)


@csrf_exempt
def get_post(request):

    if request.method == 'GET':
        cereal_maker_string = """

        <form action="/get_post/" method="POST">

        Maker:
        <br>
        <input type="text" name="maker">

        <br>

        Cereal:
        <br>
        <input type="text" name="Cereal">

        <br>
        <br>
        <input type="submit" value="Submit">

        </form>

        """

        return HttpResponse(cereal_maker_string)

    elif request.method == 'POST':

        cereal_maker_string = """

        <form action="/get_post/" method="POST">

        Maker:
        <br>
        <input type="text" name="manufacturer">

        <br>

        Cereal:
        <br>
        <input type="text" name="name">

        <br>
        <br>
        <input type="submit" value="Submit">

        </form>

        """

        get_cereal_maker = request.POST.get('manufacturer', None)

        get_cereal = request.POST.get('name', None)

        makers = CerealMaker.objects.filter(manufacturer__startswith="%s" %
                                            get_cereal_maker)

        for maker in makers:
            cereals = maker.cereal_set.filter(name__startswith="%s" %
                                              get_cereal)
            for cereal in cereals:
                cereal_maker_string += "<b>%s</b>, makes %s, which has "\
                    "the following nutritional "\
                    "information:</br>Calories: %s, Protein: %sg, Fat: %sg, "\
                    "Sodium: %smg, Fiber: %sg, Carbohydrates: %sg, </br>"\
                    "Sugars: %sg, Potassium: %smg, Vitamins: %s, "\
                    "Serving Size: %s cups.</br>"\
                    % (maker, cereal.name, cereal.calories, cereal.protein,
                        cereal.fat, cereal.sodium, cereal.fiber, cereal.carbs,
                        cereal.sugars, cereal.potassium, cereal.vitamins,
                        cereal.cups_per_serving)

        response = cereal_maker_string

        return HttpResponse(response)


class GetPost(View):
    form = """
        <form action="/GetPost/" method="POST">

        Maker:
        </br>
        <input type="text" name="manufacturer" />
        </br>

        Cereal:
        </br>
        <input type="text" name="name" />
        </br>
        <input type="submit" value="Submit"/>

        </form>
        """

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.form)

    def post(self, request, *args, **kwargs):
        get_cereal_maker = request.POST.get('manufacturer', None)

        get_cereal = request.POST.get('name', None)

        makers = CerealMaker.objects.filter(manufacturer__startswith="%s"
                                            % get_cereal_maker)

        for maker in makers:
            cereals = maker.cereal_set.filter(name__startswith="%s" %
                                              get_cereal)
            for cereal in cereals:
                self.form += "<b>%s</b>, makes %s, which has "\
                    "the following nutritional "\
                    "information:</br>Calories: %s, Protein: %sg, Fat: %sg, "\
                    "Sodium: %smg, Fiber: %sg, Carbohydrates: %sg, </br>"\
                    "Sugars: %sg, Potassium: %smg, Vitamins: %s, "\
                    "Serving Size: %s cups.</br>"\
                    % (maker, cereal.name, cereal.calories, cereal.protein,
                        cereal.fat, cereal.sodium, cereal.fiber, cereal.carbs,
                        cereal.sugars, cereal.potassium, cereal.vitamins,
                        cereal.cups_per_serving)

        response = self.form

        return HttpResponse(response)


def cereal_search(request):
    request_context = RequestContext(request)
    context = {}

    if request.method == 'POST':
        form = CerealSearchForm(request.POST)
        context['form'] = form

        if form.is_valid():

            name = form.cleaned_data['name']
            manufacturer = form.cleaned_data['manufacturer']

            context['cereal_list'] = Cereal.objects.filter(name__startswith=name, manufacturer__manufacturer__startswith=manufacturer)

            context['valid'] = "Form is Valid"

        else:
            context['valid'] = form.errors

        return render_to_response("cereal_search.html", context, context_instance=request_context)

    else:
        form = CerealSearchForm()
        context['form'] = form

        return render_to_response("cereal_search.html", context, context_instance=request_context)


def cereal_create(request):
    request_context = RequestContext(request)
    context = {}

    if request.method == 'POST':
        form = CreateCerealForm(request.POST)
        context['form']

        if form.is_valid():
            form.save()

            context['valid'] = "Cereal Saved"

        else:
            context['valid'] = form.errors

        return render_to_response("cereal_create.html", context, context_instance=request_context)

    else:
        form = CreateCerealForm()
        context['form'] = form

        return render_to_response("cereal_create.html", context, context_instance = request_context)


class CerealSearchView(FormView):
    template_name = 'cereal_search.html'
    form_class = CerealSearchForm

    def form_valid(self, form):
        request_context = RequestContext(self.request)

        context = {}

        name = form.cleaned_data['name']
        manufacturer = form.cleaned_data['manufacturer']

        context['cereal_list'] = Cereal.objects.filter(name__startswith=name, manufacturer__manufacturer__startswith=manufacturer)

        send_mail('Cereal Name starts with %s' % name, 'The Maker is %s.' % manufacturer, 'jcarl9000@gmail.com', ['jcarl9000@gmail.com'], fail_silently=False)

        return render_to_response("cereal_search.html", context, context_instance=request_context)
