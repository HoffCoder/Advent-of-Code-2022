def main():
  # Initialize Variables
  elf = 1
  calories = 0
  foods = []
  most = [0, 0, [0]]
  backup = [0, 0, [0]]
  backupsbackup = [0, 0, [0]]
  input = open('input.txt', 'r')

  # Read each line of the input file
  for line in input:
    # If line is empty
    if line.strip() == "":
      # Show information
      # print("Elf:",elf,"\nCalories:",calories,"\nFoods:",foods)
      # Update if new high calorie count
      if calories > most[1]:
        backupsbackup = backup
        backup = most
        most = [elf,calories,foods]
      elif calories > backup[1]:
        backupsbackup = backup
        backup = [elf,calories,foods]
      elif calories > backupsbackup[1]:
        backupsbackup = [elf,calories,foods]
      # Increment and reset logging information
      elf += 1
      calories = 0
      foods = []
      continue
    # Counting calories (I wish it was this easy...)
    calories += int(line)
    foods.append(int(line))
  # End of file, perform one last display and calorie check
  # print("Elf:",elf,"\nCalories:",calories,"\nFoods:",foods)
  if calories > most[1]:
    backupsbackup = backup
    backup = most
    most = [elf,calories,foods]
  elif calories > backup[1]:
    backupsbackup = backup
    backup = [elf,calories,foods]
  elif calories > backupsbackup[1]:
    backupsbackup = [elf,calories,foods]
  input.close()

  # Diplay infomation of elf with highest count
  # print(most)
  # print(backup)
  # print(backupsbackup)

  print(most[1] + backup[1] + backupsbackup[1])

if __name__ == "__main__":
  main()
