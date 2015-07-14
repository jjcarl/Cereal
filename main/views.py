from django.shortcuts import render
from django.http import HttpResponse
from main.models import Cereal, CerealMaker
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator


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
