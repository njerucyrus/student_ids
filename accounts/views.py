from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from accounts.forms import  *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from payments.models import Payment


def index(request):
    return render(request, 'accounts/index.html', {})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    request.session['username'] = cd['username']
                    user_instance = User.objects.get(username=cd['username'])
                    profile = Profile.objects.get(user=user_instance)
                    request.session['regNo'] = str(profile.regNo)
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:

                    message = "Your Account has been disabled. Contact Admin"
                    return render(request, 'login.html', {'message': message, })
            else:
                message = 'Wrong username or username'
                return render(request, 'login.html', {'message': message, })
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form, })


def user_logout(request):
    logout(request)
    try:
        del request.session['username']
        del request.session['regNo']
        request.session.modified = True
        return render(request, 'logout_then_login.html', {})
    except KeyError:
        pass
    return render(request, 'accounts/logout_then_login.html', {})


def create_account(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = StudentProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            # create profile
            cd = profile_form.cleaned_data
            school_name = cd['school']
            department_name = cd['department']
            course_name = cd['course']
            school = School.objects.get(school_name=school_name)
            department = Department.objects.get(department_name=department_name)
            course = Course.objects.get(course_name=course_name)

            profile = Profile.objects.create(
                user=new_user,
                phoneNumber=cd['phoneNumber'],
                regNo=cd['regNo'],
                national_id=cd['national_id'],
                school=school,
                department=department,
                course=course
            )
            profile.save()

            return HttpResponse('ACCOUNT CREATED SUCCESSFULLY')
    else:
        user_form = UserRegistrationForm()
        profile_form = StudentProfileForm()
    return render(request, 'accounts/create_account.html', {'user_form': user_form,
                                                   'profile_form': profile_form,
                                                   })

@login_required(login_url="/login/")
def apply_id(request):

    if request.method == 'POST':
        form = ApplyIdForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                username = request.session['username']
                regNo = request.session['regNo']
                payment = Payment.objects.get(regNo=regNo)
                status = str(payment.status).lower()
                if status == 'success':

                    user = User.objects.get(username=username)

                    application = IdApplication.objects.create(
                        user=user,
                        application_type=form.cleaned_data['application_type'],
                        passport=form.cleaned_data['passport']
                    )
                    application.save()
                    return HttpResponse('application was successful')
                else:
                    return HttpResponseRedirect('/make-payment/')
            except KeyError, e:
                pass
    else:
        form = ApplyIdForm()
    return render(request, 'accounts/apply_id.html', {'form': form, })










