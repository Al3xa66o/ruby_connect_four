class Player
  attr_accessor :name, :coin 

  def initialize(name, coin)
    @name = name
    @coin = coin
  end

  def take_turn(moves, stdin = $stdin)
    print "select a column to insert your coin"
    input = stdin.gets.chomp.to_i

    until moves.include?(input)
      print "you cannot puts that there"
      input = stdin.gets.chomp.to_i
    end
    input
  end
end