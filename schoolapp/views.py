from django.shortcuts import render , redirect
from schoolapp.models import School,Student
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#     return redirect('schoolapp:home')


class CreateSchool(CreateView):
    model = School
    fields= '__all__'
    # template_name = 'schoolapp/school_form.html'
    success_url = reverse_lazy('schoolapp:school_list')

class SchoolList(ListView):
    model = School

class UpdateSchool(UpdateView):
    model = School
    fields= '__all__'
    # template_name = 'schoolapp/school_form.html'
    success_url = reverse_lazy('schoolapp:school_list')

class SchoolDetail(DetailView):
    model = School

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        school = context['object']
        print(school.id)
        context['student_list'] = Student.objects.filter(school__id=school.id)
        return context

def deleteschool(request,id):
    a = School.objects.get(id=id)
    a.delete()
    return redirect('schoolapp:school_list')
# -------------------------------------------------------------------------
class AddStudent(CreateView):
    model = Student
    fields= '__all__'
    success_url = reverse_lazy('schoolapp:student_list')

class StudentList(ListView):
    model = Student

class UpdateStudent(UpdateView):
    model = Student
    fields= '__all__'
    success_url = reverse_lazy('schoolapp:student_list')

class StudentDetail(DetailView):
    model = Student

def deletestudent(request,id):
    a = Student.objects.get(id=id)
    a.delete()
    return redirect('schoolapp:student_list')


