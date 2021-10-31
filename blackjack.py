import random
import matplotlib.pyplot as plt

class Deck:
   
    cards_list = []
   
    def __init__(self, num_decks):
        self.cards_list.clear()
        for i in range (0, 4*num_decks):
            for j in range(2, 12):
                self.cards_list.append(j)
            for j in range(0, 3):
                self.cards_list.append(10)
        self.shuffle()
               
    def shuffle(self):
        random.shuffle(self.cards_list)
       
    def show_deck(self):
        return self.cards_list
       
    def deal_card(self):
        return self.cards_list.pop()

    def remaining_cards(self):
        return len(self.cards_list)
       

class Dealer:
   
    dealer_hand = []
    dealer_show_card = 0
    dealer_sum = 0
   
    def __init__(self, deck):
        self.dealer_hand.clear()
        self.dealer_show_card = deck.deal_card()
        card2 = deck.deal_card()
        self.dealer_hand.append(self.dealer_show_card)
        self.dealer_hand.append(card2)
        self.dealer_sum = self.dealer_sum + self.dealer_show_card + card2
   
    def dealer_hit(self, deck):
        card = deck.deal_card()
        self.dealer_hand.append(card)
        self.dealer_sum = self.dealer_sum + card
       
    def get_dealer_show_card(self):
        return self.dealer_show_card
       
    def get_dealer_sum(self):
        return self.dealer_sum
   
    def get_dealer_hand(self):
        return self.dealer_hand
   
    def dealer_action(self, deck, action):
        if action == "H":
            self.dealer_hit(deck)
       
       
class Player:
   
    player_hand = []
    player_sum = 0
    raw_player_sum = 0
   
    def __init__(self, deck, money_pool):
        self.player_hand.clear()
        card1 = deck.deal_card()
        card2 = deck.deal_card()
        self.player_hand.append(card1)
        self.player_hand.append(card2)
        self.player_sum = self.player_sum + card1 + card2
        self.raw_player_sum = self.raw_player_sum + card1 + card2
        money_pool.place_bet()
       
    def player_hit(self, deck):
        card = deck.deal_card()
        self.player_hand.append(card)
        self.player_sum = self.player_sum + card
        self.raw_player_sum = self.raw_player_sum + card

    def player_double(self, deck, money_pool):
        if money_pool.get_total_amount() >= 1:
            self.player_hit(deck)
            money_pool.double()
       
    def get_player_hand(self):
        return self.player_hand
   
    def get_raw_player_sum(self):
        return self.raw_player_sum
   
    def get_player_sum(self):
        num_ace_in_hand = 0
        for card in self.player_hand:
            if card == 11:
                num_ace_in_hand += 1
        for i in range (0, num_ace_in_hand + 1):
            if self.raw_player_sum - 10*i <= 21:
                self.player_sum = self.raw_player_sum - 10*i
        return self.player_sum

    def player_action(self, deck, money_pool, action, move_num):
        #print(action)
        if self.get_player_sum() == 21:
            action = "S"
        else:
            if move_num != 0:
              if action == "Ds":
                action = "S"
              elif action == "D":
                action = "H"
              else:
                action = action
            if action == "H":
              self.player_hit(deck)
            elif action == "D":
              self.player_double(deck, money_pool)
            elif action == "Ds":
              self.player_double(deck, money_pool)
        #print(action)

class Money_Pool:

    amount = 0
    current_bet = 0

    def __init__(self, starting_amount):
        self.amount = starting_amount
        self.current_bet = 0
   
    def place_bet(self):
        self.amount -= 1
        self.current_bet = 1

    def double(self):
        self.amount -= 1
        self.current_bet += 1

    def win(self):
        self.amount += self.current_bet*2
        self.current_bet = 0
   
    def tie(self):
        self.amount += self.current_bet
        self.current_bet = 0

    def lose(self):
        self.current_bet = 0

    def get_total_amount(self):
        return self.amount

def dealer_logic(dealer_sum, dealer_hand):
    num_ace_in_hand = 0
    for card in dealer_hand:
      if card == 11:
        num_ace_in_hand += 1
    for i in range (1, num_ace_in_hand + 1):
      if dealer_sum < 17:
        return "H"
      elif dealer_sum >= 17 and dealer_sum <= 21:
        return "S"
      elif dealer_sum - 10*i <= 21 and dealer_sum - 10*i >= 17:
        return "S"
    if dealer_sum - 10*num_ace_in_hand < 17:
      return "H"
    else:
      return "S"

def lookup_table(player_hand, player_sum, dealer_upcard):
    row = dealer_upcard - 2
    column = 21 - player_sum
    if column < 0:
        return "S"
    if player_sum == 21:
        return "S"
    if (11 in player_hand) and (player_sum in [13, 14, 15, 16, 17, 18, 19, 20]):
            table = [["S", "S", "S", "Ds", "H", "H", "H", "H", "H"],
                    ["S", "S", "S", "Ds", "D", "H", "H", "H", "H"],
                    ["S", "S", "S", "Ds", "D", "D", "D", "H", "H"],
                    ["S", "S", "S", "Ds", "D", "D", "D", "D", "D"],
                    ["S", "S", "Ds", "Ds", "D", "D", "D", "D", "D"],
                    ["S", "S", "S", "S", "H", "H", "H", "H", "H"],
                    ["S", "S", "S", "S", "H", "H", "H", "H", "H"],
                    ["S", "S", "S", "H", "H", "H", "H", "H", "H"],
                    ["S", "S", "S", "H", "H", "H", "H", "H", "H"],
                    ["S", "S", "S", "H", "H", "H", "H", "H", "H"]]
    else:
            table = [["S", "S", "S", "S", "S", "S", "S", "S", "S", "H", "D", "D", "H", "H", "H", "H", "H", "H", "H", "H"],
                    ["S", "S", "S", "S", "S", "S", "S", "S", "S", "H", "D", "D", "D", "H", "H", "H", "H", "H", "H", "H"],
                    ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "D", "D", "D", "H", "H", "H", "H", "H", "H", "H"],
                    ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "D", "D", "D", "H", "H", "H", "H", "H", "H", "H"],
                    ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "D", "D", "D", "H", "H", "H", "H", "H", "H", "H"],
                    ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H", "D", "D", "H", "H", "H", "H", "H", "H", "H", "H"],
                    ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H", "D", "D", "H", "H", "H", "H", "H", "H", "H", "H"],
                    ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H", "D", "D", "H", "H", "H", "H", "H", "H", "H", "H"],
                    ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H", "D", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
                    ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H", "D", "H", "H", "H", "H", "H", "H", "H", "H", "H"]]
    return table[row][column]








def run_game(money_pool):
  deck = Deck(2)
  player = Player(deck, money_pool)
  dealer = Dealer(deck)
  player_state = ""
  dealer_state = ""
  move_num = 0
  #force_quit = 30
  action_list = []
  while player_state != "S":
      player_state = lookup_table(player.get_player_hand(), player.get_player_sum(), dealer.get_dealer_show_card())
      if move_num != 0:
              if player_state == "Ds":
                player_state = "S"
              elif player_state == "D":
                player_state = "H"
      action_list.append(player_state)
      player.player_action(deck, money_pool, player_state, move_num)
      move_num += 1
     
  #print("player sum = ", player.get_player_sum())
  #print("raw player sum =", player.get_raw_player_sum())
  #print("Player hand:", player.get_player_hand())
  while dealer_state != "S" and (player.get_player_sum() <= 21 and len(player.get_player_hand()) >= 2):
      dealer_state = dealer_logic(dealer.get_dealer_sum(), dealer.get_dealer_hand())
      dealer.dealer_action(deck, dealer_state)
  #print("dealer sum =", dealer.get_dealer_sum())
  #print("dealer hand:", dealer.get_dealer_hand())
  if player.get_player_sum() <= 21 and player.get_player_sum() > dealer.get_dealer_sum() and dealer.get_dealer_sum() <= 21:
      money_pool.win()
      result = 'win'
  elif player.get_player_sum() <= 21 and dealer.get_dealer_sum() > 21:
      money_pool.win()
      result = 'win'
  elif player.get_player_sum() == dealer.get_dealer_sum() and player.get_player_sum() <= 21:
      money_pool.tie()
      result = 'tie'
  else:
      money_pool.lose()
      result = 'lose'
  print("money_remaining =", money_pool.get_total_amount())
  print()
  return money_pool.get_total_amount(), result, action_list

starting_balance = 1000
money_pool = Money_Pool(starting_balance)
running_total = [starting_balance]
run_num = 0
run_num_list = [0]
num_win = 0
num_tie = 0
num_lose = 0
cap = 14000000
double_down_count = 0
double_down_success = 0
while money_pool.get_total_amount() != 0 and run_num <= cap:
    run_num += 1
    run_num_list.append(run_num)
    money_left, result, action_list = run_game(money_pool)
    running_total.append(money_left)
    if result == 'win':
      num_win += 1
    if result == 'tie':
      num_tie += 1
    if result == 'lose':
      num_lose += 1
    if result == 'win' and (action_list[0] == 'D' or action_list[0] == 'Ds'):
        double_down_count += 1
        double_down_success += 1
    if result != 'win' and (action_list[0] == 'D' or action_list[0] == 'Ds'):
        double_down_count += 1


print("Win Percent: ", num_win / run_num)
print("Tie Percent: ", num_tie / run_num)
print("Loss Percent: ", num_lose / run_num)
print("Double Down Win Percent: ", double_down_success / double_down_count)
print("Starting Balance:", starting_balance)
print("Final balance:", money_pool.get_total_amount())
print("Total games played: ", cap)
    #plt.plot(run_num_list, running_total)
    #plt.show()
plt.plot(run_num_list, running_total)
plt.show()