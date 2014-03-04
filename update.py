
import os
os.environ['DJANGO_SETTINGS_MODULE'] = "goodliner.settings"

from quotes.models import quote
import json


def transfertodb():
    currentCount = quote.objects.count()
    print "\n\nUPDATING 'quote' DATABASE:\n"
    print "Quote objects in database: %s" %( currentCount )
    
    if currentCount == 0:
        currentCount = 1

    qfile = json.load( open("quotes.json") )
    
    for q in qfile["quotes"]:
        dataquote = quote(
            content = q["content"],
            respos = q["respos"],
            resneg = q["resneg"],
            quotetype = q["quotetype"]
        )
        dataquote.save()
        print "quote..%s" %(currentCount)
        currentCount += 1
     
    print "\nUpdating COMPLETE!\n"

if __name__ == '__main__':
    transfertodb()