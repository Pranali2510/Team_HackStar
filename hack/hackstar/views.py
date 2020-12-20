from .models import cleanliness_model, lost_found_model, EventDetails, Order, Foods, Event, Eregister,contact_model
from .form import cleanliness_form,  lost_found_form,contact_form,order_form
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from math import ceil
from django.views.decorators.cache import cache_control

from .models import UserDetails


def home(request):
    return render(request, 'index.html')


def view_order(request,id):
    # x=Order.objects.filter(id=id)
    # print(x.name)
    x = Order.objects.get(pk=id)
    print(x.name)
    if id == 0:
        form = order_form(request.POST)
    else:
        x = Order.objects.get(pk=id)
        form = order_form(request.POST, instance=x)

    if form.is_valid():
        form.save()
        return redirect('view_canteen')
    return render(request, "view_order.html", {"order1":x})
    # return render(request, 'view_order.html',{"order1":x})


def delete_order(request, id):
    form3 = Order.objects.get(pk=id)
    form3.delete()
    return redirect('view_canteen')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def registerevent(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        event_id = request.POST.get('eid','')
        prn = request.POST.get('prn', '')
        course = request.POST.get('course','')
        year = request.POST.get('year', '')
        phone = request.POST.get('phone',0)
        event = Eregister(name=name, event_id=event_id, prn=prn, course=course, year=year, phone=phone)
        event.save()
        return render(request, 'event.html')
    return render(request, 'registerevent.html')

def create_event(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        desc = request.POST.get('desc','')
        date = request.POST.get('date', '')
        register = request.POST.get('register',0)
        event = Event(name=name, desc=desc, date=date, register=register)
        event.save()
        return render(request, 'view_event.html')
    return render(request, 'create_event.html')

def view_event(request):
    complaint = Event.objects.all()
    return render(request, 'view_event.html', {'complaint': complaint})


def canteen(request):
    allProds = []
    catprods = Foods.objects.values('canteen_name', 'id')
    cats = {item['canteen_name'] for item in catprods}
    for cat in cats:
        prod = Foods.objects.filter(canteen_name=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides),nSlides])
    params = {'allProds':allProds}
    return render(request, 'canteen.html', params)


def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson','')
        list2 = [ v for k, v in items_json.items()]
        c=[]
        for i in list2:
	        c.append(str(i[0]) +' items of '+ i[1])
        toprice = request.POST.get('tPrices','')
        name = request.POST.get('name', '')
        time = request.POST.get('time','')
        phone = request.POST.get('phone', '')
        status = request.POST.get('status', 'pending')
        order = Order(items_json=c, name=name, time=time, phone=phone, tprice=toprice, status=status)
        order.save()
        thank = True
        id = order.id
        return render(request, 'checkout.html', {'thank':thank, 'id':id})
    return render(request, 'checkout.html')



def cleanliness(request):
    form = cleanliness_form()
    if request.method =="POST":
        form = cleanliness_form(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'cleanliness.html',{'form':form})
    return render(request, 'cleanliness.html',{'form':form})


def event(request):
    complaint = Event.objects.all()
    return render(request, 'event.html', {'complaint': complaint})


def lostfound(request):
        form1 = lost_found_form()
        if request.method == "POST":
            form1 = lost_found_form(request.POST, request.FILES)
            if form1.is_valid():
                form1.save()
            return render(request, 'lost&found.html', {'form': form1})
        return render(request, 'lost&found.html', {'form': form1})


def view_cleanliness(request):
    complaint = cleanliness_model.objects.all()
    return render(request, 'view_cleanliness.html', {'complaint': complaint})

def viewcl(request):
    complaint = cleanliness_model.objects.all()
    return render(request, 'viewcl.html', {'complaint': complaint})

def view_canteen(request):
    ords = Order.objects.all()
    return render(request, 'view_canteen.html', {'ords': ords})


def view_lost(request):
    lost = lost_found_model.objects.all()
    return render(request, 'view_lost.html', {'lost': lost})

def viewl(request):
    lost = lost_found_model.objects.all()
    return render(request, 'viewl.html', {'lost': lost})


def update_cleanliness(request, id=0):
    form2 = cleanliness_model.objects.get(pk=id)
    if id == 0:
        form = cleanliness_form(request.POST)
    else:
        form2 = cleanliness_model.objects.get(pk=id)
        form = cleanliness_form(request.POST, request.FILES, instance=form2)
    if form.is_valid():
        form.save()
        return redirect('view_cleanliness')
    return render(request, "update_cleanliness.html", {'form2': form2})


def update_canteen(request, id=0):
    form2 = Order.objects.get(pk=id)
    if id == 0:
        form = Order(request.POST)
    else:
        form2 = Order.objects.get(pk=id)
        form = Order(request.POST, request.FILES, instance=form2)
    if form.is_valid():
        form.save()
        return redirect('view_canteen')
    return render(request, "update_canteen.html", {'form2': form2})


def delete(request, id):
    form3 = cleanliness_model.objects.get(pk=id)
    form3.delete()
    return redirect('view_cleanliness')


def update_lost(request, id=0):
    lost = lost_found_model.objects.get(pk=id)
    if id == 0:
        form = lost_found_form(request.POST)
    else:
        lost = lost_found_model.objects.get(pk=id)
        form = lost_found_form(request.POST, request.FILES, instance=lost)
    if form.is_valid():
        form.save()
        return redirect('view_lost')
    return render(request, "update_lost.html", {'form2': lost})


def delete_lost(request, id):
    form3 = lost_found_model.objects.get(pk=id)
    form3.delete()
    return redirect('view_lost')


def user_dashboard(request):
    return render(request, 'user_dashboard.html')


def registeruser(request):
    if request.method == "POST":
        name = request.POST.get('name')
        prn_number = request.POST.get('prn')
        password = request.POST.get('password')
        confirmpass = request.POST.get('confirm')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        email = request.POST.get('email')

        if password == confirmpass:
            if UserDetails.objects.filter(email=email).exists():
                messages.error(request, "Username exists, try new one")
            elif UserDetails.objects.filter(email=email).exists():
                messages.error(request, "Email exists, try new one")
            else:
                users = UserDetails(name=name, prn_number=prn_number, password=password,
                                    address=address, contact=contact, email=email)
                users.save()
                messages.success(request, "Successfully Registered")
                return redirect("/")
        else:
            messages.error(request, "Please Register Again")
            return redirect("/registeruser")

    return render(request, "index.html")


def loginuser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if UserDetails.objects.filter(email=email).exists():
            if UserDetails.objects.filter(password=password).exists():
                data = UserDetails.objects.get(email=email)
                request.session['email'] = data.name

                if data.role == "User":
                    return redirect("/user_dashboard")
                elif data.role == "Canteen_Staff":
                    return redirect("/canteen_dashboard")
                elif data.role == "CleanninessStaff":
                    return redirect("/cleanniness_dashboard")
                elif data.role == "LostFoundStaff":
                    return redirect("/lostfounddashboard")
                elif data.role == "EventStaff":
                    return redirect("/event_dashboard")
            else:
                messages.error(
                    request, "Email or Password is incorrect. Please enter the credentials again")
                return redirect("/")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='signin')
def logoutuser(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("/")


def cleanniness_dashboard(request):
    return render(request, "cleanniness_dashboard.html")


def canteen_dashboard(request):
    return render(request, "canteen_dashboard.html")


def lostfounddashboard(request):
    return render(request, "lost_found_dashboard.html")


def signin(request):
    return render(request, "loginpage.html")

def event_dashboard(request):
    return render(request, "event_dashboard.html")


def postevent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        prn_number = request.POST.get('prn')
        event_name = request.POST.get('ename')
        event_dest = request.POST.get('edest')
        max_crowd = request.POST.get('crowd')
        duration = request.POST.get('duration')

        if UserDetails.objects.filter(prn_number=prn_number).exists():
            event = EventDetails(name=name, prn_number=prn_number, event_name=event_name,
                                 event_dest=event_dest, max_crowd=max_crowd, duration=duration)
            event.save()
            request.session['eventname'] = event_name;
            request.session['eventdest'] = event_dest;
            request.session['name'] = name;
            request.session['duration'] = duration;

            return redirect("/")
        else:
            redirect("/event")



def contact(request):
    form2 = contact_form()
    if request.method == "POST":
        form2 = contact_form(request.POST)
        if form2.is_valid():
            form2.save()
        return redirect('/')
    return render(request, 'contact.html', {'form': form2})

#
#
# def update_canteen(request, id=0):
#     form2 = Order.objects.get(pk=id)
#     if id == 0:
#         form = Order_form(request.POST)
#     else:
#         form2 = cleanliness_model.objects.get(pk=id)
#         form = cleanliness_form(request.POST, request.FILES, instance=form2)
#     if form.is_valid():
#         form.save()
#         return redirect('view_cleanliness')
#     return render(request, "update_cleanliness.html", {'form2': form2})
