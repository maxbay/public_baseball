# Max Bay's Public Baseball Stuff

Welcome to my public baseball repository! This contains a collection of code (in various forms) focused on things that interest me.


## Apps

**[Dynamic Dead Zone](https://dynamic-dead-zone.streamlit.app/)**
   - One of the first cues batters have as to the shape of an incoming pitch is the arm slot of the pitcher. This app models the "expected" shape of a fastball as distribution conditional on pitcher scaled release point.

<img src="https://raw.githubusercontent.com/maxbay/public_baseball/refs/heads/main/imgs/DDZ.png" alt="Dynamic Dead Zone" width="350" />

## Projects in Both Python and R, Separated by Programming Language 
   
### Python (Notebooks)

Here’s a list of the notebooks you’ll find in the `/notebooks` directory:

**[Command Confidence Ellipse](https://github.com/maxbay/public_baseball/blob/main/notebooks/command_confellipse.ipynb)**
   - Uses vertical and horizontal release angle variance of fastball as proxy for command. Turns out this is pretty sticky between seasons. 

**[Dynamic Spin Efficiency](https://github.com/maxbay/public_baseball/blob/main/notebooks/dynamic_spin_efficiency.ipynb)**
   - Spin efficiency changes over the flight of a pitch because the ball drops over time. This looks at a couple theoretical examples. 
   
**[Infer 3D Spin Vector](https://github.com/maxbay/public_baseball/blob/main/notebooks/infer_spin_vector.ipynb)**
   - This uses [Dr. Alan Nathan's method](https://baseball.physics.illinois.edu/HawkeyeAveSpinComponents.pdf) to infer the 3D spin vector components from tracking data
   - I also wrote this for use in R programming language [link here](https://maxbay.github.io/public_baseball/infer_spin_vector.html)

**[Fetch Player Height Data](https://github.com/maxbay/public_baseball/blob/main/notebooks/fetch_player_height.ipynb)**
   - Convenience functions for getting player height data via API endpoint
   - I also wrote this for use in R programming language [link here](https://maxbay.github.io/public_baseball/fetch_player_height.html)


**[Release Angle to Plate](https://github.com/maxbay/public_baseball/blob/main/notebooks/releaes_angle_var.ipynb)**
   - Small changes in release angle can have a massive effect on the quality of a pitch. The notebook has some visualizations demonstrating this.

### R
**[Infer 3D Spin Vector](https://maxbay.github.io/public_baseball/infer_spin_vector.html)**
   - This uses [Dr. Alan Nathan's method](https://baseball.physics.illinois.edu/HawkeyeAveSpinComponents.pdf) to infer the 3D spin vector components from tracking data

**[Fetch Player Height Data](https://maxbay.github.io/public_baseball/fetch_player_height.html)**
   - Convenience functions for getting player height data via API endpoint
