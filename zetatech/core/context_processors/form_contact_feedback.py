from core.form import Form_Contact_Feedback
# Create your views here.

def form_contact_feedback(request):
    form = Form_Contact_Feedback()
    return  {'form_contact_feedback': form}