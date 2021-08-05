from django.shortcuts import render
from .forms import SymptomForm
from .classifier_files.makepred import predict

# Create your views here.

def home(request):
    print(" ******** ", request.method)
    post = False
    res = []
    sym = ""
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            sym1 = form.cleaned_data.get('symptom_1')
            sym2 = form.cleaned_data.get('symptom_2')
            sym3 = form.cleaned_data.get('symptom_3')
            sym4 = form.cleaned_data.get('symptom_4')
            sym5 = form.cleaned_data.get('symptom_5')
            sym = sym1+" ; "+sym2+" ; "+sym3+" ; "+sym4+" ; "+sym5
            sym1,sym2,sym3,sym4,sym5 = process_symptoms(sym1,sym2,sym3,sym4,sym5)

            res = predict([sym1+' '+sym2+' '+sym3+' '+sym4+' '+sym5])

            post = True
            form = SymptomForm()
            # response = render(request, 'users/register.html',
            #                   {'form': form, 'post': post, 'res': res})
            # return response
            #messages.success(request, f'{sym1}+{sym2}+{sym3} !')
            # return http.HttpResponseRedirect('.')
            # return redirect("blog_home")
    else:
        form = SymptomForm()

    return render(request, 'predictor/home.html', {'form':form, 'post':post, 'res':res, 'symptoms':sym})


def process_symptoms(*sym):
    tup = ()
    for i in sym:
        tup = tup + ('_'.join(i.split()),)
    return tup