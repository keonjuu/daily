# 5 21
# 5 6 7 8 9
import sys

def blackjack(n,m,card)
  maxCard = 0
  for c1 in range(n-2):
    for c2 in range(c1+1, n-1):
      for c3 in range(c2+1, n):
        if maxCard == m: return maxCard 
        if card[c1]+card[c2]+card[c3]==m and maxCard<(card[c1] +card[c2] +card[c3]):
            maxCard = card[c1] +card[c2] +card[c3]

  return maxCard 

n,m = map(int, sys.stdin.readline().split()) 
card = list(map(int, sys.stdin.readline().split())) 
print(blackjack(n,m,card))
