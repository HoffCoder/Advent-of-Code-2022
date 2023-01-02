# Rock:     A  = 1 point
# Paper:    B  = 2 points
# Scissors: C  = 3 points

# Win:  Z = 6
# Draw: Y = 3
# Lose: X = 0

def shoot(thiers, mine):
  # Modulo magic...
  return ((ord(thiers) + ord(mine) + 2) % 3 + 1) + ((ord(mine) - 88) * 3)

def main():
  score = 0
  guide = open('guide.txt', 'r')
  
  for line in guide:
    score += shoot(line[0],line[2])

  print("Final score following the guide: ", score)

if __name__ == "__main__":
  main()
