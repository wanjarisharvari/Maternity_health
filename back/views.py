import os
import joblib
import numpy as np
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Load model (Ensure model.pkl is in the correct path)
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = joblib.load(MODEL_PATH)

@csrf_exempt  # Not recommended in production; use Django's CSRF protection
def index(request):
    if request.method == 'POST':
        try:
            # Extract and convert inputs
            age = float(request.POST.get('age', 0))
            systolicBp = float(request.POST.get('systolicBp', 0))
            diastolicbp = float(request.POST.get('diastolicbp', 0))
            bloodsugar = float(request.POST.get('bloodsugar', 0))
            bodytemp = float(request.POST.get('bodytemp', 0))
            heartrate = float(request.POST.get('heartrate', 0))

            # Create input array
            a = np.array([[age, systolicBp, diastolicbp, bloodsugar, bodytemp, heartrate]])

            # Make prediction
            result = model.predict(a)[0]  # Get first value

            # Render corresponding template
            if result == 'high risk':
                return render(request, 'High.html')
            elif result == 'mid risk':
                return render(request, 'mid.html')
            else:
                return render(request, 'low.html')

        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=400)

    return render(request, 'kot.html')
