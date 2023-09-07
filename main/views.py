from django.shortcuts import render
def show_main(request):
    context = {
        'name': 'Andika Pramudya Wardana',
        'class': 'KKI'
    }

    return render(request, 'main.html', context)