from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pickle
import os
from django.middleware.csrf import get_token
import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
nltk.download('stopwords')

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'model.sav')
model = pickle.load(open(filename, 'rb'))
vectorizer = pickle.load(open(os.path.join(dirname, 'vectorizer.sav'), 'rb'))

@csrf_exempt
def index(request):
    if(request.method == "POST"):
        try:
            text = json.loads(request.body)['text']
            vector = textprocess(text)
            result = model.predict(vector)
            if result[0]==0 :
                return JsonResponse({"result":"negative"})
            return JsonResponse({"result":"positive"}) 
        except Exception as e:
            print("An error occurred:", str(e))
            return HttpResponse("An error occurred")
    return JsonResponse({"token": get_token(request)})


def textprocess(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    ps = PorterStemmer()
    text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]
    text = ' '.join(text)
    text = [text]
    return vectorizer.transform(text)
    
def front(request):
    return render(request, 'index.html')