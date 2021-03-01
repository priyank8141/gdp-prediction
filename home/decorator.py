from django.shortcuts import render

def role_required(allowed_roles =[]):
    def dec(view_fun):
        def wrap(request,*args,**kwargs):
            userdata = request.session.get('userdata')
            print(userdata['role'])
            if userdata['role'] in allowed_roles:
                return view_fun(request,*args,**kwargs)
            else:
                return render(request, "nopermission.html")
        return wrap
    return dec