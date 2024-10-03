require_relative 'board.rb'

def get_name(player_number, stdin= $stdin)
  print "enter your name, player #{player_number}?\n> "
  stdin.gets.chomp
end

def new_game(name1 = 'Player 1', name2 = 'Player 2')
  GameBoard.new(name1, name2)
end

def play_game(stdin = $stdin, stdin2 = $stdin)
  name1 = get_name(1, stdin)
  name2 = get_name(2, stdin2)
  game = new_game(name1, name2)
  game.play
  
end

play_game