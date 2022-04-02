from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import authenticate

from .forms import *
from career.forms import *
from career.models import *
from product.models import *
from product.forms import *

def adminPanel(request, username):
    if request.user.username != username:
        print('//////////////////////////////////////////////////////////////////////////')
    
    try:
        user = User.objects.get(username=username)
    except:
        return redirect('login')
        
    
    context = {
        'admin': user
    }
    
    return render(request, 'admin_panel/index.html', context)    


def user_login(request):
    
    if request.user.is_authenticated:
        return redirect('admin-panel', request.user.username)
    else:
    
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                
                return redirect('admin-panel', user.username)
            else:
                messages.error(request, 'Login or password error')
    
    context = {
    }
    
    return render(request, 'admin_panel/login.html', context)    



def admin_vacancy(request):
    vacancies = Vacancy.objects.all().order_by('-updated_date')
    user = request.user
    careerInfo = Career.objects.all().first()
    
    careerForm = CareerForm(instance=careerInfo)

    vacancyForm = VacancyForm()
    dutiesForm = DutiesForm()
    skillsForm = SkillsForm()
    requirementsForm = RequirementsForm()
    prosForm = ProsForm()

    
    if request.POST:
        careerForm = CareerForm(request.POST or None, request.FILES or None, instance=careerInfo)

        vacancyForm = VacancyForm(request.POST, request.FILES)
        dutiesForm = DutiesForm(request.POST)
        skillsForm = SkillsForm(request.POST)
        requirementsForm = RequirementsForm(request.POST)
        prosForm = ProsForm(request.POST)
        
        print(DutiesForm(request.POST))
        print(SkillsForm(request.POST))
        print(RequirementsForm(request.POST))
        print(ProsForm(request.POST))


        if careerForm.is_valid():
            obj = careerForm.save(commit=False)
            obj.save()
            
            return redirect('admin-vacancy')
        
        if vacancyForm.is_valid():
            obj = vacancyForm.save(commit=False)
            obj.author = user
            obj.save()
            
            return redirect('admin-vacancy')
        
        if dutiesForm.is_valid():
            obj = dutiesForm.save(commit=False)
            obj.author = user
            obj.save()
            
            return redirect('admin-vacancy')
        
        if skillsForm.is_valid():
            obj = skillsForm.save(commit=False)
            obj.author = user
            obj.save()
            
            return redirect('admin-vacancy')
        
        if requirementsForm.is_valid():
            obj = requirementsForm.save(commit=False)
            obj.author = user
            obj.save()
            
            return redirect('admin-vacancy')
        
        if prosForm.is_valid():
            obj = prosForm.save(commit=False)
            obj.author = user
            obj.save()
            
            return redirect('admin-vacancy')
            
    
    context = {
        'vacancies': vacancies,
        'user': user,
        'careerForm': careerForm,
        'vacancyForm': vacancyForm,
        'dutiesForm': dutiesForm,
        'skillsForm': skillsForm,
        'requirementsForm': requirementsForm,
        'prosForm': prosForm,
    }
    return render(request, 'admin_panel/admin_vacancy.html', context)


# def vacancy_detail(request, id):
#     vacancy = Vacancy.objects.get(id=id)
    
#     context = {
#         'vacancy': vacancy,
#     }
    
#     return render(request, 'admin_panel/modal.html')


def delete_vacancy(request, id):
    vacancy = Vacancy.objects.get(id=id)
    
    vacancy.delete()
    
    return redirect('admin-vacancy')



def addAdmin(request):
    if request.user.username == 'admin':
        addAdminCreateForm = AddAdminCreateForm()

        if request.POST:
            addAdminCreateForm = AddAdminCreateForm(request.POST)
            
            if addAdminCreateForm.is_valid():
                obj = addAdminCreateForm.save(commit=False)
                obj.save()
                
                return redirect('login')
        
        context = {
        }
        
        return render(request, 'admin_panel/register.html', context)    
    else:
        return redirect('home')
    

def user_logout(request):
    logout(request)
    
    return redirect('login')


def profile(request, username):
    user = User.objects.get(username=username)

    editAdminForm = EditAdminForm(instance=user)
    
    if request.POST:
        editAdminForm = EditAdminForm(request.POST or None, request.FILES or None, instance=user)
        
        if editAdminForm.is_valid():
            obj = editAdminForm.save(commit=False)
            obj.save()
            
            user = User.objects.get(username=obj.username)
            
            return redirect('profile', user.username)
    
    context = {
        'user': user,
        'editAdminForm': editAdminForm,
    }
    
    return render(request, 'admin_panel/profile.html', context)

def editbrand(request, slug):
    brand =Brand.objects.get(slug=slug)
    brand_form = BrandForm(request.POST or None, request.FILES or None, instance=brand)

    if request.method == 'POST':
        brand_form = BrandForm(request.POST, request.FILES, instance=brand)

        if brand_form.is_valid():
            brand_form.save()
            return redirect('home', slug=slug)

    context = {
        'brand':brand,
        'brand_form':brand_form,
    }
    return render(request, 'admin_panel/chart.html', context)

def editproduct(request, slug):
    product = Products.objects.get(slug=slug)
    product_form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if request.method == 'POST':
        product_form = ProductForm(request.POST , request.FILES, instance=product)

        if product_form.is_valid():
            product_form.save()
            return redirect('home')


    context = {
        'product':product,
        'product_form':product_form,
    }
    return render(request, 'admin_panel/edit-product.html', context)

def admin_product(request):
    product = Products.objects.all().order_by('-id')

    context = {
        'product':product,
    }
    
    return render(request, 'admin_panel/admin-product.html', context)

def add_product(request):
    product_form = ProductForm()
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('home')
    context ={
        'product_form':product_form,
    }
    return render(request, 'admin_panel/add-product.html', context)

def delete_product(request, pk):
    product = Products.objects.get(id=pk)
    product.delete()
    return redirect('admin_product')