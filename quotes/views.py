from django.shortcuts import render
from django.http import HttpResponse
from quotes.models import quote

import random

# Create your views here.

def makeHash(num):
   return hex(num + 1000)[2:]
 
def deHash(num):
   return int("0x" + str(num), 16 ) - 1000


def randomQuote(request):
    r = random.randrange(1, quote.objects.count())
    randomQuote = quote.objects.get(pk = r)
     
    quoteIdHash = makeHash(r)
    #randomQuote = "Hello how are you"
    #quoteIdHash = "ec2"
    #if request.is_ajax():

     
    return render(request, "quotes/singleQuote.html", \
           {"singleQuote": randomQuote, \
            "quoteIdHash": quoteIdHash,  \
            "title": "Random Inspirational Quotes for You!"})
 
def getQuote(request, qHash):
    q = None
    print "qhash:", qHash
     
    try:
       i = deHash(qHash)
       print "i = ", i
        
       if i >= quote.objects.count() or i <= 0:
          pass
       else: 
          q = quote.objects.get(pk = i)
    except:
       pass

    print q
        
    return render(request, "quotes/singleQuote.html", \
      {"singleQuote": q, \
       "quoteIdHash": qHash, \
       "title": "Random Inspirational Quotes for You!"})

def incrementQuote(request):
     if request.is_ajax():
        quoteHash = request.GET.get("qHash")
        print quoteHash
        q = quote.objects.get(pk = deHash(quoteHash))

        print "Incrementing quote:", q.content
        print "q.likes:", q.likes
        q.likes += 1
        print "q.likes:", q.likes
        q.save()

        return HttpResponse("Quote Updated")
