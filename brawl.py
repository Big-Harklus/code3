import random
import time
import re

player_one = ""
player_two = ""
player_one_class = ""
player_two_class = ""
player_one_character = ""
player_two_character = ""

barbarian_max_lives = 100
gaint_max_lives = 300
magician_max_lives = 75
gnome_max_lives = 50
jonkler_max_lives = 200

player_one_lives = 0
player_two_lives = 0

player_one_attack = ""
player_two_attack = ""

player_one_damage = 0
player_two_damage = 0

player_one_choosing_character = False
player_two_choosing_character = False

current_round = 0
turns_played = 0
round_over = False
game_over = False

IsPlaying = False
RoundReset = True

current_players_turn = 0

barbarian_messages_fail1 = [
    'Men de råkar sparka deras vänster fot hårt in i en sten och trillar om kull skrikandes', 
    'Men de halkar och trillar på rumpan', 
    'Men de glömmer bort vad de tänkte göra']
barbarian_messages_fail2 = ['Men de missar totalt', 'Men det höll inte hårt nog i svärdet och råkar kasta iväg det åt sidan istället']
barbarian_messages_fail3 = ['Men de missade sin fiende totalt och landade så hårt på marken att de aggresivt sket på sig']

gaint_messages_fail1 = ['Men de missar totalt och slår marken istället', 'Men de halkar om kull just innan de ska kasta första slaget', 'Men de vill inte']
gaint_messages_fail2 = ['Men de kan inte lyfta sitt ben nog högt up', 'Men de glömde bort vad de skulle göra så de sänker sitt ben igen']
gaint_messages_fail3 = ['Men de tappar stenen i marken', 'Men stenen flög inte långt nog alls', 'Men stenen flög för långt']

magician_messages_fail1 = ['Men elden slocknar innan den hinner nå sitt mål', 'Men eldbollen flyger åt fel hål och tänder ett träd istället']
magician_messages_fail2 = ['Men det kommer ingen blixt', 'Det börjar regna istället', 'Men de trillar baklänges och råkar skicka blixten mot ett träd som fattar eld']
magician_messages_fail3 = ['Gargammel springer iväg', 'Gargammel vill inte strida, så han drar en fet fjärt innan han springer iväg', 'Gargammel dör']

gnome_messages_fail1 = ['Det är värdelöst']
gnome_messages_fail2 = ['Men de halkar omkull och slår huvudet hårt in i en sten']
gnome_messages_fail3 = ['Men det kommer ingen prutt', 'De råkar bajsa på sig lite']

jonkler_messages_fail1 = ['Ingenting händer']
jonkler_messages_fail2 = ['Ingenting händer']
jonkler_messages_fail3 = ['Raketen missar totalt och träffar av ett oskyldigt barn 30km bort', 'Raketen hinner epxlodera innan den når sitt mål', 'Raketen ändrar håll i luften och lyckas träffa av en polisstation']

def Attack(chosen_attack, attacking_player, character_class):
    attacker = ""
    defender = ""
    if attacking_player == 1:
        attacker = player_one
        defender = player_two
    else:
        attacker = player_two
        defender = player_one

    if chosen_attack != 4:
        dice_roll = random.randint(1,6)

        if dice_roll == 1:
            ##miss
            if chosen_attack == 1:
                if character_class == "1":
                    print(f"Efter ett mäktigt vrål russar {attacker} fram till {defender} och börjar våldsamt virva med armarna...")
                    time.sleep(3)
                    amount = len(barbarian_messages_fail1) - 1
                    random_message = random.randint(0, amount)

                    for i, v in enumerate(barbarian_messages_fail1):
                        if i == random_message:
                            print(v)
            if chosen_attack == 2:
                if character_class == "1":
                    print(f"{attacker} tar ett starkt grepp om sitt svärd och gör ett starkt hugg mot {defender}...")
                    time.sleep(3)
                    amount = len(barbarian_messages_fail2) - 1
                    random_message = random.randint(0, amount)

                    for i, v in enumerate(barbarian_messages_fail2):
                        if i == random_message:
                            print(v) 
            if chosen_attack == 3:
                if character_class == "1":
                    print(f"{attacker} börjar vråla väldigt högt och spänner sedan sina muskler aggresivt innan de slänger sig över {defender} som en galen björn...")
                    time.sleep(3)
                    amount = len(barbarian_messages_fail3) - 1
                    random_message = random.randint(0, amount)

                    for i, v in enumerate(barbarian_messages_fail3):
                        if i == random_message:
                            print(v)
            time.sleep(2)
            return 0
        elif dice_roll < 6:
            ##vanlig attack
            if chosen_attack == 1:
                if character_class == "1":
                    print(f"Efter ett mäktigt vrål russar {attacker} fram till {defender} och börjar våldsamt virva med armarna...")
                    time.sleep(3)
                    print(f'{defender} tar en fet haymaker till skallen')
            if chosen_attack == 2:
                if character_class == "1":
                    print(f"{attacker} tar ett starkt grepp om sitt svärd och gör ett starkt hugg mot {defender}...")
                    time.sleep(3)
                    print(f"{defender} blir huggen i benet")
            if chosen_attack == 3:
                if character_class == "1":
                    print(f"{attacker} börjar vråla väldigt högt och spänner sedan sina muskler aggresivt innan de slänger sig över {defender} som en galen björn...")
                    time.sleep(3)
                    print(f"{attacker} smäller skiten ur {defender}")
            time.sleep(2)
            return 1
        elif dice_roll == 6:
            ##kritisk skada
            if chosen_attack == 1:
                if character_class == "1":
                    print(f"Efter ett mäktigt vrål russar {attacker} fram till {defender} och börjar våldsamt virva med armarna...")
                    time.sleep(3)
                    print(f'{defender} tar en FET haymaker till skallen')
            if chosen_attack == 2:
                if character_class == "1":
                    print(f"{attacker} tar ett starkt grepp om sitt svärd och gör ett starkt hugg mot {defender}...")
                    time.sleep(3)
                    print(f"{defender} blir huggen i bröstet")
            if chosen_attack == 3:
                if character_class == "1":
                    print(f"{attacker} börjar vråla väldigt högt och spänner sedan sina muskler aggresivt innan de slänger sig över {defender} som en galen björn...")
                    time.sleep(3)
                    print(f"{attacker} börjar vildt slå, klösa och skära {defender}, det flyger blod överallt")
            time.sleep(2)
            return 2
        else:
            print("AGAGAGAGA")
            if character_class == "1":
                print(f"{attacker} tar fram en fet ölburk och klunkar hela grejen under 2 sekunder")
            elif character_class == "2":
                print(f"{attacker} bajsar våldsamt")
            elif character_class == "3":
                print(f"{attacker} tar fram en mysterisk flaska och dricker den magiska elixiren som finns inuti")
            elif character_class == "4":
                print(f"{attacker} skrattar arslet av sig")
            elif character_class == "5":
                print(f"{attacker} börja jonkla")
            time.sleep(2)
            return 3
    
    

while True:
    if RoundReset == True:
        RoundReset = False

        player_one = input("Spelare 1: ")
        player_one_class = input("Välj Klass: 1 = Barbarian, 2 = Jätte, 3 = Magiker, 4 = Tomtenisse, 5 = Jonkler: ")
        
        player_one_choosing_character = True
        while player_one_choosing_character == True:
            if player_one_class == "1":
                player_one_character = "Barbarian"
                player_one_lives = barbarian_max_lives
                player_one_choosing_character = False
            elif player_one_class == "2":
                player_one_character = "Jätte"
                player_one_lives = gaint_max_lives
                player_one_choosing_character = False
            elif player_one_class == "3":
                player_one_character = "Magiker"
                player_one_lives = magician_max_lives
                player_one_choosing_character = False
            elif player_one_class == "4":
                player_one_character = "Tomtenisse"
                player_one_lives = gnome_max_lives
                player_one_choosing_character = False
            elif player_one_class == "5":
                player_one_character = "Jonkler"
                player_one_lives = jonkler_max_lives
                player_one_choosing_character = False
            else:
                player_one_class = input("Felaktig Input, Välj Klass: 1 = Barbarian, 2 = Jätte, 3 = Magiker, 4 = Tomtenisse, 5 = Jonkler: ")

        player_two = input("Spelare 2: ")
        player_two_class = input("Välj Klass: 1 = Barbarian, 2 = Jätte, 3 = Magiker, 4 = Tomtenisse, 5 = Jonkler: ")

        player_two_choosing_character = True
        while player_two_choosing_character == True:
            if player_two_class == "1":
                player_two_character = "Barbarian"
                player_two_lives = barbarian_max_lives
                player_two_choosing_character = False
            elif player_two_class == "2":
                 player_two_character = "Jätte"
                 player_two_lives = gaint_max_lives
                 player_two_choosing_character = False
            elif player_two_class == "3":
                 player_two_character = "Magiker"
                 player_two_lives = magician_max_lives
                 player_two_choosing_character = False
            elif player_two_class == "4":
                 player_two_character = "Tomtenisse"
                 player_two_lives = gnome_max_lives
                 player_two_choosing_character = False
            elif player_two_class == "5":
                 player_two_character = "Jonkler"
                 player_two_lives = jonkler_max_lives
                 player_two_choosing_character = False
            else:
                 player_two_class = input("Felaktig Input, Välj Klass: 1 = Barbarian, 2 = Jätte, 3 = Magiker, 4 = Tomtenisse, 5 = Jonkler: ")

        print(f"{player_one}, en {player_one_character}, har valt att utmana")
        time.sleep(2)
        print(f"{player_two}, en {player_two_character}, i strid!")
        time.sleep(3)
        print("Må den bästa krigaren vinna!")
        time.sleep(1)
        game_over = False
        round_over = True
        current_round = 0
        IsPlaying = True

    while IsPlaying == True:
        if round_over == True and game_over == False:
            current_players_turn = random.randint(1, 2)
            round_over = False
            turns_played = 0
            current_round += 1
            time.sleep(2)
            print(f"Runda: {current_round}")
            time.sleep(2)
            print(f"{player_one}'s hälsa är {player_one_lives}")
            time.sleep(2)
            print(f"{player_two}'s hälsa är {player_two_lives}")
            time.sleep(2)
            if current_players_turn == 1:
                print(f"{player_one} börjar denna runda")
            else:
                print(f"{player_two} börjar denna runda")
            time.sleep(2)
            while round_over == False:
                if current_players_turn == 1 and game_over == False and round_over == False:
                    while current_players_turn == 1 and game_over == False and round_over == False:
                        if player_one_class == "1":
                            player_one_attack_input = input(f"{player_one} välj attack: 1 = Knyttnävar, 2 = Svärd, 3 = Inre Vrede, 4 = Drick Öl: ")
                        elif player_one_class == "2":
                            player_one_attack_input = input(f"{player_one} välj attack: 1 = Knyttnävar, 2 = Stampa Fot, 3 = Kasta Sten, 4 = Bajsa: ")
                        elif player_one_class == "3":
                            player_one_attack_input = input(f"{player_one} välj attack: 1 = Kasta eldboll, 2 = Kasta Blixt, 3 = Gargammel Spell, 4 = Drick Magisk Elixir: ")
                        elif player_one_class == "4":
                            player_one_attack_input = input(f"{player_one} välj attack: 1 = Hoppa, 2 = Spring, 3 = Prutta, 4 = Skratta: ")
                        elif player_one_class == "5":
                            player_one_attack_input = input(f"{player_one} välj attack: 1 = Sjung, 2 = Griddy, 3 = RPG, 4 = Jonkla: ")
                        if not re.search('[a-zA-Z]', player_one_attack_input):
                            player_one_attack = int(player_one_attack_input)
                            if player_one_attack <= 4 and player_one_attack > 0:
                                attack_result = Attack(player_one_attack, 1, player_one_class)
                                if attack_result == 0:
                                    print(f"{player_two} skrattar hånfullt mot {player_one}")
                                    time.sleep(2)
                                elif attack_result == 1:
                                    player_one_damage = 15
                                    player_two_lives -= player_one_damage
                                    print(f"{player_two} tar {player_one_damage} skada")
                                    time.sleep(2)
                                elif attack_result == 2:
                                    player_one_damage = 15 * 2
                                    player_two_lives -= player_one_damage
                                    print(f"{player_two} tar {player_one_damage} skada")
                                    time.sleep(2)
                                elif attack_result == 3:
                                    player_one_lives += 10
                                    print(f"{player_one}'s hälsa ökar med 10")
                                    time.sleep(2)
                                    if player_one_class == 1:
                                        if player_one_lives > barbarian_max_lives:
                                            player_one_lives = barbarian_max_lives
                                    elif player_one_class == 2:
                                        if player_one_lives > gaint_max_lives:
                                            player_one_lives = gaint_max_lives
                                    elif player_one_class == 3:
                                        if player_one_lives > magician_max_lives:
                                            player_one_lives = magician_max_lives
                                    elif player_one_class == 4:
                                        if player_one_lives > gnome_max_lives:
                                            player_one_lives = gnome_max_lives
                                    elif player_one_class == 5:
                                        if player_one_lives > jonkler_max_lives:
                                            player_one_lives = jonkler_max_lives
                                if player_two_lives <= 0:
                                    game_over = True
                                    round_over = True
                                else:
                                    if turns_played < 1:
                                        turns_played += 1
                                        current_players_turn = 2
                                    else:
                                        round_over = True
                            else:
                                print("Felaktig Input")
                                time.sleep(1)
                        else:
                            print("Felaktig Input")
                            time.sleep(1)

                if current_players_turn == 2 and game_over == False and round_over == False:
                    while current_players_turn == 2 and game_over == False and round_over == False:
                        if player_two_class == "1":
                            player_two_attack_input = input(f"{player_two} välj attack: 1 = Knyttnävar, 2 = Svärd, 3 = Inre Vrede, 4 = Drick Öl: ")
                        elif player_two_class == "2":
                            player_two_attack_input = input(f"{player_two} välj attack: 1 = Knyttnävar, 2 = Stampa Fot, 3 = Kasta Sten, 4 = Bajsa: ")
                        elif player_two_class == "3":
                            player_two_attack_input = input(f"{player_two} välj attack: 1 = Kasta eldboll, 2 = Kasta Blixt, 3 = Gargammel Spell, 4 = Drick Magisk Elixir: ")
                        elif player_two_class == "4":
                            player_two_attack_input = input(f"{player_two} välj attack: 1 = Hoppa, 2 = Spring, 3 = Prutta, 4 = Skratta: ")
                        elif player_two_class == "5":
                            player_two_attack_input = input(f"{player_two} välj attack: 1 = Sjung, 2 = Griddy, 3 = RPG, 4 = Jonkla: ")
                        if not re.search('[a-zA-Z]', player_two_attack_input):
                            player_two_attack = int(player_two_attack_input)
                            if player_two_attack <= 4 and player_two_attack > 0:
                                attack_result = Attack(player_two_attack, 2, player_two_class)
                                if attack_result == 0:
                                    print(f"{player_one} skrattar hånfullt mot {player_two}")
                                    time.sleep(2)
                                elif attack_result == 1:
                                    player_two_damage = 15
                                    player_one_lives -= player_two_damage
                                    print(f"{player_one} tar {player_two_damage} skada")
                                    time.sleep(2)
                                elif attack_result == 2:
                                    player_two_damage = 15 * 2
                                    player_one_lives -= player_two_damage
                                    print(f"{player_one} tar {player_two_damage} skada")
                                    time.sleep(2)
                                elif attack_result == 3:
                                    player_two_lives += 10
                                    print(f"{player_two}'s hälsa ökar med 10")
                                    if player_two_class == 1:
                                        if player_two_lives > barbarian_max_lives:
                                            player_two_lives = barbarian_max_lives
                                    elif player_two_class == 2:
                                        if player_two_lives > gaint_max_lives:
                                            player_two_lives = gaint_max_lives
                                    elif player_two_class == 3:
                                        if player_two_lives > magician_max_lives:
                                            player_two_lives = magician_max_lives
                                    elif player_two_class == 4:
                                        if player_two_lives > gnome_max_lives:
                                            player_two_lives = gnome_max_lives
                                    elif player_two_class == 5:
                                        if player_two_lives > jonkler_max_lives:
                                            player_two_lives = jonkler_max_lives
                                if player_one_lives <= 0:
                                    game_over = True
                                    round_over = True
                                else:
                                    if turns_played < 1:
                                        turns_played += 1
                                        current_players_turn = 1
                                    else:
                                        round_over = True
                            else:
                                print("Felaktig Input")
                                time.sleep(1)
                        else:
                            print("Felaktig Input")
                            time.sleep(1)
        elif round_over == True and game_over == True:
            IsPlaying = False
            print("Game Over")
            time.sleep(2)
            if player_one_lives <= 0:
                print(f"{player_two} vann!")
            else:
                print(f"{player_one} vann!")
            
            RoundReset = True