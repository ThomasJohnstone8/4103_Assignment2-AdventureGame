import random
from collections import deque

# Grid size and starting health of the player
gridSize = 5
startHealth = 10

# List of tuples corrosponding to the direction 
directionOptions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (up, down, left, right)
directionName = ["Up", "Down", "Left", "Right"]

# Create the grid in terminal
def generateGrid(players):
    grid = [['.' for _ in range(gridSize)] for _ in range(gridSize)] # Making every point in the grid a [.]

    # Place treasure
    treasure_x, treasure_y = random.randint(0, gridSize-1), random.randint(0, gridSize-1) # Use random module to randomly place the treasure
    grid[treasure_x][treasure_y] = 'T'

    # Place traps and obstacles randomly
    for _ in range(gridSize * 2):  # Randomly place traps and obstacles * 2 so there are more traps and obstacles
        x, y = random.randint(0, gridSize-1), random.randint(0, gridSize-1)
        if grid[x][y] == '.':
            grid[x][y] = random.choice(['X', 'O'])

    # Place power-ups
    for _ in range(gridSize):  # Randomly place power-ups
        x, y = random.randint(0, gridSize-1), random.randint(0, gridSize-1)
        if grid[x][y] == '.':
            grid[x][y] = 'P'

    # Place both players at the same starting position (0, 0)
    for player in players:
        player.position = (0, 0)

    return grid, (treasure_x, treasure_y)

# Display the grid
def displayGrid(grid, players):
    print("\nGrid:")
    for r in range(gridSize):
        row = ""
        for c in range(gridSize):
            cell = grid[r][c]
            # Display player positions
            player_here = [player for player in players if player.position == (r, c)] # Checks what the players position is in the grid
            if player_here:
                row += f"[{player_here[0].name}] "  # Display player name
            else:
                row += f"[{cell}] " # Formatted string to display the cells ([.], T, X, O, P)
        print(row)
    print()

# Player class
class Player:
    def __init__(self, name):
        self.name = name  # Name is 1 or 2
        self.health = startHealth
        self.position = None  # Player position will be set during grid generation

# Search Algorithms


# BFS: Find shortest path to treasure with movement directions
def bfs(grid, start, goal):
    visited = [[False] * gridSize for _ in range(gridSize)]
    queue = deque([(start, [])])  # (current_position, path_taken)
    directionMap = {
        (-1, 0): "Up",
        (1, 0): "Down",
        (0, -1): "Left",
        (0, 1): "Right"
    } # Dictionary that changes the directional deltas into directions a player can read easier
    
    while queue:
        (x, y), path = queue.popleft()
        
        # If we reach the goal, return the path with directions
        if (x, y) == goal:
            directions = []
            for move in path:
                directions.append(directionMap[move])
            return directions
        
        for dx, dy in directionOptions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < gridSize and 0 <= ny < gridSize and not visited[nx][ny]:
                if grid[nx][ny] not in ['O']:  # Can’t move through obstacles
                    visited[nx][ny] = True
                    queue.append(((nx, ny), path + [(dx, dy)]))
    
    return []  # Return an empty list if no valid path was found


# DFS: Explore deeply
def dfs(grid, start):
    stack = [start]
    visited = set()
    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in directionOptions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < gridSize and 0 <= ny < gridSize:
                if grid[nx][ny] not in ['O']:  # Can’t move through obstacles
                    stack.append((nx, ny))
    return visited

# Binary Search (BS): Search a specific row or column for treasure or power-ups
def binarySearch(grid, searchType, target):
    if searchType == "row":
        # Search in each row for the target (treasure or power-up)
        for r in range(gridSize):
            row = [grid[r][c] for c in range(gridSize)]
            low, high = 0, gridSize - 1
            while low <= high:
                mid = (low + high) // 2
                if row[mid] == target:
                    return r, mid  # Found the target in this row
                elif row[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
    elif searchType == "column":
        # Search in each column for the target (treasure or power-up)
        for c in range(gridSize):
            column = [grid[r][c] for r in range(gridSize)]
            low, high = 0, gridSize - 1
            while low <= high:
                mid = (low + high) // 2
                if column[mid] == target:
                    return mid, c  # Found the target in this column
                elif column[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
    return None  # Target not found

# Main game loop
def main():
    # Initialise players as Player 1 and Player 2
    players = [Player("1"), Player("2")]  # Name players as 1 and 2
    # Generate grid with players and treasure
    grid, treasurePosition = generateGrid(players)
    
    currentPlayerIndex = 0 # 0 is 1 and 1 is 2 because python counting starts at 0
    
    # Print a welcome message for player to understand the game
    print("Welcome to my Adventure Game! In this game you will face obstacles(O), traps(X) and power ups(P).")
    print("The main goal of this gane is to reach the treasure(T).")
    print("This can be done using the searching algorithms given to you the player or searching yourself. Good Luck!")
    
    while True:
        player = players[currentPlayerIndex]
        # Display grid and player info
        displayGrid(grid, players)
        print(f"Player {player.name}'s Health: {player.health}")

        # Every loop it checks if the player has won 
        if player.position == treasurePosition:
            print(f"Player {player.name} found the treasure! They win!")
            break  # Exit the loop and end the game
        
        # Always checks what the player health is and if it's 0, the game end
        if player.health <= 0:
            print(f"Player {player.name} has been eliminated!")
            players.remove(player) # Also removes the player when eliminated

            # If the length of players is  1, the game ends
            if len(players) == 1:
                print(f"Player {players[0].name} wins!")
                break  # Exit the loop and end the game
        
        # Player's options each turn
        print("Your turn. What would you like to do?")
        print("1. Move (Up, Down, Left, Right)")
        print("2. Use BFS to find the shortest path to the treasure")
        print("3. Use DFS to explore the grid")
        print("4. Use Binary Search to search a row or column for treasure/power-up")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            # Move player (loop to retry if invalid move)
            while True:
                print("Move in which direction?")
                for directionIndex, direction in enumerate(directionName):
                    print(f"{directionIndex + 1}. {direction}")
                directionChoice = int(input("Enter choice (1-4): ")) - 1

                # Validates that it is only within the 4 options.
                if directionChoice not in range(4):
                    print("Invalid move. Try again.")
                    continue
                dx, dy = directionOptions[directionChoice]
                newPosition = (player.position[0] + dx, player.position[1] + dy)

                # Validate move (stay within grid boundaries and not overlap another player)
                if 0 <= newPosition[0] < gridSize and 0 <= newPosition[1] < gridSize:
                    # Check if the new position is empty and not an obstacle
                    if newPosition not in [p.position for p in players] and grid[newPosition[0]][newPosition[1]] != 'O':
                        player.position = newPosition
                        # Check for traps or power-ups
                        if grid[player.position[0]][player.position[1]] == 'X':
                            player.health -= 2  # Trap hit
                            print(f"Player {player.name} stepped on a trap and lost 2 health.")
                        elif grid[player.position[0]][player.position[1]] == 'P':
                            powerType = random.choice(['health', 'hint'])
                            if powerType == 'health':
                                player.health += 2  # Restore health
                                print(f"Player {player.name} found a power-up and gained 2 health.")
                            elif powerType == 'hint':
                                print(f"Player {player.name} found a power-up: The treasure is nearby!")

                        break  # Exit loop after valid move
                    else:
                        print("Invalid move. You can't move into an obstacle or another player. Try again.")
                else:
                    print("Invalid move. Please stay within grid boundaries. Try again.")

        elif choice == "2":
            # BFS to find shortest path to treasure
            path = bfs(grid, player.position, treasurePosition)
            if path:
                print(f"Shortest path to the treasure: {path}")
            else:
                print("No valid path found to the treasure.")
        
        elif choice == "3":
            # DFS to explore deeper
            explored = dfs(grid, player.position)
            print(f"Explored cells: {explored}")

        elif choice == "4":
            # Binary Search to find treasure or power-ups in a certain row or column
            searchType = input("Search in row or column? (Enter 'row' or 'column'): ").strip().lower()
            if searchType not in ['row', 'column']:
                print("Invalid choice. Please enter 'row' or 'column'.")
                continue
            target = input("Enter target to search for ('T' for treasure, 'P' for power-up): ").strip().upper()
            if target not in ['T', 'P']:
                print("Invalid target. Please enter 'T' for treasure or 'P' for power-up.")
                continue
            result = binarySearch(grid, searchType, target)
            if result:
                print(f"Found {target} at position {result}")
            else:
                print(f"{target} not found in the {searchType}.")
        
        else:
            print("Invalid choice, try again.")
            continue
        
        # Switches between players 1 and 2
        currentPlayerIndex = 1 - currentPlayerIndex

# Run the game
if __name__ == "__main__":
    main()
