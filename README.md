# Public Baseball Analysis

Welcome to my public baseball analysis repository! This repository contains a collection of code (in various forms) focused on various research, demonstrations and modeling projects that interest me. 

## Notebooks

Here’s a list of the notebooks you’ll find in the `/notebooks` directory:

1. **[Command Confidence Ellipse](notebooks/notebooks/command_confellipse.ipynb)**
   - Uses vertical and horizontal release angle variance of fastball as proxy for command. Turns out this is pretty sticky between seasons. 

2. **[Dynamic Spin Efficiency](notebooks/dynamic_spin_efficiency.ipynb)**
    - Spin efficiency changes over the flight of a pitch because the ball drops over time. This looks at a couple theoretical examples. 
   
4. **[Infer 3D Spin Vector](notebooks/infer_spin_vector.ipynb)**
   - This uses [Dr. Alan Nathan's method](https://baseball.physics.illinois.edu/HawkeyeAveSpinComponents.pdf) to infer the 3D spin vector components from tracking data
   - I also wrote this for use in R programming language [link here](https://maxbay.github.io/public_baseball/infer_spin_vector.html)

5. **[Release Angle to Plate](notebooks/releaes_angle_var.ipynb)**
   - Small changes in release angle can have a massive effect on the quality of a pitch. The notebook has some visualizations demonstrating this. 


## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/maxbay/public_baseball.git
