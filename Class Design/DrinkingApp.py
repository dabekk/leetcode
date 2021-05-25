# You were told to develop an app to store the amount of water that you have drunk per day. Customers can input the amount of water every time they drink it, the data need # to be store and reseted everyday. Can you implement a structure like this?

class DrinkingApp():
  def __init__(self):
    self.current_user = None
    self.liquid_required = 2000   # some default amount
    self.user_db    # some database which maintains all users - users can sign in to app. In the system design the DB will not be loaded into the app - users will verify and authenticate to sign in. This self.user_db is just to demonstrate.

  def sign_in(self, user):    # note in regular app there will be some authentication included
    # signs in user - set self.current_user to be input user. Also set required_liquid based on user.liquid_required

  def new_user_registration(self):
    # this will create a new user and place into self.user_db
    # if new user created - user automatically signed in

  def drink_liquid(self, beverage):   # user can enter the beverage they drunk
    # take in a beverage - type = "water", amount = "400ml"
    # update remaining required liquid i.e. decrement self.liquid_required

  def reset_liquid_required(self):    # run this every midnight local time
    # resets self.liquid_required to self.current_user.liquid_required

  def send_reminder(self):   # run a check every 3 hours to see if user is on their drinking goal
    # evaluate self.liquid_required throughout the day (waking hours) - if not enough water consumed - sent push notif
    # note: this is an optional functionality which will need permissions to send notificaitons

class Beverage():
  def __init__(self, type="water", amount):   # amount given in ml.
    self.type = type
    self.amount = amount

class User():
  def __init__(self, age, gender, weight=70, height=170):
    self.age = age
    self.gender = gender
    self.weight = weight
    self.height = height
    self.liquid_required = self.calculate_liquid_required(age, gender, weight, height)
    self.

  def calculate_liquid_required(self, age, gender, weight, height):   # note if the liquid is other than water e.g. green tea - may have to modify this func
    # calculate optimal liquid required based on inputs

# User Flow

# 1. User signs into the DrinkingApp or creates new account
# 2. User's liquid requirements calculated based on their user data e.g. weight, height etc.
# 3. User inputs what beverages they consume and in which quantity
# 4. As user inputs - their liquid requirement for rest of day decreases
# 5. At end of day - liquid required amount resets for the next day

# Expansions
# - preloaded list of beverages and quantities in the app for easy user input e.g. glass of water (300 ml) - user can click to select as opposed to manually input beverage
# - user can hold a progress chart (import some third party chart). Update the chart daily so they can track progress and water drinking over multiple days/weeks.
