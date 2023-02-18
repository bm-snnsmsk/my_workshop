from django.shortcuts import render
from django.http import HttpResponse  ## HttpResponse 'ı import ettik

# Create your views here.

def index(request) :
    ## return HttpResponse("<div ><h2>This is a heading in a div element</h2><p>This is some text in a div element.</p></div>")
    return render(request,"pages/index.html")  ## templates klasörüne git ordan pages klasörüne git orda index.html dosyasını getir

def about(request) :
    ## return HttpResponse("<div ><h2>Bu sayfa ikinci eklediğim saydfaadır</h2><p>Byu sayfa eklediğim 2. bir sayfadır</p></div>")
    return render(request,"pages/about.html")  ## templates klasörüne git ordan pages klasörüne git orda about.html dosyasını getir
