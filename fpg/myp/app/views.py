from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def array(request):
    context={
        "n": 35,
    }
    return render(request, 'array.html', context)

def backt(request):
    context={
        "n": 35,
    }
    return render(request, 'backtracking.html')

def bsearch(request):
    context={
        "n": 5,
    }
    return render(request, 'binarySearch.html')

def greedy(request):
    context={
        "n": 5,
    }
    return render(request, 'Greedy.html')

def llist(request):
    context={
        "n": 5,
    }
    return render(request, 'linked list.html')

def rec(request):
    context={
        "n": 5,
    }
    return render(request, 'recursion.html')

def heap(request):
    context={
        "n": 35,
    }
    return render(request, 'heap.html', context)

def stque(request):
    context={
        "n": 35,
    }
    return render(request, 'stque.html', context)

def str(request):
    context={
        "n": 35,
    }
    return render(request, 'str.html', context)

def bt(request):
    context={
        "n": 35,
    }
    return render(request, 'bt.html', context)

def dp(request):
    context={
        "n": 35,
    }
    return render(request, 'dp.html', context)


def bst(request):
    context={
        "n": 35,
    }
    return render(request, 'bst.html', context)

def grp(request):
    context={
        "n": 35,
    }
    return render(request, 'grp.html', context)

def trie(request):
    context={
        "n": 35,
    }
    return render(request, 'trie.html', context)
