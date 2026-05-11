# Group 5 Monopoly Project

# Game Description

Our game will be a modified version of Monopoly. We will incorporate the basic rules of rolling two dice to move around the board. We will also include the CPU in the role of the banker. Users will be able to buy the initial land when they go around the board. The game play aspects that we will eliminate are chance and community chest cards, mortgages, hotels, and any other aspect that we have not listed above.  Plan to eliminate chance,and community chest and change them to spaces that have a player gaining or losing money. Free parking: will be standard Monopoly rules as a free space with no fees when landed on. Standard rent price: prices will be determined by the 2 or 3 sections space. Such as in traditional Monopoly there are two navy blue spaces, 3 light blue spaces etc. The two jail spaces, and the utilities spaces will cause a player to lose a specific amount of money. Railroad spaces can be purchased by players and generate a fixed rent when other players land on them. Community chest and Chance will give users a specific amount of money.  By eliminating some factors of Monopoly it will allow us to keep traditional gameplay while speeding up the games functions. The goal of the players is to gain as much money and bankrupt additional players. The aspects that make our game rewarding is the random dice results for players to get awards or punishments; Players can gain the sense of achievement when they buy properties and earn money from other players.Properties you can improve and purchase. We plan to only allow a player to improve a space with a house, and not go to hotels. 

# Repository Description

1) Main Class
    - Main.py class runs the core gameplay loop by using the other classes. It handles player turns, dice rolling, movement, property interaction, and player status checking.

2) Classes Directory
    - Board.py: It imports BoardSpace Class. Board class creates the structure of the Monopoly game board. It contains BoardSpace, methods to move around the board, get the name of the space.

    - BoardSpace.py: This is responsible to determine the price category, and postion number of any particular space on the board. 

    - Player.py: This class is responsible for controlling the behavior of the player which contains buying property, paying rent, gaining money, moving around the board using the Board Class.

    - Dice.py: This class is simulates rolling a six sided dice and sums value. The sum will determine how many board spaces the player will move.

    - OwnableSpace.py: This class determines the behavior that happens when a player lands on an ownable space. It handles property purchases, rent payments, and house purchase interactions for owned properties.
    
    - CPUPlayer.py: This class respresents the CPU player that makes automated decisions every round of the game without user input.

3) Child Classes Directory
    - Chance_Space.py: This child class uses polymorphism to determine what will happen when a user lands on the Chance Space. 

    - Community_Chest_Space.py: This child class uses polymorphism to determine what will happen when a user lands on the Community Chest Space. 

    - Free_Parking_Space.py: This child class uses polymorphism to determine what will happen when a user lands on the Free Parking Space. 

    - Go_Space.py: This child class uses polymorphism to determine what will happen when a user lands on the Go space.

    - Go_To_Jail.py: This child class uses polymorphism to determine what will happen when a user lands on the Go to Jail Space.

    - Just_Visiting_Space: This child class uses polymorphism to determine what will happen when a user lands on the Just Visiting space.

    - Property_Space.py: This child class outline the details of each space on the board. This class allows for upgrades to a specific space on the board. It uses encapsulation to protect the rent price.   

    - Tax_Space.py: This child class outlines what happens when a player lands on a tax space. It uses encapsulation to protect the tax amount. 

    - Railroad_Space.py: This child class represents railroad spaces that can be purchased and generate a fixed rent when other players land on them.

    - Utility_Space.py: This child class represents utility spaces that can be purchased and require players to pay a fixed fee when landed on.


# References

- Monopoly Rules. (n.d.). Retrieved April 24, 2026, from https://fgbradleys.com/wp-content/uploads/rules/Monopoly_Rules.pdf?srsltid=AfmBOornP4uL21QccxjGKR_EF3P0_j0b1fNeqWtZ6v9Dc94DSQcObE-0

- https://www.howstuffworks.com/about-dave-roos.htm. (2011, July 21). How Monopoly Works. HowStuffWorks. https://entertainment.howstuffworks.com/leisure/brain-games/monopoly2.htm

# Group Members

‌Our group is Section 0303 Group 5, and team members include: 

- Briana Bristow 
- Jiayang Zhang 
- Melanie Abzun 
- Siddhi Patel


# Attribution Table

|Method/Function | Primary Author | Technique Claimed|
|:---            |:---            |:---|
|calculate_rent  | Briana Bristow | Abstraction|
|super().__init__| Briana Bristow | Inheritance|


‌





