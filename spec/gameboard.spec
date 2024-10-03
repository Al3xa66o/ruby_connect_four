require 'board'
require 'player'



describe GameBoard do
  let(:gameboard) { GameBoard.new("Leo", "Nardo")}

  it "is a class" do
    expect(gameboard).to be_instance_of GameBoard
  end

  it "has to have istance variable: board, player1, player2, turn_count, moves" do
    expect(gameboard).to respond_to(:board, :player1, :player2, :turn_count, :moves)
  end

  describe "instance variable" do
    describe "players" do
      it "has player istances" do
        expect(gameboard.player1).to be_a Player
        expect(gameboard.player2).to be_a Player
      end
    end

    describe "turn number" do
      it "starts at 1" do
        expect(gameboard.turn_count).to eq(1)
      end
    end

    describe "board" do
      it "is an array made up with 6 column" do
        test_board = Array.new(7) { Array.new(6, " ")}
        expect(gameboard.board).to eq(test_board)
      end
    end
  end

  describe "#display_board" do
    it "print the game board" do
      expect(STDOUT).to receive(:puts).with("\n+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
  1   2   3   4   5   6   7")
      
      gameboard.display_board
    end

    it "handle modified game board" do
      expect(STDOUT).to receive(:puts).with("\n+---+---+---+---+---+---+---+
| ⚫ |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   | ⚫ |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   | ⚫ |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
  1   2   3   4   5   6   7")
      
      gameboard.board[0][5] = '⚫'
      gameboard.board[2][2] = '⚫'
      gameboard.board[6][1] = '⚫'

      gameboard.display_board
    end

    describe "#check_win" do
      describe "#check_horizontal" do
        it "check for an horizontal win" do
          gameboard.board[2][4] = '⚫'
          gameboard.board[3][4] = '⚫'
          gameboard.board[4][4] = '⚫'
          gameboard.board[5][4] = '⚫'
          
          expect(gameboard.check_horizontal).to be true
        end
      end

      describe "#check_vertical" do
        it "check for a vertical win" do
          gameboard.board[1][2] = '⚫'
          gameboard.board[1][3] = '⚫'
          gameboard.board[1][4] = '⚫'
          gameboard.board[1][5] = '⚫'

          expect(gameboard.check_vertical).to be true
        end
      end

      describe "#check_diagonal" do
        it "check for a diagonal win" do
          gameboard.board[3][3] = '⚫'
          gameboard.board[4][2] = '⚫'
          gameboard.board[5][1] = '⚫'
          gameboard.board[6][0] = '⚫'

          expect(gameboard.check_diagonal).to be true

        end
      end
    end
  end
end