from django.shortcuts import render
from django.http import JsonResponse
from .models import Enquiry, ProjectImage, Review
import urllib.parse

MANAGER_NAME = 'manager'
MANAGER_PASSWORD = 'srigst143'


def home(request):
    project_images = ProjectImage.objects.filter(is_active=True)[:12]
    reviews = Review.objects.filter(is_active=True)[:6]
    return render(request, 'core/index.html', {
        'project_images': project_images,
        'reviews': reviews,
    })


def founders(request):
    return render(request, 'core/founders.html')


def contact(request):
    preselect = request.GET.get('service', '')
    return render(request, 'core/contact.html', {'preselect': preselect})


def enquiry(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Invalid method.'})
    name = request.POST.get('name', '').strip()
    phone = request.POST.get('phone', '').strip()
    service = request.POST.get('service', '').strip()
    message = request.POST.get('message', '').strip()
    if not name or not phone:
        return JsonResponse({'success': False, 'error': 'Name and phone are required.'})
    try:
        Enquiry.objects.create(name=name, phone=phone, service=service, message=message)
    except Exception:
        pass
    wa_lines = ["Hi Sri GST Interiors! 👋", "I'd like to get a free quote.", "",
                f"*Name:* {name}", f"*Phone:* {phone}"]
    if service:
        wa_lines.append(f"*Service:* {service}")
    if message:
        wa_lines.append(f"*Message:* {message}")
    wa_lines += ["", "Please get back to me. Thank you!"]
    wa_url = "https://wa.me/919394543143?text=" + urllib.parse.quote("\n".join(wa_lines))
    return JsonResponse({'success': True, 'wa_url': wa_url})


def manager_login(request):
    if request.method == 'POST':
        name = request.POST.get('manager_name', '').strip()
        password = request.POST.get('manager_password', '').strip()
        if name == MANAGER_NAME and password == MANAGER_PASSWORD:
            request.session['is_manager'] = True
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Invalid credentials'})
    return JsonResponse({'success': False, 'error': 'Invalid method'})


def manager_logout(request):
    request.session.pop('is_manager', None)
    return JsonResponse({'success': True})


def manager_upload(request):
    if not request.session.get('is_manager'):
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)
    if request.method == 'POST':
        title = request.POST.get('title', 'Recent Project').strip()
        image = request.FILES.get('image')
        if not image:
            return JsonResponse({'success': False, 'error': 'No image provided'})
        proj = ProjectImage.objects.create(title=title, image=image)
        return JsonResponse({'success': True, 'url': proj.image.url, 'title': proj.title, 'id': proj.id})
    return JsonResponse({'success': False, 'error': 'Invalid method'})


def manager_photos(request):
    if not request.session.get('is_manager'):
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)
    photos = ProjectImage.objects.filter(is_active=True)
    data = [{'id': p.id, 'url': p.image.url, 'title': p.title} for p in photos]
    return JsonResponse({'success': True, 'photos': data})


def manager_delete(request):
    if not request.session.get('is_manager'):
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)
    if request.method == 'POST':
        img_id = request.POST.get('id')
        try:
            proj = ProjectImage.objects.get(id=img_id)
            proj.delete()
            return JsonResponse({'success': True})
        except ProjectImage.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Not found'})
    return JsonResponse({'success': False, 'error': 'Invalid method'})


def manager_review(request):
    if not request.session.get('is_manager'):
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        location = request.POST.get('location', 'Bhimavaram').strip()
        text = request.POST.get('text', '').strip()
        stars = request.POST.get('stars', '★★★★★')
        if not name or not text:
            return JsonResponse({'success': False, 'error': 'Name and text required'})
        Review.objects.create(name=name, location=location, text=text, stars=stars)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid method'})
