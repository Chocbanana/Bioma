# I. Environment
## A. Geography and weather 
### 1. Generation
  -	 procedural generation using cellular automata (ayyy done by pato) of ground w varying elevations, also lakes/ponds
  -	 rewrite that in c#
  -	 make cliff and lake gen more realistic  (lakes form in valleys,  have mountains, more noise, higher resolution etc)
  -	 try to make mountain shadows look more realistic?
  
### 2. Visual display w UI
  -	 have a "redraw scene button"
  -	 have params displayed and editable in debug mode
  -	 ideally have multiple platforms set up now: osx, windows, linux, android (fuck ios lol)
   
  
### 3. Weather
  -	 (noisy) cycling seasons: temperature, rain/snow
  - Combination of amount of rain and temperature should affect lake water level
  - Should rain create mini pools/ponds if heavy enough? (would require coding ground soaking up water etc)
  
### 4. Assets
 -	Ground textures: high nutrient ground, low nutrient ground
 - water textures
 - generic rain/wind sounds, generic outdoors sound?



## B. Basic plants
### 1. Generation
 - Using turtle drawing or similar, use fractal generation combined w basic plant principles to generate several plant types (varying leaf clustures,, leaf size, branching rules, stem length/flexiblity/thickness)
 - no flowers for now :( 
 - no roots for now
 - only outlines
 - Fixed amount of plant types for now, about 3-5
 
 	
 	
### 2. Properties / Different states
 - Water level, sunlight level, age, health, amt of stored energy (sugar)
 - health is dependent on all of above factors
 - sprite changes based on properties: younger means smaller, less healthy is brown etc
 - if health goes below a certain level, plant dies


### 3. Interactions
 - If there is overlapping of plants in an area, the higher leaves get the sunlight
 - plant clustures near water sources extend the water line logrithmically (i.e. plants near lakes let farther out plants get access to water but at lower amounts)


### 4. Modify / Iterate until stable environment
 - Run to find optimal balance of params of plants, location of lake near mountains, etc until they grow and die at a predictable rate (stable attractor)


----


## C. Basic decomposers
## D. Evolution / Mutable properties
## E. Optimization
## TBD



-------



# II. Playable Character
# III. Offspring 

-------
# IV. Major Technical Challenges 

This game is not just a game: It is an ecosystem simulator with advanced graphics and gameplay mechanics. To achieve something so ambitious we must first prototype some elements of the game, each a small project on its own. 

## Procedural Drawing of Life Forms
We must develop a map that can compute a good-looking creature from some definite set of parameters.  For games like no man's sky, this alone can be the selling point of the while game. For us things can be a little simpler because:
 - We only must render 2d sprites rather than full 3d models
 - Sprites are quite small (maybe 64x64 tops), so details will be less visible 
 - Bad-looking creatures are somewhat ok provided they are not too common
 (<30%). If the user decides to cross a frog with a giraffe do they expect something pretty? 

### Approach 
 - Generate crude 3d model using a fractal technique and lots of random numbers
 - Highlight areas like head, arms etc using colors
 - Project the 3d model onto a 2d image, emphasizing borders using outlines 
 - Post process colored regions with features like face, claws etc

## Ecosystem simulation

In single player, the players main enemy is the ecosystem itself. The player must do better than random natural selection and constantly adapt to a changing environment. To make this challenging the ecosystem must also be good at adapting and produce specialized creatures that are hard to defeat. 

### Suggestions for a prototype
 - Use cellular automata. Each cell can hold one species, or be empty. Each cell has environment parameters like temperature. 
 - Each species has a list of properties governing combat strength,  rate of movement, food requirements. 
 - Time evolve the cellular automaton and see if interesting behavior is common. 
 - Find a means for species to mix and mingle their properties, and improve through natural selection. 
 - Do not make the visualization too fancy. 

## AI Combat system

Combat works as follows:
 - Player controls a main creature with wasd. If this creature dies, it is game over. 
 - Player can select a single other creature to control with the mouse, and action buttons 1234.
 - More than two creatures can be in play, but this is only useful if the player can coordinate them all. 
 - Coordination of other creatures is assisted by AI. 

To make this work we need a good creature AI. We need this for enemy creatures anyway. Can we develop a combat system with bare bones graphics that is already fun to play without all the ecosystem jazz? 

-------
# V. Polish
# Fuck yea we made a game
# VI. Multiplayer!
