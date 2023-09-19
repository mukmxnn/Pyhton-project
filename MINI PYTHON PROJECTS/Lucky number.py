import random 


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

while True:
    players = input("Sila masukkan bilangan pemain (2-4): ")
    if players.isdigit():
        players = int(players)
        if  2 <= players <= 4:
            
            break
        else:
            print("Nombor mestilah antara 2 - 4 pemain ")
    else:
        print("Tidak sah, cuba lagi")

max_score = 50
player_scores = [0 for i in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPemain nombor",player_idx + 1,"bermula\n")
        print("Jumlah skor anda ialah:",player_scores[player_idx],"\n")
        current_score = 0

        while True:
           should_roll = input("Adakah anda ingin meneruskan? ketik (y) jika ingin meneruskan: ")
           if should_roll.lower() != "y":
               break

           value = roll()
           if value == 1:
              print("Skor anda = 1, giliran selesai")
              current_score = 0 
              break
           else:
              current_score += value
              print("Nombor anda =", value)

           print("Skor terkini ialah", current_score)

        player_scores[player_idx] += current_score
        print("Jumlah skor anda ialah: ",player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("\nPemain nombor", winning_idx + 1,"adalah pemenang dengan skor sebanyak:",max_score)

