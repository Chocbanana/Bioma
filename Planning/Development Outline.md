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
# IV. Game Mechanics/ Goals
# V. Polish
# Fuck yea we made a game
# VI. Multiplayer!