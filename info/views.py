from . import  models
from django.shortcuts import render
def index(request):
    data=models.skills.objects.all()
    professional_skills=models.professional_skills.objects.all()
    education=models.education.objects.all()
    skills=models.skills.objects.all()
    personal_info=models.personal_info.objects.all()
    skills_2=models.skills_2.objects.all()
    return render(request,template_name='info/index.html',context={"data":data,"professional_skills":professional_skills,"education":education,"skills":skills,"personal_info":personal_info,"skills_2":skills_2})
