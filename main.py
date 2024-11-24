# import random
# from game_data import data


# def folowers_vs():
#     score=0
#     x = True
#     while x: 
        
#         A = random.choice(data)
#         B = random.choice(data)
#         print(f"{A['name']} vs {B['name']}")
#         vs = input('enter A/B ')
        

#         if vs == "A":
#             if A['follower_count'] >= B['follower_count']:
#                 score +=1
                             
#             else:
#                 x = False
                    
#         elif vs == 'B':
#             if A['follower_count'] <= B['follower_count']:
#                 score += 1
                    
#             else:
#                 x = False
#         return score    
            

                
        
# print(folowers_vs())
           
            
    
    
    
    
    
    
# from game_data import data
# import random
# import os


# def get_random_account():
#     '''random yntrum e dictionary'''
#     return random.choice(data)

# def format_data(account):
#     name = account['name']
#     description=account['description']
#     country=account['country']
#     return f'{name}, a {description}, from {country}'

# def check_answer(guess, a_followers,b_followers):
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"
    
    
# def game():
#     score = 0 
#     game_should_continue= True
#     account_a= get_random_account()
#     account_b= get_random_account()
#     while game_should_continue:
#         account_a = account_b
#         account_b = get_random_account()
        # while account_a == account_b:
        #       account_b = get_random_account()
            
        # print(f'compare A: {format_data(account_a)}.')
        # print("vs")
        # print(f'against B:{format_data(account_b)}.')
        
        # guess= input('who has more followers A or B ')
        # a_follower_count = account_a['follower_count']
        # b_follower_count = account_b['follower_count']
        # is_correct = check_answer(guess,a_follower_count,b_follower_count)
        
        
        # os.system('cls')
        
        # if is_correct:
        #     score +=1
        #     print(f"youre right {score}")
        # else:
        #     game_should_continue = False
        #     print(f'thats wrong {score}')
            
# game()

            
            

