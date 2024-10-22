from django.views.generic import doctor, Patient, Surgery

# Create your views here.
class doctorListView(ListView):
    model = doctor
    template_name = 'Doctors_list.html'
    context_object_name = "all_Doctors_list"