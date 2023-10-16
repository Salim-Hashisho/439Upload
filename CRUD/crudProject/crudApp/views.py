from django.shortcuts import render, redirect
from .models import Contact
from django.db import models
import datetime

def index(request):
  data = Contact.objects.all()
  context = {"data": data}
  return render(request, 'index.html', context)

def insertData(request):
  if request.method == 'POST':
    # we're getting them from the name attribute of the input 
    id = request.POST.get('id')
    name = request.POST.get('name')
    dob = request.POST.get('dob')

    year = int(dob[:4])
    month = int(dob[5:7])
    day = int(dob[8:10])
    
    date_of_birth = datetime.date(year=year, month=month, day=day)
    difference = (datetime.date.today() - date_of_birth).days
    print(difference)
    age = int(difference/365)
    
    email = request.POST.get('email')
    number = request.POST.get('number')
    address = request.POST.get('address')
    gender = request.POST.get('gender')
    image = request.FILES['image']
    query = Contact(id=id, name=name, age=age, dob=dob, email=email, number=number, address=address, gender=gender, image=image)
    query.save()
    return redirect('/')
  return render(request, 'index.html')

def updateData(request, id):
  if request.method == 'POST':
      id = request.POST.get('id')
      name = request.POST.get('name')
      dob = request.POST.get('dob')
      age = request.POST.get('age')
      email = request.POST.get('email')
      number = request.POST.get('number')
      address = request.POST.get('address')
      gender = request.POST.get('gender')
      image = request.FILES['image']
      contact = Contact.objects.get(id=id)
      # Update the contact details and image
      contact.name = name
      contact.age = age
      contact.dob = dob
      contact.email = email
      contact.number = number
      contact.address = address
      contact.gender = gender
      contact.image = image
      contact.save()
      return redirect('/')
  data = Contact.objects.get(id=id)
  context = {"d": data}
  return render(request, 'update.html', context)


def deleteData(request, id, models=models):
  data = Contact.objects.get(id=id)
  # print("data dob", data.dob.day)
  # print("data age", data.age)
  # date_of_birth = datetime.datetime(year=data.dob.year, month=data.dob.month, day=data.dob.day)
  # date_now = datetime.datetime.today()
  # print("dob", date_of_birth)
  # print("datenow", date_now)
  # print(date_now - date_of_birth)
  print(data.age)
  if (data.age < 18):
    data.delete()

  data = Contact.objects.all()
  context = {"data": data, "message":"Can only delete people below 18 years ols"}
  return render(request, 'index.html', context)
  return redirect('/', )