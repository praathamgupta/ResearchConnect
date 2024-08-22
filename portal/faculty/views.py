from django.shortcuts import render
from .models import Faculty
from django.db.models import Q
import json
from urllib.parse import unquote_plus

def blog1(request):
    return render(request, 'faculty/blog1.html')

def blog2(request):
    return render(request, 'faculty/blog2.html')

def blog3(request):
    return render(request, 'faculty/blog3.html')

def blog4(request):
    return render(request, 'faculty/blog4.html')

def blog5(request):
    return render(request, 'faculty/blog5.html')

def search(request):
    query = request.GET.get('query', None)
    university = request.GET.get('university', None)
    area = request.GET.get('area', None)

    All_Faculties = Faculty.objects.all()

    if query:
        Faculties = (Faculty.objects.filter(Q(college__icontains=query)) | 
                     Faculty.objects.filter(Q(name__icontains=query)) | 
                     Faculty.objects.filter(Q(department__icontains=query)) | 
                     Faculty.objects.filter(Q(research_areas__icontains=query))) 
    else:
        Faculties = All_Faculties

    if university and area:
        Faculties = Faculties.filter(college__icontains=unquote_plus(university),
                                     research_areas__icontains=unquote_plus(area))
    elif university:
        Faculties = Faculties.filter(college__icontains=unquote_plus(university))
    elif area:
        Faculties = Faculties.filter(research_areas__icontains=unquote_plus(area))

    all_research_areas = set()
    for faculty in All_Faculties:
        research_areas_list = getattr(faculty, 'research_areas')
        for area in research_areas_list:
            all_research_areas.add(area)

    all_colleges = set()
    for faculty in All_Faculties:
        college = getattr(faculty, 'college')
        all_colleges.add(college)

    sorted_research_areas = sorted(all_research_areas)
    sorted_colleges = sorted(all_colleges)

    context = {
        'Faculties': Faculties,
        'research_areas': sorted_research_areas,
        'colleges': sorted_colleges,
    }

    return render(request, 'faculty/search.html', context)

def professor(request, professor_name):
    id = request.GET.get('id', None)
    professor = Faculty.objects.get(id = id)

    context = {
        'professor': professor,
    }

    return render(request, 'faculty/professor.html', context)

def home(request):
    Faculties = Faculty.objects.all()

    all_research_areas = set()
    for faculty in Faculties:
        research_areas_list = getattr(faculty, 'research_areas')
        for area in research_areas_list:
            all_research_areas.add(area)

    all_colleges = set()
    for faculty in Faculties:
        college = getattr(faculty, 'college')
        all_colleges.add(college)

    sorted_research_areas = sorted(all_research_areas)
    sorted_colleges = sorted(all_colleges)

    context = {
        'Faculties': Faculties[:3],
        'research_areas': sorted_research_areas,
        'colleges': sorted_colleges,
    }

    return render(request, 'faculty/home.html', context)
