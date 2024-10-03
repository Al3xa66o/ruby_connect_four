require_relative 'player.rb'

class GameBoard
  attr_accessor :board, :player1, :player2, :turn_count, :moves

  def initialize(name1 = 'Player 1', name2 = 'Player 2')
    @board = Array.new(7) { Array.new(6, ' ') }
    @player1 = Player.new(name1, '⚪')
    @player2 = Player.new(name2, '⚫')
    @turn_count = 1
    @moves = [1, 2, 3, 4, 5, 6, 7]
  end


  def play
    display_board
    turns
  end
  

  def display_board
    display_string = "\n"

    5.downto(0) do |row|
      display_string << "+---+---+---+---+---+---+---+\n"
      0.upto(6) do |column|
        display_string << "| #{@board[column][row]} "
      end
      display_string << "|\n"
    end

    display_string << "+---+---+---+---+---+---+---+\n"
    display_string << '  1   2   3   4   5   6   7'

    puts display_string
  end

  def turns
    won = false
    until @turn_count > 42 || won
      turn 
      @turn_count += 1
      display_board
      won = check_win
    end
    won ? win : draw
  end

  def turn
    player = @turn_count.even? ? @player2 : @player1
    chosen_column = player.take_turn(@moves) - 1
    add_coin(player, chosen_column)
  end

  def add_coin(player, column)
    i = 0
    until @board[column][i] == ' '
      i += 1
    end
    @board[column][i] = player.coin
    @moves.delete(column + 1) if i == 5
  end

  def check_win
    return true if check_diagonal || check_horizontal || check_vertical
    false
  end

  def check_horizontal
    0.upto(5) do |y|
      0.upto(3) do |x|
        return true if @board[x][y] != ' ' && @board[x][y] == @board[x + 1][y] && @board[x + 1][y] == @board[x + 2][y] && @board[x + 2][y] == @board[x + 3][y]
      end
    end
    false
  end

  def check_vertical
    0.upto(6) do |x|
      0.upto(2) do |y|
        return true if @board[x][y] != ' ' && @board[x][y] == @board[x][y + 1] && @board[x][y + 1] == @board[x][y + 2] && @board[x][y + 2] == @board[x][y + 3]
      end
    end
    false
  end

  def check_diagonal
    0.upto(3) do |x|
      0.upto(2) do |y|
        return true if @board[x][y] != ' ' && @board[x][y] == @board[x + 1][y + 1] && @board[x + 1][y + 1] == @board[x + 2][x + 2] && @board[x + 2][y + 2] == @board[x + 3][x + 3]
      end

      3.upto(5) do |y|
        return true if @board[x][y] != ' ' && @board[x][y] == @board[x + 1][y - 1] && @board[x + 1][y - 1] == @board[x + 2][x - 2] && @board[x + 2][y - 2] == @board[x + 3][y - 3]
      end
    end
    false
  end

  def win
    winner = @turn_count.even? ? @player1.name : @player2.name
    puts "gg #{winner}"

  end

  def draw
    puts "it's a draw better luck next time"
  end
end
