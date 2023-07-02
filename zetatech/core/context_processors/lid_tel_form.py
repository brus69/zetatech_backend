from core.form import Lid_Tel_Form

def lid_tel_form(request):
    form = Lid_Tel_Form()
    return  {'lid_tel_form': form}