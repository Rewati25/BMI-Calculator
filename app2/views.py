from django.shortcuts import render
from .models import BMIRecord

def bmi_calculator(request):
    result = None
    category = None
    error = None

    if request.method == 'POST':
        name = request.POST.get('name')
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))

        if height <= 0 or weight <= 0:
            error = "Height and weight must be greater than zero."
        else:
            height_m = height/100
            bmi = round(weight/(height_m**2),2)
            
            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"
            BMIRecord.objects.create(
                name = name,
                weight = weight,
                height = height,
                bmi = bmi,
                category = category
            )
            result = bmi
    history = BMIRecord.objects.all().order_by('-created_at')[:5]

    return render(request, 'bmi.html', {
        'result' : result,
        'category' : category,
        'error' : error,
        'history' : history,
    })
# Create your views here.
