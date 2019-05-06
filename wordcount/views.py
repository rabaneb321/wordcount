from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'home.html')
def eggs(request):
    return HttpResponse("<h1>EGGS LOVE ME</h1>")

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    word_dictionary={}
    for word in wordlist:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add word_dictionary
            word_dictionary[word]=1
    sorted_words=sorted(word_dictionary.items(), key=operator.itemgetter(1),reverse=True)


    return render(request,'count.html', {'fulltext':fulltext,'count':len(wordlist),'sorted_words':sorted_words})
