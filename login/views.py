import psycopg2
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
def show_login(request):
    print("this is login page")
    return render(request, "login.html")

def logproess(request):
    conn = psycopg2.connect(database="agriculture", user='postgres', password='priyank8141', host='127.0.0.1',port='5432')
    cursor = conn.cursor()

    print("this is login process")
    if (request.method == 'POST'):
        try:
            email = request.POST['email']
            password = request.POST['password']
            Query = "select * from signup_user where email = %s"
            cursor.execute(Query, (email,))
            records = cursor.fetchall()
            print(records)
            id=records[0][0]
            if records[0][10] == password:
                print("success login")
                if records[0][10] == 'farmer':
                    print("farmer")
                    return HttpResponseRedirect(reverse("farmerlog", args=(id,)))
                elif records[0][10] == 'sarpanch':
                    print("sarpanch")
                    return HttpResponseRedirect(reverse("sarpanchlog", args=(id,)))
                elif records[0][10] == 'organization':
                    print("organization")
                    return HttpResponseRedirect(reverse("organizationlog", args=(id,)))
            else:
                context = {
                'message': 'invalid password and username'
                }
                return render(request, "login.html", context)

            # for row in records:
            # print("Id = ", row[0], )
            #     print("Model = ", row[1])
            #     print("Price  = ", row[2])
            # if ins is None:
            #     context = {
            #     'message': 'invalid password and username'
            #     }
            #     return render(request, "login.html",context)
            # else:
            #     return render(request, "signup.html")
            #     print("success login")
        except (Exception, psycopg2.Error) as error:
            print("error:-", error)

        finally:
        # closing database connection.
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

