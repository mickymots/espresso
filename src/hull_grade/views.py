from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist 

from parchment_intake.models import ParchmentIntake
from green_beans_intake.models import GreenBeansIntake
from beans_intake.models import Intake, IntakeNotes, IntakeFiles, Location, Status,  DryingBatch, IntakeDetails, Inventory, InventoryFiles
from hull_grade.models import HullGradeIntake

from hull_grade.forms.hull_grade_intake_form import HullGradeIntakeForm
from hull_grade.forms.hull_grade_result_form import HullGradeResultForm
from hull_grade.forms.green_beans_intake_update_form import GreenBeansIntakeUpdateForm

from green_beans_intake.forms.green_beans_intake_form import GreenBeansIntakeForm
from green_beans_intake.models import GreenBeansIntake, GreenBeansIntakeFiles
from hull_grade.forms.hull_grade_intake_form import getHullGradeIntakes


intake_details_template = 'intake_details.html/'

def get_dashboard(request):
    context = {}

    query_results = HullGradeIntake.objects.filter(hulled_graded=False)
    context['query_results'] = query_results
 
    return render(request, 'hull_grade/hull_grade_dashboard.html', context=context)




def get_record_result_form(request, intake_id):
    context = {}
    intake_detail = HullGradeIntake.objects.get(id=intake_id)

    if request.POST:

        result_form = HullGradeResultForm(request.POST)
       
        if result_form.is_valid() :
            intake_detail = result_form.cleaned_data['hull_grade_intake']
            intake_detail.hulled_graded = True
            
            intake_detail.save()
            result_form.save()
            return redirect('hull_grade_index')

        else:
            intake_detail = result_form.cleaned_data['hull_grade_intake']
            context['intake_detail'] = intake_detail
            context['form'] = result_form

           
    else:
        context['intake_detail'] = intake_detail
        context['form'] = HullGradeResultForm()

    return render(request, 'hull_grade/hull_grade_record_result.html', context)


def getHullGradeIntakes(intake_id):
    partial_intake_exists = False
    hulled_graded_intakes = HullGradeIntake.objects.filter(intake_id=intake_id)
    total_bags = 0.0

    if hulled_graded_intakes:
        for intake in hulled_graded_intakes:
            total_bags += intake.no_of_full_bags
            if intake.partial_weight > 0:
                partial_intake_exists = True
        return (total_bags,partial_intake_exists) 


def get_inventory():
    inventory = Inventory.objects.all()
    result = []
    for intake in inventory:
        hull_grade_intakes = getHullGradeIntakes(intake.id)
        if hull_grade_intakes:

            total_hulled_graded_bags,partial_intake_exists = hull_grade_intakes
            
            full_bags_graded = intake.full_bags == total_hulled_graded_bags
            partial_bag_graded = intake.partial_bag_weight > 0 and partial_intake_exists
            
            if not (full_bags_graded and partial_bag_graded):
                result.append(intake)
        else:
            result.append(intake)
    return result


def get_parchments():
    parchments = ParchmentIntake.objects.all()
    result = []

    for intake in parchments:
        hull_grade_intakes = getHullGradeIntakes(intake.id)
        if hull_grade_intakes:
            total_hulled_graded_bags,partial_intake_exists = hull_grade_intakes
            is_full_bags_graded = total_hulled_graded_bags == intake.total_bags_count 
            if not is_full_bags_graded:
                result.append(intake)
        else:
            result.append(intake)
    return result


# show batchlist page
def get_batch_list(request):
    context = {}

    inventory = get_inventory()
    parchments = get_parchments()
    green_beans = GreenBeansIntake.objects.all()

    context['inventory'] = inventory
    context['parchments'] = parchments
    context['green_beans'] = green_beans

    return render(request, 'hull_grade/intake_batch_list.html', context=context)


def get_intake_form(request, batch_type, intake_id):
    template = 'hull_grade/hull_grade_intake.html'
    context = {}

    if request.POST:

        intake_form = HullGradeIntakeForm(request.POST)
       
        if intake_form.is_valid() :
            intake_form.save()
            return redirect('hull_grade_index')

        else:
            context['form'] = intake_form
            batch_type = intake_form.cleaned_data['batch_type']
            intake_id = intake_form.cleaned_data['intake_id']

            intake_detail = getIntakeDetail(batch_type, intake_id)

            context['intake_detail'] = intake_detail
            context['batch_type'] = batch_type
            
           
    else:
        intake_detail = getIntakeDetail(batch_type, intake_id)
        hull_graded_details = getHullGradeIntakes(intake_id)
        if hull_graded_details:
            total_hulled_graded_bags,partial_intake_exists = hull_graded_details
            context['total_hulled_graded_bags'] = total_hulled_graded_bags
            context['partial_intake_exists'] = partial_intake_exists
        # total_full_bags = get_bags_count(batch_type, intake_details)
        # Create new form
        context['intake_detail'] = intake_detail
        context['batch_type'] = batch_type
        


        context['form'] = HullGradeIntakeForm(initial={'batch_type': batch_type, 'intake_id': intake_id})
        

    return render(request, template, context)

# Method to update the green beans intake - largely follow green bean intake process
def get_intake_update_form(request, intake_id):
    template = 'hull_grade/green_bean_intake_update.html'

    context = {}
    if request.POST:

        intake_form = GreenBeansIntakeUpdateForm(request.POST)
       
        if intake_form.is_valid() :
            intake_id = intake_form.cleaned_data['intake_id']
            intake = GreenBeansIntake.objects.get(id=intake_id)

            intake.grade1_weight = intake_form.cleaned_data['grade1_weight']
            intake.grade2_weight = intake_form.cleaned_data['grade2_weight']
            intake.grade3_weight = intake_form.cleaned_data['grade3_weight']
            intake.grade_pb_weight = intake_form.cleaned_data['grade_pb_weight']
            intake.grade_fines_weight = intake_form.cleaned_data['grade_fines_weight']

            intake.save()
            return redirect('hull_grade_batch_list')

        else:
            context['form'] = intake_form
           
    else:
        intake_detail = GreenBeansIntake.objects.get(id=intake_id)
        form = GreenBeansIntakeForm(instance=intake_detail)
        context['form'] = form
        context['intake_id'] = intake_id
        

    return render(request, template, context)


def getIntakeDetail(batch_type, intake_id):

    if batch_type == 'CH':
        return Inventory.objects.get(id=intake_id)

    elif batch_type == 'PH':
        return ParchmentIntake.objects.get(id=intake_id)

    else:
        return  GreenBeansIntake.objects.get(id=intake_id) 