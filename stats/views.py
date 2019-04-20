from django.shortcuts import render

def get_stats(request):
    context = {
        
    }
    return render(request, 'stats/stats.html', context)
