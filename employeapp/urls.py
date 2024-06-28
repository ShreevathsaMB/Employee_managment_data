from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addemployee/', views.employee_create, name='addemployee'),
    path('employelist/', views.employee_list, name='employelist'),
    path('deleteemployee/<int:pk>/', views.delete_employee, name='deleteemployee'),
    path('editemployee/<int:pk>/', views.edit_employee, name='editemployee'),
    path('employelist/pdf', views.generate_employee_list_pdf, name='generate_employee_list_pdf'),

]

