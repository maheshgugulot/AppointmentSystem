import json
from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime

def home(request):
     return render(request,'login.html')


def create_account(request):
    url = "https://appointment-system-api.p.rapidapi.com/appointment/createAccount"

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        clinic_name = request.POST.get('clinicName')
        user_first_name = request.POST.get('userFirstName')
        user_last_name = request.POST.get('userLastName')
        interval = request.POST.get('interval')
        
        querystring = {
            "username": username,
            "password": password,
            "clinicName": clinic_name,
            "userFirstName": user_first_name,
            "userLastName": user_last_name,
            "interval": interval
        }
        payload = {
            "key1": "value",
            "key2": "value"
        }
        headers = {
            "content-type": "application/json",
	        "X-RapidAPI-Key": "fc6057025cmshfd8290552b29756p11c73bjsn46e5916df597",
            "X-RapidAPI-Host": "appointment-system-api.p.rapidapi.com"
        }
        response = requests.post(url, json=payload, headers=headers, params=querystring)
        return HttpResponse(response)
    return render(request,'create_account.html')
def login(request):
    url = "https://appointment-system-api.p.rapidapi.com/appointment/login"

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        querystring = {
            "username": username,
            "password": password
        }
        headers = {
            "X-RapidAPI-Key": "fc6057025cmshfd8290552b29756p11c73bjsn46e5916df597",
            "X-RapidAPI-Host": "appointment-system-api.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        print(response.text)
        

        return render(request, 'view.html', {'my_list':response.text })        
    return render(request,'login.html')

def appointment_time_list(request):

    url = "https://appointment-system-api.p.rapidapi.com/appointment/getHoursByDayByClinic"

    if request.method == 'POST':
        date = request.POST.get('date')
        clinic_name = request.POST.get('clinicName')

        
        querystring = {
            "username": date,
            "clinicName": clinic_name,

        }
        headers = {
            "X-RapidAPI-Key": "fc6057025cmshfd8290552b29756p11c73bjsn46e5916df597",
            "X-RapidAPI-Host": "appointment-system-api.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        return HttpResponse(response)
    return render(request,'appointment_time_list.html')

def add_appointment(request):

        url = "https://appointment-system-api.p.rapidapi.com/appointment/addappointment"
        if request.method == 'POST':

            clinic_name = request.POST.get('clinicName')
            day= request.POST.get('day')
            hour= request.POST.get('hour')
            name= request.POST.get('name')
            phonenumber= request.POST.get('phonenumber')




            querystring = {
                "clinicName": clinic_name

            }
            payload = {
                "aDay": day,
                "aHour": hour,
                "aName": name,
                "aTel": phonenumber,
                "aType": "Appoint"
            }
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": "fc6057025cmshfd8290552b29756p11c73bjsn46e5916df597",
                "X-RapidAPI-Host": "appointment-system-api.p.rapidapi.com"
            }

            response = requests.post(url, json=payload, headers=headers, params=querystring)
            return HttpResponse(response)
        return render(request,'add_appointment.html')

def get_appointments(request):

    url = "https://appointment-system-api.p.rapidapi.com/appointment/getAppointments"
    if request.method == 'POST':
        date = request.POST.get('day')
        date_obj = datetime.strptime(date, "%Y-%m-%d")

        formatted_date = date_obj.strftime("%Y.%m.%d")
        clinic_name = request.POST.get('clinicName')
        print(formatted_date)
        print(clinic_name)
        
        querystring = {
            "date": formatted_date,
            "clinicName": clinic_name,
        }
        headers = {
            "X-RapidAPI-Key": "fc6057025cmshfd8290552b29756p11c73bjsn46e5916df597",
            "X-RapidAPI-Host": "appointment-system-api.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        print(response)
        
        json_data = response.json()
        json_list = json.dumps(json_data)

        return render(request, 'display.html', {'my_list': json_list})
    return render(request,'get_appointments.html')

def delete_appointment(request):

    url = "https://appointment-system-api.p.rapidapi.com/appointment/deleteappointment"
    if request.method == 'POST':

        app_id = request.POST.get('app_id')
        username = request.POST.get('username')
        token = request.POST.get('token')




        querystring = {"appId":app_id,"username":username,"token":token}

        headers = {
            "X-RapidAPI-Key": "fc6057025cmshfd8290552b29756p11c73bjsn46e5916df597",
            "X-RapidAPI-Host": "appointment-system-api.p.rapidapi.com"
        }

        response = requests.delete(url, headers=headers, params=querystring)

        return HttpResponse(response)
    return render(request,'delete_appointment.html')

def update_appointment(request):

    url = "https://appointment-system-api.p.rapidapi.com/appointment/updateAppointment"
    if request.method == 'POST':

        username = request.POST.get('username')
        token = request.POST.get('token')
        app_id = request.POST.get('app_id')
        day= request.POST.get('day')
        hour= request.POST.get('hour')
        name= request.POST.get('name')
        phonenumber= request.POST.get('phonenumber')


        querystring = {"username":username,"token":token}

        payload = {
            "id": app_id,
            "aDay": day,
            "aHour": hour,
            "aName":name,
            "aTel":phonenumber,
            "aType": "appoint"
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "fc6057025cmshfd8290552b29756p11c73bjsn46e5916df597",
            "X-RapidAPI-Host": "appointment-system-api.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers, params=querystring)
        return HttpResponse(response)
    return render(request,'update_appointment.html')

