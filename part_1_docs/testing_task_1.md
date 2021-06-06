### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:   
      # it should be card.value == 1
      return True
    else
    # else is missing colon "else:"
      return False
   

  dif highest_card(self, card1 card2):
  # a class function attributes are separated by "," i.e (self, card1, card2)
  # a function in python is defined with "def"
  if card1.value > card2.value:
    return card
    # it should be return card1
  else:
    return card2
  


def cards_total(self, cards):
  # function needs to be indented
  # total variable need to be assigned a value e.g total = 0
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  #  string interpolation starts with f" You have a total of + total" and variable should be inclosed in curly brackets {total} so the correct format should be return f"You have a total of {total}"
```
