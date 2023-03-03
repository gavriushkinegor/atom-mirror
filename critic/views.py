from django.shortcuts import render
from django.http import HttpResponse
import tensorflow as tf
import tensorflow_text as text

# load your model here

#reloaded_model = tf.saved_model.load("C:\\Users\\Raiden\\Desktop\\atom\\critic\\BigBert")


#def home(request):
#    if request.method == 'POST':
#        input_text = request.POST['input_text']
#        score = int(tf.sigmoid(reloaded_model(tf.constant(input_text)))[0]*9 + 1)
#        score = round(score)
#        context = {'input_text': input_text, 'score': score}
#        return render(request, 'home.html', context)
#    else:
#        return render(request, 'home.html')
from django.shortcuts import render
from django.http import HttpResponse
import tensorflow as tf
import tensorflow_text as text

# load your model here
reloaded_model = tf.saved_model.load("BigBert")
#input_signature = [{"input": reloaded_model.signatures['serving_default'].inputs[0]}]


def home(request):
    if request.method == 'POST':
        input_text = request.POST['input_text']
        try:
            input_text = tf.constant([input_text])
            score = int(tf.sigmoid(reloaded_model(input_text).numpy()[0][0]) * 9 + 1)
            score = round(score)
            context = {'input_text': input_text.numpy()[0].decode(), 'score': score}
            return render(request, 'home.html', context)
        except ValueError as e:
            error_message = f"Could not evaluate the review: {str(e)}"
            context = {'error_message': error_message}
            return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')
    
