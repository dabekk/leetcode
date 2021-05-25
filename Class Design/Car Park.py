# Assumptions:
# - the system will have 1 type of parking spot - regular sized car
# - there will be 2 types of terminals - enter and exit
# - we will take payment for the parking at moment of exit (if car has been in car park for less than 15 mins - no fee)
# - there will not be a specific parking assignment i.e. you enter car park - you will park anywhere you want/is free

class CarPark():
  self.terminals = []
  def __init__(self, number_of_spaces, number_of_entrances)   # entrances will always have an exit also
    self.free_spaces = number_of_spaces
    self.number_of_entrances = self.create_terminals(number_of_entrances)

  def create_terminals(self, number_of_entrances):
    # initialize all the terminals as per number_of_entrances

  def display_free_spaces_left(self):
    # display number of free spaces left - user feedback so they no if there are spaces left before they approach


class Terminal:
  def __init__(self):

  def update_free_spaces():
    # increment/decrement number of free spaces

class EntryTerminal(Terminal):
  def __init__(self):

  def provide_ticket(self):
    # provide a parking ticket

  def allow_car(self):

  def update_free_spaces(self):
    # override inherited class to decrement free spaces
    # if there are no spaces left - do not allow car in

import payment_processing as payments
import datetime as time

class ExitTerminal(Terminal):
  def __init__(self):


  def calculate_fee(self, ticket):
    # accept a ticket and calculate fee
    # payments.calculate_fee(ticket.entrance_time, time.current_time, ticket.rate_per_hour)   # if time is less than 15, no fee
    # self.accept_payment(amount)

  def accept_payment(self, amount):
    # accept payment and provide change

  def update_free_spaces(self):
    # override inherited class to increment free spaces

  def no_ticket_emergency(self):    # this should be initiated by user via no_ticket button on ExitTerminal
    # charges user penalty fee for lost ticket - this can be decided

class Ticket:
  def __init__(self, entrance_time, rate_per_hour, penalty_fee):  # penalty_fee in case of lost ticket.
    self.entrance_time = entrance_time
    self.rate_per_hour = rate_per_hour

# Notes:

# 1. User approaches car park entrance terminal
# 2. Terminal issues a ticket (ticket notes the time of entry and rate per hour) - free spaces left updates
# 3. User parks car wherever they wish
# 4. User leaves car park through exit terminal
# 5. Exit terminal accepts parking ticket and charges user at moment of exit - free spaces left updates. IF no ticket - penalty charge applied
# 6. User leaves

# Bonus: number of free spaces left displayed by the car park to inform incoming drivers.
