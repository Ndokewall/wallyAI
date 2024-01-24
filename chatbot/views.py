from django.shortcuts import render,redirect

# create functions
def chatbot(request):
    if  not request.user.is_authenticated:
        return redirect('/login')
    
    elif request.user.is_authenticated:
        return redirect('chatbot')
    
    else: 
        return render(request,'chatbot.html')
