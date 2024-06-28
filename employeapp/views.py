from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.contrib.admin.views.decorators import staff_member_required


def employee_list(request):
  employees = Employee.objects.all()
  context = {'employees': employees}
  return render(request, 'employelist.html', context)


def employee_create(request):
  if request.method == 'POST':
    form = EmployeeForm(request.POST, request.FILES)  # Include uploaded files
    if form.is_valid():
      form.save()
      return redirect('employelist')
  else:
    form = EmployeeForm()
  return render(request, 'addemployee.html', {'form': form})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employelist')
   
  # Ensure user is logged in
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)  # Update existing employee
        if form.is_valid():
            employee=form.save()
            return redirect(employee_list)
    else:
        form = EmployeeForm(instance=employee)  # Pre-populate edit form with existing data
    return render(request, "addemployee.html", {'form': form})
  
  
from reportlab.pdfgen import canvas 

def generate_employee_list_pdf(request):
    employees = Employee.objects.all()

    # Create a temporary buffer to hold the PDF data
    buffer = BytesIO()

    # Create the PDF object with the buffer
    pdf = canvas.Canvas(buffer)
    pdf.setTitle("Employee List")

    # Add headers
    pdf.drawString(50, 750, "Employee Name")
    pdf.drawString(200, 750, "Department")  # Adjusted position for department
    pdf.drawString(350, 750, "Years of Exp.")
    pdf.drawString(450, 750, "Salary")
    pdf.drawString(550, 750, "Company")
    pdf.drawString(650, 750, "DoJ")  # Added DoJ header

    # Iterate through employees and add data to table
    y_pos = 700
    for employee in employees:
        pdf.drawString(50, y_pos, employee.name)
        pdf.drawString(200, y_pos, employee.company)  # Added department (assuming company)
        pdf.drawString(350, y_pos, str(employee.years_of_experience))  # Convert to string
        pdf.drawString(450, y_pos, str(employee.salary))  # Convert to string
        pdf.drawString(550, y_pos, employee.company)  # Added company
        if employee.doj:  # Check if DoJ exists before drawing
            pdf.drawString(650, y_pos, employee.doj.strftime("%Y-%m-%d"))  # Format DoJ
        y_pos -= 20

    # Close the PDF object (important to save data)
    pdf.save()

    # Set the response content and return the PDF
    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="employee_list.pdf"'
    return response


def home(request):
 
  return render(request, 'home.html')

