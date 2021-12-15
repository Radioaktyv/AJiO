from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, Dish
from .forms import CreateNewList, CreateNewDish


# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "AJiO/list.html", {"ls": ls})


def home(response):
    return render(response, "AJiO/home.html", {})


def create(response):
    test = ToDoList.objects.values_list()
    dishes = Dish.objects.values_list()

    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            for id, name, description, price in dishes:
                amount = int(response.POST.get("p" + str(id)))
                txt = name
                for x in range(amount):
                    ToDoList.objects.get(id=t.id).item_set.create(text=txt, complete=False)

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "AJiO/create.html", {"form": form, "dishes": dishes})


def NoIdOrders(response):
    test = ToDoList.objects.values_list()
    if response.method == "POST":
        if response.POST.get("delete"):
            for x, y in test:
                if response.POST.get("c" + str(x)) == "clicked":
                    ToDoList.objects.filter(id=x).delete()
                    # print(del_order)
                    test = ToDoList.objects.values_list()
    return render(response, "AJiO/orders.html", {"test": test})


def menu(response):
    dishes = Dish.objects.values_list()
    print(dishes)
    if response.method == "POST":
        form = CreateNewDish(response.POST)
        if response.POST.get("save"):
            if form.is_valid():
                n = form.cleaned_data["name"]
                d = form.cleaned_data["description"]
                p = form.cleaned_data["price"]
                if n is not None and d is not None and p is not None:
                    t = Dish(name=n, description=d, price=p)
                    t.save()

        if response.POST.get("delete"):
            for id, name, description, price in dishes:
                if response.POST.get("c" + str(id)) == "clicked":
                    Dish.objects.filter(id=id).delete()
                    # print(del_order)
                    dishes = Dish.objects.values_list()
        return HttpResponseRedirect("/menu")

    else:
        form = CreateNewDish()
    return render(response, "AJiO/menu.html", {"form": form, "dishes": dishes})


def EditMenu(response, id):
    edit = Dish.objects.get(id=id)

    if response.method == "POST":
        if response.POST.get("save"):
            name = response.POST.get("name")
            description = response.POST.get("description")
            price = response.POST.get("price")
            if len(name)>2 and len(description)>2 and float(price) > 0:
                name = str(name)
                t = Dish(id=id, name=name, description=description, price=price)
                t.save()

        if response.POST.get("delete"):
            pass
        return HttpResponseRedirect("/menu/" + str(id))

    else:
        form = CreateNewDish()
    return render(response, "AJiO/editmenu.html", {"edit": edit})

def IdOrders(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid input")
    return render(response, "AJiO/idorders.html", {"ls": ls})