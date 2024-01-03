from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection, transaction, IntegrityError, OperationalError
from apps.utils import dictfetchall, getMaxUcode
from apps.cbvusingquery.models import *
from apps.cbvusingquery.serializers import *
import os, sys, json


# Create your views here.


class EmployeeCRUD(APIView):
    def get(self, request):
        try:
            getEmployeeQuery = 'SELECT * FROM employee WHERE active=true ORDER BY ucode DESC'
            with connection.cursor() as c:
                c.execute(getEmployeeQuery)
                getEmployees = dictfetchall(c)

            return Response({'Success': True, 'Data': getEmployees}, status=status.HTTP_200_OK)

        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success': False, 'Error': str(err)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            requestData = request.data
            tablename = 'employee'

            firstname = requestData['firstname']
            lastname = requestData['lastname']
            emailid = requestData.get('emailid', None)
            mobile = requestData['mobile']
            department = requestData.get('department', None)
            salary = requestData.get('salary', None)
            active = requestData.get('active', True)

            ucode = getMaxUcode(tablename)

            addEmployeeQuery = 'INSERT INTO employee (ucode, firstname, lastname, emailid, mobile, department, salary, active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            addEmployeeValues = [ucode, firstname, lastname, emailid, mobile, department, salary, active]
            with connection.cursor() as c:
                c.execute(addEmployeeQuery, addEmployeeValues)

                getEmployeeQuery = f'SELECT * FROM employee WHERE ucode={ucode}'
                c.execute(getEmployeeQuery)
                employeeData = dictfetchall(c)

            return Response({'Success': True, 'Message': 'Employee details added successfully', 'Data': employeeData}, status=status.HTTP_201_CREATED)

        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success': False, 'Error': str(err)}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        try:
            requestData = request.data
            uid = requestData['uid']
            
            if uid in (None, 0, ''):
                raise Exception('uid is required')
            
            firstname = requestData.get('firstname', None)
            lastname = requestData.get('lastname', None)
            emailid = requestData.get('emailid', None)
            mobile = requestData.get('mobile', None)
            department = requestData.get('department', None)
            salary = requestData.get('salary', None)
            active = requestData.get('active', None)

            updateEmployeeQuery = 'UPDATE employee SET firstname=%s, lastname=%s, emailid=%s, mobile=%s, department=%s, salary=%s, active=%s WHERE uid=%s '
            updateEmployeeValues = [firstname, lastname, emailid, mobile, department, salary, active, uid]
            with connection.cursor() as c:
                c.execute(updateEmployeeQuery, updateEmployeeValues)

                getEmployeeQuery = f'SELECT * FROM employee WHERE uid={uid}'
                c.execute(getEmployeeQuery)
                employeeData = dictfetchall(c)

            return Response({'Success': True, 'Message': 'Employee details updated successfully', 'Data': employeeData}, status=status.HTTP_200_OK)

        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success': False, 'Error': str(err)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            requestData = request.data
            uid = requestData['uid']

            if uid in (None, 0, ''):
                raise Exception('uid is required')
            
            updateEmployeeQuery = f'UPDATE employee SET active=false WHERE uid={uid} '
            with connection.cursor() as c:
                c.execute(updateEmployeeQuery)

            return Response({'Success': True, 'Message': 'Employee details deleted successfully'}, status=status.HTTP_200_OK)

        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success': False, 'Error': str(err)}, status=status.HTTP_400_BAD_REQUEST)


class FilterEmployeeList(APIView):
    def post(self, request):
        try:
            requestData = request.data
            firstname = requestData.get('firstname', None)
            lastname = requestData.get('lastname', None)
            mobile = requestData.get('mobile', None)
            department = requestData.get('department', None)
            condition = (None, 0, '')

            searchQuery = ' WHERE active=true '

            if firstname not in condition:
                searchQuery += f''' AND firstname like '%{firstname}%' '''

            if lastname not in condition:
                searchQuery += f''' AND lastname like '%{lastname}%' '''

            if mobile not in condition:
                searchQuery += f''' AND mobile like '%{mobile}%' '''

            if department not in condition:
                searchQuery += f''' AND department='{department}' '''
            
            mainQuery = 'SELECT firstname, lastname, emailid, mobile, department, salary, active FROM employee'
            mainQuery += searchQuery + ' ORDER BY ucode DESC '

            with connection.cursor() as c:
                c.execute(mainQuery)
                data = dictfetchall(c)
            
            return Response({'Success': True, 'Data': data}, status=status.HTTP_200_OK)

        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success': False, 'Error': str(err)}, status=status.HTTP_400_BAD_REQUEST)