# Sri GST Interiors — Django Website

## Setup (3 commands only)

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open: http://127.0.0.1:8000

## Admin Panel (optional)
```bash
python manage.py createsuperuser
```
Then go to: http://127.0.0.1:8000/admin
→ View and manage all customer enquiries here.

## How WhatsApp works
When a customer fills the quote form (page form OR popup modal) and clicks Submit:
1. Their data is saved to the database (viewable in admin)
2. WhatsApp opens automatically with their details pre-filled
3. The message is sent to +91 93945 43143

## Project Files
- core/templates/core/index.html  ← The full website (exact HTML, no changes)
- core/views.py                   ← Handles form POST + WhatsApp redirect
- core/models.py                  ← Enquiry model (name, phone, service, message)
- core/admin.py                   ← Admin panel for enquiries
