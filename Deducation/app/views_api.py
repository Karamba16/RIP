from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import render, redirect
from django.db import connection
from django.urls import reverse
from django.db.models import Q
from app import models,serializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from app.serializer import StudentSerializer
from app.models import Student
'''
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name']



class ApplicationForDeducationViewSet(viewsets.ModelViewSet):
    queryset = ApplicationForDeducation.objects.all()
    serializer_class = ApplicationForDeducationSerializer

    def create(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    @action(detail=True, methods=['put'])
    def confirm(self, request, pk=None):
        application = self.get_object()
        application.confirm()
        return Response({'status': 'confirmed'})

'''
class StudentList(APIView):
    model_class=Student
    serializer_class=StudentSerializer

    def get(self, request, format=None):
        """
        Возвращает список студентов
        """
        student = self.model_class.objects.all()
        serializer = self.serializer_class(student, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Добавляет новую студента
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    model_class = Student
    serializer_class = StudentSerializer

    def get(self, request, pk, format=None):
        """
        Возвращает информацию о студенте
        """
        student = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Обновляет информацию о студенте (для модератора)
        """
        student = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Удаляет информацию о студенте
        """
        student = get_object_or_404(self.model_class, pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['Put'])
def put_detail(request, pk, format=None):
    """
    Обновляет информацию об услуге (для пользователя)
    """
    student = get_object_or_404(Student, pk=pk)
    serializer = StockSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['Get'])
def get_student_list(request, format=None):
    """
    Возвращает список услуг
    """
    try:
        inserted_application = get_object_or_404(ApplicationForCalculation,application_status="Inserted")
        print(f'!!!{inserted_application.application_id}!!!')
    except:
        inserted_application = None
        pass
    print(inserted_application)

    print('get')
    query = request.GET.get("title")
    print(query)
    if query:
        student = Student.objects.filter(last_name__icontains=query,status="1")
    else:
        student = Student.objects.filter(status="1")
    serializer = StudentSerializer
    # print(serializer)
    print(type(serializer.data))
    if inserted_application:
        '''my_dict = [f'inserted application id = {inserted_application.application_id}', serializer.data]'''
        my_dict = {"inserted_application_id": inserted_application.application_id, "studentss": serializer.data}
        return Response(my_dict, template_name='tort')
    # my_dict = [serializer.data]
    # my_dict = {"calculations": serializer.data}
    my_dict = {"inserted_application_id": None, "calculations": serializer.data}
    return Response(my_dict, template_name='tort')





@api_view(['Get'])
def get_student_detailed(request, pk, format=None):
    """
    Возвращает конкретную услуги
    """
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = CalculationTypesSerializer(student)
        return Response(serializer.data)

@api_view(["Post"])
def create_student(request, format=None):
    """
       Создание услуги
    """
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["Delete"])
def delete_student(request, pk, format=None):
    """
       Удаление услуги
    """
    student = get_object_or_404(Student, pk=pk)
    student.status = "Deleted"
    student.save()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["Get"])
def get_applications_list(request, format=None):
    """
       Возвращает список заявок
    """
    print(request.data)
    '''start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    status = request.GET.get('status')'''
    data = request.data
    if data['start_date']:
        start_date = data['start_date']
    else:
        start_date = None
    if 'end_date' in data:
        end_date = data['end_date']
    else:
        end_date = None
    if data['status']:
        status = data['status']
    else:
        status = None
    print(start_date)
    print(status)
    applications_list = ApplicationForDeducation.objects.all()

    if start_date:
        applications_list = applications_list.filter(date_application_create__gte=start_date)
        if end_date:
            applications_list = applications_list.filter(date_application_create__lte=end_date)
    if status:
        print("aaaa")
        applications_list = applications_list.filter(application_status=status)

    applications_list = applications_list.order_by('-date_application_create')
    serializer = ApplicationForDeducationSerializer(applications_list, many=True)
    return Response(serializer.data)


@api_view(["Get"])
def get_application_detailed(request, pk, format=None):
    """
       Возвращает конкретную заявку
    """
    application = get_object_or_404(ApplicationForDeducation, pk=pk)
    serializer = ApplicationForDeducationSerializer(application)
    applications_students = ApplicationForDeducation.students.filter(application_id=pk)
    serializer_apps = ApplicationForDeducationSerializer(applications_students, many=True)

    filters = Q()
    print("aaaa")
    for stud in applications_students:
        filters |= Q(student_id=stud.student_id)
    print(filters)
    if filters != Q():
        student = Student.objects.filter(filters)
    else:
        student = {}
    serializer_stud = StudentSerializer(student, many=True)
    apps_stud_data = {
        'application': serializer.data,
        'student': serializer_stud.data
    }
    return Response(apps_stud_data)
    #return Response(serializer.data)


@api_view(['PUT'])
def change_inputs_application(request, pk, format=None):
    """
    Обновляет информацию в заявке - surname and reason
    """
    application = get_object_or_404(ApplicationForDeducation, pk=pk)
    if application.application_status != '1':
        return Response({"error": "Неверный статус."}, status=400)
    serializer = ApplicationDetailedSerializer(application, data=request.data, partial=True) #AplSer
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_student_from_application(request, application_id,calculation_id, format=None):
    """
      Удаление студента из заявки
    """
    application = get_object_or_404(ApplicationForDeducation, pk=application_id)

    applications_students = get_object_or_404(ApplicationForDeducation.students, application_id=application, student_id=student_id)

    applications_students.delete()

    serializer = ApplicationDetailedSerializer(application) #AplSer
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def put_applications_moderator(request, pk, format=None):
    """
    Обновляет информацию о заявке модератором
    """
    application = get_object_or_404(ApplicationForВувгсфешщт, pk=pk)
    print(application.application_status)
    print(f'_______{request.data}__________')
    print(request.data['application_status'])
    print(application.application_status)
    if request.data['application_status'] not in ['1','2','3','4','5'] or application.application_status == 'Inserted':
        return Response({"error": "Неверный статус."}, status=400)
    application.application_status = request.data['application_status']
    application.date_application_complete = datetime.now()
    serializer = ApplicationSerializer(application, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_applications_user(request, pk, format=None):
    """
    Обновляет информацию о заявке пользователем
    """
    application = get_object_or_404(ApplicationForDeducation, pk=pk)
    print(f'_______{request.data}__________')
    print('aaaaaaa')
    print(request.data['application_status'])
    print(application.application_status)
    if request.data['application_status'] != '3' or application.application_status != '1':
        return Response({"error": "Неверный статус."}, status=400)
    print("ssssss")
    application.application_status = request.data['application_status']
    print("ffffff")
    application.date_application_accept = date.today()
    print("wwwwwww")
    serializer = ApplicationSerializer(application, data=request.data, partial=True)
    print("oooooo")
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)