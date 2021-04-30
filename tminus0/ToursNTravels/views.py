from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from developer.models import user_admin
from django.shortcuts import redirect
import jwt
import json
import datetime

from ToursNTravels.models import *
numreview = len(review.objects.all())
user_email = None

numbooking = len(booking.objects.all())
numpayment = len(payment.objects.all())


@csrf_exempt
def index(request):
    return render(request, 'index.html')


def change_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        oldpassword = request.POST['oldPassword']
        newpassword = request.POST['newPassword']
        try:
            auth = user_admin.objects.get(email=email)
        except user_admin.DoesNotExist:
            auth = None
        if auth is not None:
            try:
                auth = user_admin.objects.get(
                    email=email, password=oldpassword)
            except user_admin.DoesNotExist:
                auth = None
            if auth is not None:
                user_admin.objects.filter(email=email).update(
                    password=newpassword
                )
                return render(request, 'login.html', {'msg': 'Password Changed Successfully'})
            else:
                return render(request, 'change_pass.html', {'msg': 'Password Changed UnSuccessful'})
        check_user = user.objects.filter(email=email, password=oldpassword)
        valid_user = (len(list(check_user)) == 1)
        if (valid_user):
            current_user = email
            # user_name = check_user.first().username
            user.objects.filter(email=email).update(
                password=newpassword
            )
            return render(request, 'login.html', {'msg': 'Password Changed Successfully'})
        else:
            return render(request, 'change_pass.html', {'msg': 'Password Changed UnSuccessful'})
            # request.session['current_user'] = current_user
            # request.session['user_name'] = user_name

    return render(request, 'change_pass.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        try:
            auth = user_admin.objects.get(email=email)
        except user_admin.DoesNotExist:
            auth = None
        if auth is not None:
            try:
                auth = user_admin.objects.get(email=email, password=password)
            except user_admin.DoesNotExist:
                auth = None
            if auth is not None:
                check_user = user_admin.objects.filter(email=email)
                current_user = email
                user_name = check_user.first().username
                request.session['current_user'] = current_user
                request.session['user_name'] = user_name
                return render(request, 'developer/index.html')
            else:
                return render(request, 'login.html')
        check_user = user.objects.filter(email=email, password=password)
        valid_user = (len(list(check_user)) == 1)
        if (valid_user):
            current_user = email
            user_name = check_user.first().username
            request.session['current_user'] = current_user
            request.session['user_name'] = user_name
            #encoded = jwt.encode(payload, secret, algorithm='HS256')
            return redirect('explore')
            # return render(request, 'explore.html', {'msg': 'Login successful'})
        else:
            return render(request, 'login.html', {'msg': 'Failed. Please try again'})
    else:
        return render(request, 'login.html')


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(request.POST)
        existing_email = user.objects.filter(email=email)
        is_new_user = (len(list(existing_email)) == 0)
        print(is_new_user)
        if (is_new_user):
            new_user = user.objects.create(
                username=username, email=email, password=password)
            new_user.save()
            return render(request, 'signup.html', {'msg': 'Sign up successful'})
        else:
            return render(request, 'signup.html', {'msg': 'Error. Email already exists'})
    else:
        return render(request, 'signup.html')


@csrf_exempt
def reviews(request):
    global numreview

    if request.method == 'POST':
        Review = request.POST['review']
        rating = request.POST['rating']
        author = request.session['current_user']
        author = user.objects.get(email=author)
        current_date = datetime.datetime.today().strftime('%Y-%m-%d')
        user_exists = review.objects.filter(author=author)
        # if (len(list(user_exists)) == 0):
        numreview = int(len(review.objects.all()))+1
        print(review)
        new_review = review.objects.create(id=numreview,
                                           review=Review, rating=rating, submissionDate=current_date, author=author)
        reviews = review.objects.all()

        return render(request, 'reviews.html', {'results': 'yes', 'some_list': reviews})
    else:
        reviews = review.objects.all()
        return render(request, 'reviews.html', {'results': 'yes', 'some_list': reviews})


@csrf_exempt
def hotels(request):
    if request.method == 'POST':
        Location = request.POST['location']
        # locationArr = location.split(',')
        locationCity = Location
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        hotels = hotel.objects.filter(city=locationCity)
        hotels = list(hotels)
        return render(request, 'hotels.html', {"results": "yes", "some_list": hotels})
    else:
        return render(request, 'hotels.html')


@csrf_exempt
def trains(request):
    if request.method == 'POST':
        source = request.POST['source']
        destination = request.POST['destination']
        startdate = request.POST['startdate']
        startdate = startdate.split('-')
        year = int(startdate[0])
        month = int(startdate[1])
        day = int(startdate[2])
        trainClass = request.POST['class']
        print(request.POST)
        trains = train.objects.filter(sourceLocation=source).filter(
            destinationLocation=destination).filter(departureDate=datetime.date(year, month, day))
        trains = list(trains)
        if (trainClass == 'economy'):
            trains = train.objects.filter(sourceLocation=source).filter(destinationLocation=destination).filter(
                departureDate=datetime.date(year, month, day)).filter(numSeatsRemainingEconomy__gt=0)
            trains = list(trains)
            return render(request, 'trains.html', {"results": "yes", "some_list": trains, "class": trainClass})
        elif (trainClass == 'business'):
            trains = train.objects.filter(sourceLocation=source).filter(destinationLocation=destination).filter(
                departureDate=datetime.date(year, month, day)).filter(numSeatsRemainingBusiness__gt=0)
            trains = list(trains)
            return render(request, 'trains.html', {"results": "yes", "some_list": trains, "class": trainClass})
        else:
            trains = train.objects.filter(sourceLocation=source).filter(destinationLocation=destination).filter(
                departureDate=datetime.date(year, month, day)).filter(numSeatsRemainingFirst__gt=0)
            trains = list(trains)
            return render(request, 'trains.html', {"results": "yes", "some_list": trains, "class": trainClass})
    else:
        return render(request, 'trains.html')


@csrf_exempt
def flights(request):
    if request.method == 'POST':
        source = request.POST['source']
        destination = request.POST['destination']
        startdate = request.POST['startdate']
        startdate = startdate.split('-')
        year = int(startdate[0])
        month = int(startdate[1])
        day = int(startdate[2])
        flightClass = request.POST['class']
        print(request.POST)
        flights = flight.objects.filter(sourceLocation=source).filter(
            destinationLocation=destination).filter(departureDate=datetime.date(year, month, day))
        flights = list(flights)
        if (flightClass == 'economy'):
            flights = flight.objects.filter(sourceLocation=source).filter(destinationLocation=destination).filter(
                departureDate=datetime.date(year, month, day)).filter(numSeatsRemainingEconomy__gt=0)
            flights = list(flights)
            return render(request, 'flights.html', {"results": "yes", "some_list": flights, "class": flightClass})
        elif (flightClass == 'business'):
            flights = flight.objects.filter(sourceLocation=source).filter(destinationLocation=destination).filter(
                departureDate=datetime.date(year, month, day)).filter(numSeatsRemainingBusiness__gt=0)
            flights = list(flights)
            return render(request, 'flights.html', {"results": "yes", "some_list": flights, "class": flightClass})
        else:
            flights = flight.objects.filter(sourceLocation=source).filter(destinationLocation=destination).filter(
                departureDate=datetime.date(year, month, day)).filter(numSeatsRemainingFirst__gt=0)
            flights = list(flights)
            return render(request, 'flights.html', {"results": "yes", "some_list": flights, "class": flightClass})
    else:
        return render(request, 'flights.html')


@csrf_exempt
def explore(request):
    if request.method == 'POST':
        Location = request.POST['location']
        city = Location
        Location = location.objects.filter(city=city)
        temp = location.objects.get(city=city)
        Attraction = attraction.objects.filter(location=temp)
        Location = list(Location)
        return render(request, 'explore.html', {"results": "yes", "location": Location, "some_list": Attraction})
    else:
        return render(request, 'explore.html')


@csrf_exempt
def myadmin(request):
    if request.method == 'POST':
        location = request.POST['location']
        locationArr = location.split(',')
        city = locationArr[0]
        region = locationArr[1]
        Location = location.objects.filter(city=city)
        Attraction = attraction.objects.filter(city=city)
        location = list(location)
        return render(request, 'myadmin.html', {"results": "yes", "location": location, "some_list": attraction})
    else:
        return render(request, 'myadmin.html')


def print_invoice(request):
    purchase_ = purchase.objects.all()
    return render(request, 'developer/print.html', {'transactions': purchase_})


def book(request):
    global numbooking
    global numpayment
    if request.method == 'POST':
        new_transaction = None
        objId = request.GET.get('id')
        bookType = request.GET.get('type')
        card_number = request.POST['card_number']
        card_type = request.POST['card_type']
        current_user = request.session['current_user']
        current_user = user.objects.get(email=current_user)

        current_date = datetime.datetime.today().strftime('%Y-%m-%d')

        if (bookType == 'flight'):
            travelClass = request.GET.get('class')

            if (travelClass == 'economy'):
                numbooking = len(booking.objects.all())+1
                numpayment = len(payment.objects.all())+1
                flight_ = flight.objects.get(id=objId)
                booking_ = booking.objects.create(id=numbooking,
                                                  startDate=current_date, Flight=flight_)
                payment_ = payment.objects.create(id=numpayment,
                                                  paymentType=card_type, amount=flight_.fareEconomy, cardNo=card_number)
                flight.objects.filter(id=objId).update(
                    numSeatsRemainingEconomy=flight_.numSeatsRemainingEconomy-1)
                new_purchase = purchase.objects.create(Type=travelClass,
                                                       userID=current_user, transactionDate=current_date, bookingID=booking_, paymentID=payment_)
                new_transaction = new_purchase
                new_purchase.save()
            elif (travelClass == 'business'):
                numbooking = len(booking.objects.all())+1
                numpayment = len(payment.objects.all())+1
                flight_ = flight.objects.get(id=objId)
                # train_ = train.objects.get(id=1000)
                booking_ = booking.objects.create(id=numbooking,
                                                  startDate=current_date, Flight=flight_)
                payment_ = payment.objects.create(id=numpayment,
                                                  paymentType=card_type, amount=flight_.fareBusiness, cardNo=card_number)
                flight.objects.filter(id=objId).update(
                    numSeatsRemainingBusiness=flight_.numSeatsRemainingBusiness-1)
                new_purchase = purchase.objects.create(Type=travelClass,
                                                       userID=current_user, transactionDate=current_date, bookingID=booking_, paymentID=payment_)
                new_transaction = new_purchase
                new_purchase.save()
            elif (travelClass == 'first'):
                numbooking = len(booking.objects.all())+1
                numpayment = len(payment.objects.all())+1
                flight_ = flight.objects.get(id=objId)
                # train_ = train.objects.get(id=1000)
                booking_ = booking.objects.create(id=numbooking,
                                                  startDate=current_date, Flight=flight_)
                payment_ = payment.objects.create(id=numpayment,
                                                  paymentType=card_type, amount=flight_.fareFirst, cardNo=card_number)
                flight.objects.filter(id=objId).update(
                    numSeatsRemainingFirst=flight_.numSeatsRemainingFirst-1)
                new_purchase = purchase.objects.create(Type=travelClass,
                                                       userID=current_user, transactionDate=current_date, bookingID=booking_, paymentID=payment_)
                new_transaction = new_purchase
                new_purchase.save()
        elif (bookType == 'train'):
            travelClass = request.GET.get('class')
            obj = train.objects.filter(id=objId).first()
            if (travelClass == 'economy'):
                numbooking = len(booking.objects.all())+1
                numpayment = len(payment.objects.all())+1
                # flight_ = flight.objects.get(id=1000)
                train_ = train.objects.get(id=objId)
                booking_ = booking.objects.create(id=numbooking,
                                                  startDate=current_date,  Train=train_)
                payment_ = payment.objects.create(id=numpayment,
                                                  paymentType=card_type, amount=train_.fareEconomy, cardNo=card_number)
                train.objects.filter(id=objId).update(
                    numSeatsRemainingEconomy=train_.numSeatsRemainingEconomy-1)
                new_purchase = purchase.objects.create(Type=travelClass,
                                                       userID=current_user, transactionDate=current_date, bookingID=booking_, paymentID=payment_)
                new_transaction = new_purchase
                new_purchase.save()
            elif (travelClass == 'business'):
                numbooking = len(booking.objects.all())+1
                numpayment = len(payment.objects.all())+1
                # flight_ = flight.objects.get(id=1000)
                train_ = train.objects.get(id=objId)
                booking_ = booking.objects.create(id=numbooking,
                                                  startDate=current_date, Train=train_)
                payment_ = payment.objects.create(id=numpayment,
                                                  paymentType=card_type, amount=train_.fareBusiness, cardNo=card_number)
                train.objects.filter(id=objId).update(
                    numSeatsRemainingBusiness=train_.numSeatsRemainingBusiness-1)
                new_purchase = purchase.objects.create(Type=travelClass,
                                                       userID=current_user, transactionDate=current_date, bookingID=booking_, paymentID=payment_)
                new_transaction = new_purchase
                new_purchase.save()
            elif (travelClass == 'first'):
                numbooking = len(booking.objects.all())+1
                numpayment = len(payment.objects.all())+1
                # flight_ = flight.objects.get(id=1000)
                train_ = train.objects.get(id=objId)
                booking_ = booking.objects.create(id=numbooking,
                                                  startDate=current_date,  Train=train_)
                payment_ = payment.objects.create(id=numpayment,
                                                  paymentType=card_type, amount=train_.fareFirst, cardNo=card_number)
                train.objects.filter(id=objId).update(
                    numSeatsRemainingFirst=train_.numSeatsRemainingFirst-1)
                new_purchase = purchase.objects.create(Type=travelClass,
                                                       userID=current_user, transactionDate=current_date, bookingID=booking_, paymentID=payment_)
                new_transaction = new_purchase
                new_purchase.save()
        elif (bookType == 'hotel'):
            numbooking = len(booking.objects.all())+1
            numpayment = len(payment.objects.all())+1
            # flight_ = flight.objects.get(id=1000)
            hotel_ = hotel.objects.get(id=objId)
            booking_ = booking.objects.create(id=numbooking,
                                              startDate=current_date, Hotel=hotel_)
            payment_ = payment.objects.create(id=numpayment,
                                              paymentType=card_type, amount=(hotel_.dailyCost), cardNo=card_number)
            # train.objects.filter(id=objId).update(
            #     numSeatsRemainingBusiness=train_.numSeatsRemainingBusiness-1)
            new_purchase = purchase.objects.create(
                userID=current_user, transactionDate=current_date, bookingID=booking_, paymentID=payment_)
            new_transaction = new_purchase
            new_purchase.save()
        return render(request, 'book.html', {'msg': 'Booking successful', 'obj': new_transaction})
    else:
        objId = request.GET.get('id')
        bookType = request.GET.get('type')
        if (bookType == 'flight'):
            travelClass = request.GET.get('class')
            obj = flight.objects.filter(id=objId)
            return render(request, 'book.html', {'booking': 'yes', 'some_list': obj, 'type': bookType, 'class': travelClass})
        elif (bookType == 'train'):
            travelClass = request.GET.get('class')
            obj = train.objects.filter(id=objId)
            return render(request, 'book.html', {'booking': 'yes', 'some_list': obj, 'type': bookType, 'class': travelClass})
        elif (bookType == 'hotel'):
            obj = hotel.objects.filter(id=objId)
            return render(request, 'book.html', {'booking': 'yes', 'some_list': obj, 'type': bookType})
        else:
            return render(request, 'book.html')


def account(request):
    setting = request.GET.get('setting')
    current_user = request.session['current_user']
    user_ = user.objects.get(email=current_user)

    if (setting == 'history'):
        History = purchase.objects.filter(userID=user_)
        return render(request, 'account.html', {'setting': setting, 'transactions': History})
    else:
        return render(request, 'account.html', {'setting': setting})


def logout(request):
    # clear session
    user_email = None
    del request.session['current_user']
    del request.session['user_name']
    return render(request, 'index.html', {'msg': 'Logout successful'})
