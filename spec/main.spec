require 'main'
require 'player'
require 'board'

describe "main.rb" do
  
  describe "#get_name" do
    before do 
      allow($stdout).to receive(:write)
    end

    it "take a name as input" do
      test = StringIO.new("test")
      name = get_name(0, test)
      expect(name).to eq("test")
    end
  end

  describe "#new_game" do
    it "create an istance of GameBoard" do
      expect(GameBoard).to receive(:new).with("name1", "name2")
      new_game("name1", "name2")
    end

    it "takes two input and use them as a player" do
      expect(new_game("name1", "name2").player1.name).to eq("name1")
      expect(new_game("name1", "name2").player2.name).to eq("name2")
    end

    it "create new player" do
      expect(Player).to receive(:new).with("name1", "⚪")
      expect(Player).to receive(:new).with("name2", "⚫")
      new_game("name1", "name2")
    end
  end
end