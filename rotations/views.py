# rotations/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Rotation
from .forms import RotationForm

@login_required
def rotation_list(request):
    qs = Rotation.objects.filter(user=request.user).order_by('-start_date')
    return render(request, 'rotations/list.html', {'rotations': qs})

@login_required
def add_rotation(request):
    if request.method == 'POST':
        form = RotationForm(request.POST)
        if form.is_valid():
            rot = form.save(commit=False)
            rot.user = request.user
            rot.save()
            return redirect('rotations:list')
    else:
        form = RotationForm()
    return render(request, 'rotations/add.html', {'form': form})
