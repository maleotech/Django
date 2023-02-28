from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student
from django.core.paginator import Paginator

from django.db.models import Q

class StudentListView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            qs = Student.objects.all()
            print('query', query)
            for term in query.split():
                qs = qs.filter( Q(first_name__icontains = term) | Q(last_name__icontains = term))
            student_list = qs
        else:
            student_list = Student.objects.all()

        paginator = Paginator(student_list, 5)  #   5 student data each page
        page_number = request.GET.get('page')
        students = paginator.get_page(page_number)

        context = {'students': students, 'query': query}
        return render(request, 'student_list.html', context)

class StudentDetailView(View):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        context = {'student': student}
        return render(request, 'student_detail.html', context)

class StudentCreateView(View):
    def get(self, request):
        form = StudentForm()
        context = {'form': form}
        return render(request, 'student_form.html', context)

    def post(self, request):
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        context = {'form': form}
        return render(request, 'student_form.html', context)

class StudentUpdateView(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        form = StudentForm(instance=student)
        context = {'form': form, 'student': student}
        return render(request, 'student_form.html', context)

    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=pk)
        context = {'form': form, 'student': student}
        return render(request, 'student_form.html', context)

class StudentDeleteView(View):
    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return redirect('student_list')

