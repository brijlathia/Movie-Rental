from django.http import HttpResponse
from django.shortcuts import render,redirect
from movies.views import read_file1
def read_file():
    customers = []
    cid = 0
    
    with open('project4/customers.txt') as f:
        for line in f.readlines():
            if line.count(',') is 3:
                name,age,city,movie_rented = line.split(',')
                cust = {'id':cid,'name':name,'age':age,'city':city, 'movie_rented':movie_rented}
            else:    
                name,age,city = line.split(',')
                cust = {'id':cid,'name':name,'age':age,'city':city}
            customers.append(cust)
            cid += 1
    #customers = sorted(customers, key = lambda i: i['name'])
    return customers

def write_line_to_file(line):
	with open('project4/customers.txt','a+') as f:
		f.write(line)

def update_line_to_file(line, cid):
	with open('project4/customers.txt','a+') as f:
		f.write(line)

def customerslist(req):
    customers = read_file()
    movies = read_file1()
    detail = {'customers':customers,'movies':movies}
    return render(req,'movies/main.html', detail)

def get_detail(req,cid):
	customers = read_file()
	customer = customers[cid]
	return render(req,'movies/detail.html',{'customer':customer})

def add_user(req):
    cid = req.GET.get('cid')
    name = req.GET.get('name')
    age = req.GET.get('age')
    city = req.GET.get('city')
    newCust = name+','+str(age)+','+city+'\n'
    write_line_to_file(newCust)
    return redirect('http://127.0.0.1:8000/customers')

