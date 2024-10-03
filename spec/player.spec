require 'player'

describe Player do
  let(:player) { Player.new("Leo", "⚫")}

  it "has a name" do
    expect(player.name).to eq("Leo")
  end

end