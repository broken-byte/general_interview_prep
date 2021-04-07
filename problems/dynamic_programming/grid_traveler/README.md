# Grid Traveler
Given n*m grid dimensions, source and target coordinates, how many ways can 
a traveler walk from source to target if they are limited to moving
either right or down? 

###Example:
input = 2, 3, (0,0), (1, 2)
output = 3

Explanation: 
- For a grid of size 2 by 3 from (0, 0) to (1, 2):
  
      [0, 0, 0]
      
      [0, 0, 0]
    We can move:
  
        - Right, Right, Down
        - Down, Right, Right
        - Right, Down, Right
        
