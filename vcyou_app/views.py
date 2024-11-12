from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.conf import settings
import os
import joblib
from django.views.decorators.csrf import csrf_protect
from ml_models.ml_model import ExecuteJobLib

def index(request):
    return render(request, 'index.html')

@csrf_protect
def form(request):
    if request.method == 'POST':
        try:
            company_name = request.POST.get('companyName', '')
            funding_rounds = float(request.POST.get('fundingRounds', 0))
            funding_total_usd = float(request.POST.get('fundingTotalUSD', 0))
            funding_period_year = float(request.POST.get('fundingPeriodYear', 0))
            business_domain = float(request.POST.get('businessDomain', 0))

            if funding_rounds < 0 or funding_total_usd < 0 or funding_period_year < 0:
                raise ValueError("Invalid input values")

            model_path = os.path.join(settings.ML_MODELS_DIR, 'VCYou.joblib')
            if not os.path.exists(model_path):
                return JsonResponse({'error': 'Model not found'}, status=500)

            prediction = ExecuteJobLib(
                funding_rounds, 
                funding_period_year, 
                funding_total_usd, 
                business_domain
            )
            
            context = {
                'prediction': bool(prediction[0]),
                'company_name': company_name
            }
            return render(request, 'pred.html', context)

        except (ValueError, TypeError) as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Internal server error'}, status=500)

    return render(request, 'form.html')
  
