from django.shortcuts import render, HttpResponse
from accounts.forms import  *


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
    return render(request, 'create_account.html', {'user_form': user_form,
                                                   'profile_form': profile_form,
                                                   })



