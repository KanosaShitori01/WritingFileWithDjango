from django.shortcuts import render
from django.core.files import File
# Create your views here.
def writingFiles(request):
    if request.method == 'POST': 
        text = request.POST['text']
        file = open(r"D:\Program File (K.N)\GitHub\Back-End\Python\django\wrfile\acti\files\text.txt", "w")
        writeFile = File(file)
        writeFile.write(text)
        file.close()
        print(file)
    return render(request, "index.html", {})