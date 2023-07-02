from core.form import FeedbackForm
# Create your views here.

def modal_form(request):
    form = FeedbackForm()
    return  {'modal_form': form}