from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from testapp.models import Student,Subject,SubmitWorks,Work
from django.db.models import Q

def filt_submited_works(submited:bool,filt_subject_id,filt_assign_date,
                        filt_sent,filt_teacher,filt_std_id):
    filt_res = SubmitWorks.objects.filter(
            work=Work.objects.filter(assign_datetime = filt_assign_date),
            subject=Subject.objects.filter(
                Q(
                    subject_id=filt_subject_id,
                    submit_datetime=filt_sent
                ) & Q(
                    Q(teacher1=filt_teacher)|
                    Q(teacher2=filt_teacher)
                )
            ),student=Student.objects.filter(
                id=filt_std_id
            )
        )
    if submited: return filt_res
    else:
        return Work.objects.exclude(
            Q(topic=filt_res.work.topic)
        )

@csrf_exempt
def index(request:HttpRequest):
    filt_subject_id = request.GET.get("subjectid","")
    filt_assign_date = request.GET.get("assign_date","")
    filt_sent = request.GET.get("sent","")
    filt_std_id = request.GET.get("studentid","")
    filt_teacher = request.GET.get("teacher","")
    return render(request,"index.html",{
        "submited_works":SubmitWorks.objects.filter(
            work=Work.objects.filter(assign_datetime = filt_assign_date),
            subject=Subject.objects.filter(
                Q(
                    subject_id=filt_subject_id,
                    submit_datetime=filt_sent
                ) & Q(
                    Q(teacher1=filt_teacher)|
                    Q(teacher2=filt_teacher)
                )
            ),student=Student.objects.filter(
                id=filt_std_id
            )
        ),
        "unsubmited_works":Work.objects.filter(

        ),
        "subjects":Subject.objects.all(),
        "students":Student.objects.all(),
        "works":Work.object.all()
    })

