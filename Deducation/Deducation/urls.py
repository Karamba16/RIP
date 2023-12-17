"""
URL configuration for Deducation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from app import views,views_api,serializer
from rest_framework import routers

router = routers.DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    #path('admin/', admin.site.urls),
    #path('student/<int:id>/', views.detailed_service_page, name='detailed'),
    #path('', views.service_page, name='main'),

    path(r'students/', views_api.StudentList.as_view(), name='student-list'),
    path(r'students/<int:pk>/', views_api.StudentDetail.as_view(), name='students-detail'),
    path(r'students/<int:pk>/put/', views_api.put_detail, name='students-put'),
    path(r'students/<int:pk>/edit/', views_api.change_calculation_type_data, name='change_data'),
    path(r'students/<int:pk>/delete/', views_api.delete_calculation, name='delete_student'),
    path(r'students/<int:pk>/add/', views_api.add_calculation_type, name='add_student'),
    path(r'students/<int:pk>/edit_im/', views_api.change_calculation_image, name='change_student_image'),

    path(r"applications/", views.get_applications_list, name='applications_list'),
    '''
    path(r"applications/<int:pk>/", views.get_application_detailed, name='get_application_detailed'),
    path(r'applications/<int:pk>/change_inputs/', views.change_inputs_application, name='change_inputs_application'),
    path(r'applications/<int:application_id>/delete/', views.delete_application_for_calculation, name='delete_application'),
    path(r'applications/<int:pk>/change_status/moderator/', views.put_applications_moderator, name='application_status_by_moderator'),
    path(r'applications/<int:pk>/change_status/client/', views.put_applications_client, name='application_status_by_client'),

    path(r'applications_calculations/<int:pk>/<int:calculation_id>/', views.edit_result_applications_calculations, name='edit_result_applications_calculations'),
    path(r'applications_calculations/<int:application_id>/operations_delete/<int:calculation_id>/', views.delete_calculation_from_application,name='delete_calculation_from_application'),
'''
]
