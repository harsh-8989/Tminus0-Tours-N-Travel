from django.db import models

# Create your models here.


class user(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=35, unique=True, primary_key=True)
    password = models.CharField(max_length=20)


class location(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=2)
    country = models.CharField(max_length=2, default='US')


class attraction(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    location = models.ForeignKey(
        location, on_delete=models.CASCADE)

    # city = models.CharField(max_length=30, default='Stony Brook')
    attractionName = models.CharField(max_length=30)
    attractionDescription = models.CharField(max_length=1000)
    image = models.CharField(max_length=200)


class flight(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    departureTime = models.TimeField()
    sourceLocation = models.ForeignKey(
        location, on_delete=models.CASCADE, default=None, related_name="flight_source")
    destinationLocation = models.ForeignKey(
        location, on_delete=models.CASCADE, default=None, related_name="flight_destination")
    fareEconomy = models.DecimalField(max_digits=6, decimal_places=2)
    fareBusiness = models.DecimalField(max_digits=6, decimal_places=2)
    fareFirst = models.DecimalField(max_digits=6, decimal_places=2)
    numSeatsRemainingEconomy = models.IntegerField()
    numSeatsRemainingBusiness = models.IntegerField()
    numSeatsRemainingFirst = models.IntegerField()


class train(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    departureTime = models.TimeField()
    sourceLocation = models.ForeignKey(
        location, on_delete=models.CASCADE, default=None, related_name="train_source")
    destinationLocation = models.ForeignKey(
        location, on_delete=models.CASCADE, default=None, related_name="train_destination")
    fareEconomy = models.DecimalField(max_digits=6, decimal_places=2)
    fareBusiness = models.DecimalField(max_digits=6, decimal_places=2)
    fareFirst = models.DecimalField(max_digits=6, decimal_places=2)
    numSeatsRemainingEconomy = models.IntegerField()
    numSeatsRemainingBusiness = models.IntegerField()
    numSeatsRemainingFirst = models.IntegerField()


class booking(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    startDate = models.DateTimeField(auto_now=True)
    # TRANSPORTATION_TYPES = [('flight'), ('train')]
    Flight = models.ForeignKey(
        flight, on_delete=models.CASCADE, default=None)
    Train = models.ForeignKey(
        train, on_delete=models.CASCADE, default=None)


class review(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    rating = models.IntegerField()
    review = models.CharField(max_length=1000)
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    submissionDate = models.DateField(auto_now=True)


class payment(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    PAYMENT_TYPES = [('credit', 'Credit'), ('debit', 'Debit')]
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    paymentType = models.CharField(choices=PAYMENT_TYPES, max_length=6)
    cardNo = models.CharField(max_length=16)


class purchase(models.Model):
    transactionDate = models.DateTimeField(auto_now=True)
    userID = models.ForeignKey(user, on_delete=models.CASCADE)
    bookingID = models.ForeignKey(
        booking, on_delete=models.CASCADE)
    paymentID = models.ForeignKey(
        payment, on_delete=models.CASCADE)


class hotel(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    dailyCost = models.DecimalField(max_digits=6, decimal_places=2)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    companyName = models.CharField(max_length=30, default='hotel')
