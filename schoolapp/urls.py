from django.urls import path, include
from schoolapp import views

app_name = 'schoolapp'

urlpatterns = [
    # path('', views.home, name = 'home'),
    path('add-school/',views.CreateSchool.as_view(), name = 'add_school'),
    path('', views.SchoolList.as_view(), name = 'school_list'),
    path('update-school/<int:pk>/',views.UpdateSchool.as_view(), name = 'update_school'),
    path('school-detail/<int:pk>/',views.SchoolDetail.as_view(), name = 'school_detail'),
    path('delete-school/<int:id>/',views.deleteschool, name = 'delete_school'),



    path('add-student/',views.AddStudent.as_view(), name = 'add_student'),
    path('student-list/', views.StudentList.as_view(), name = 'student_list'),
    path('update-student/<int:pk>/',views.UpdateStudent.as_view(), name = 'update_student'),
    path('student-detail/<int:pk>/',views.StudentDetail.as_view(), name = 'student_detail'),
    path('delete-student/<int:id>/',views.deletestudent , name = 'delete_student')
]