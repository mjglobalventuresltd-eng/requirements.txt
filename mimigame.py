Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> customer_name = "Milia Jay"
>>> number_of_passes = 3
>>> tokens_per_pass = 30
>>> price_per_pass = 15.00
>>> token_required_per_game = 3
>>> # calculations
>>> total_tokens = number_of_passes * tokens_per_pass
>>> total_cost = number_of_passes * price_per_pass
>>> games_available = total_tokens // token_required_per_game
>>> print ("customer:", customer_name)
customer: Milia Jay
>>> print ("passes:", number_of_passes)
passes: 3
>>> print ("tokens:", total_tokens)
tokens: 90
>>> print ("total cost : $" + str(total_cost))
total cost : $45.0
>>> print ("games availiable: " + str(games_available))
games availiable: 30
