# app/views.py
from django.shortcuts import render, redirect
from .models import Movie, Theater, Screening, Ticket
def home(request):
    return render (request , 'app/home.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'app/movie_list.html', {'movies': movies})

def theater_list(request):
    theaters = Theater.objects.all()
    return render(request, 'app/theater_list.html', {'theaters': theaters})

def screening_list(request):
    screenings = Screening.objects.all()
    return render(request, 'app/screening_list.html', {'screenings': screenings})

def book_tickets(request):
    screenings = Screening.objects.all()
    return render(request, 'app/book_tickets.html', {'screenings': screenings})

def confirm_booking(request):
    if request.method == 'POST':
        selected_screenings_ids = request.POST.getlist('selected_screenings')
        user_name = request.POST.get('user_name')

        for screening_id in selected_screenings_ids:
            screening = Screening.objects.get(id=screening_id)
            quantity = request.POST.get(f'quantity_{screening_id}', 0)
            
            # Check if the requested quantity is valid
            if 0 < int(quantity) <= screening.available_tickets:
                # Update the available_tickets field for the screening
                screening.available_tickets -= int(quantity)
                screening.save()

                # Create a new ticket entry
                Ticket.objects.create(user_name=user_name, screening=screening, quantity=int(quantity))

        # Redirect to a confirmation page or another relevant page
        return redirect('home')

    return redirect('book_tickets')

def booking_confirmation(request):
    tickets = Ticket.objects.all()
    return render(request, 'app/book_confirmation.html', {'tickets': tickets})


# cinema/views.py (Updated)
from django.shortcuts import render
from .models import Ticket

def all_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'app/all_tickets.html', {'tickets': tickets})


# cinema/views.py (Updated)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket

@login_required
def booked_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'cinema/all_tickets.html', {'tickets': tickets})
