from django.contrib.auth.decorators import login_required
from .models import Department
from .forms import DepartmentForm
from django.shortcuts import render, get_object_or_404, redirect

def department_list(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        departments = Department.objects.filter(name__icontains=search_query)
    else:
        
        departments = Department.objects.all()

    return render(request, 'department_list.html', {'departments': departments})
@login_required
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'department_form.html', {'form': form})

def department_update(request, dept_id):
    department = get_object_or_404(Department, dept_id=dept_id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')  
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'department_update.html', {'form': form, 'department': department})



@login_required
def department_delete(request, dept_id):
    department = get_object_or_404(Department, id=dept_id)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'department_confirm_delete.html', {'department': department})
