from django.http import HttpResponse
from django.shortcuts import render,redirect

def read_file1():
    movies = []
    mid = 0
    with open('movies/Templates/movies/movies.txt') as f:
        for line in f.readlines():
            if line.count(',') is 1:
                movie_name,qty = line.split(',')
                movie = {'id':mid,'name':movie_name,'qty':int(qty)}
            movies.append(movie)
            mid += 1
    return movies

def read_customers():
    customers = []
    cid = 0
    with open('project4/customers.txt') as f:
        for line in f.readlines():
            if line.count(',') is 3:
                name,age,city, movie_rented = line.split(',')
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

def update_to_file(lines):
    with open('project4/customers.txt','w') as f:
        for item in lines:
            if "movie_rented" in item:
                f.write(item['name'] + ',' + item['age'] + ',' + item['city'] + ',' + item['movie_rented'])
            else:
                f.write(item['name'] + ',' + item['age'] + ',' + item['city'])         

def movies(req,cid):
    movies = read_file1()
    return render(req,'movies/movies.html',{'movies': movies})

def confirm(req,cid,mid):
    movies = read_file1()
    movie = movies[mid]

    customers = read_customers()
    customer = customers[cid]

    c = customer['name']
   
    m = movie['name']
    n = ""

    customer['city'] = str(customer['city']).replace('\n','')
    if m != "Delete Movie":
        if "movie_rented" in customer:
            customer['movie_rented'] = str(m) + '\n'
        else:
            customer.update({"movie_rented": str(m) + '\n'})
    else:
        customer.update({"movie_rented": str(n) + '\n'})

    customers[cid] = customer

    #customer.update({"movie_rented": str(m)})
    update_to_file(customers)
    return render(req, 'movies/final.html',{'customer':customer})


def write_line_to_file(line):
	with open('movies/movies.txt','a+') as f:
		f.write(line)

def update_to_file1(lines):
    with open('movies/Templates/movies/movies.txt','w') as f:
        for item in lines:
            if "qty" in item:
                print(f.write(item['movie_name'] + ',' + item['qty']) ) 


def get_detail(req,mid):
	movies = read_file1()
	movie = movies[mid]
	return render(req,'movies/mdetails.html',{'movie':movie})

