from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Description

def index(request):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def add(request):
    errors_course = Course.objects.validator(request.POST)
    errors_description = Description.objects.validator(request.POST)

    if len(errors_course) > 0:
        for key, value in errors_course.items():
            messages.error(request, value)
        return redirect('/courses/')
    elif len(errors_description) > 0:
        for key, value in errors_description.items():
            messages.error(request, value)
    else:
        course = Course.objects.create(name=request.POST['name'])
        content = Description.objects.create(content=request.POST['content'], course=course)
        messages.success(request, 'Course successfully created')
        return redirect('/courses/')

def delete_index(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'delete_index.html', context)

def destroy(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('/courses/')