# Rock:     A or X = 1 point
# Paper:    B or Y = 2 points
# Scissors: C or Z = 3 points

def shoot(thiers, mine):
  # Modulo magic...
  return 6 - 3 * ((ord(thiers) - ord(mine)) % 3) + ord(mine) - 87

def main():
  score = 0
  guide = open('guide.txt', 'r')
  
  for line in guide:
    score += shoot(line[0],line[2])

  print("Final score following the guide: ", score)

if __name__ == "__main__":
  main()
