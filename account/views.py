from django.http import HttpResponse
from django.shortcuts import render
from .forms import StudentForm

#views.py
def student_view(request):
    template_name = "account/form.html"
    
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data saved successfully.')
    else:
        form = StudentForm()

    context = {'form': form}
    return render(request, template_name, context)

    ##
