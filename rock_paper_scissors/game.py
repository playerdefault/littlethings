import engine, os

if os.name == 'nt':
    os.system('cls')
elif os.name == 'posix':
    os.system('clear')

## game banner
print(r"""
         _    _      _                            _         
         | |  | |    | |                          | |        
         | |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___   
         | |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  
         \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | 
          \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  
          ______           _     ______                       
          | ___ \         | |    | ___ \                      
          | |_/ /___   ___| | __ | |_/ /_ _ _ __   ___ _ __   
          |    // _ \ / __| |/ / |  __/ _` | '_ \ / _ \ '__|  
          | |\ \ (_) | (__|   <  | | | (_| | |_) |  __/ |     
          \_| \_\___/ \___|_|\_\ \_|  \__,_| .__/ \___|_|     
           _____      _                    | |                
           /  ___|    (_)                   |_|                
           \ `--.  ___ _ ___ ___  ___  _ __ ___                
            `--. \/ __| / __/ __|/ _ \| '__/ __|               
            /\__/ / (__| \__ \__ \ (_) | |  \__ \               
            \____/ \___|_|___/___/\___/|_|  |___/               
                                                                
                                                                                                                    


        """)

user_input = input("Rock(0), Paper(1), Scissor(2)?: ")
if (int(user_input) in [0,1,2]) == False:
    print("Please enter 0 for Rock, 1 for Paper, or 2 for Scissor. The game will now exit. \n")
    exit()

result = engine.main(int(user_input))

if result == True:
    print("You win!")
elif result == False:
    print("You lose!")
elif result == None:
    print("It's a draw!")
