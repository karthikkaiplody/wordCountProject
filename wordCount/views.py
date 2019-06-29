from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return HttpResponse("Hello")

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    # to get the typed data from the user.
    fulltext = request.GET['fulltext']
    # printing the data which we have get from the user (will show in the terminal)
    #print (fulltext)
    # get the list of words in the user entered text.
    wordlist = fulltext.split()

    # to print the dict in the django you should first declare a dictionary.
    wordDict={}

    for word in wordlist:
        if word in wordDict:
            #increment
            wordDict[word] += 1
        else:
            #add to the dictionary
            wordDict[word] = 1

    sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist),'wordDict':wordDict,'sortedWords':sortedWords})

def cube(request):
    return HttpResponse("Rubiks Cube!")
