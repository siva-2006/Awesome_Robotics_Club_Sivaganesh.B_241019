# Awesome_Robotics_Club_Sivaganesh.B_241019
Task -  4

Part - A

Magnetic Ball Control
If the ball is made of steel or some magnetic material, we could place a grid of electromagnets underneath the platform and use them to pull the ball in different directions. By carefully adjusting the strength of the magnets, like turning one on slightly while turning another off, we can gently attract the ball and move it around the surface without physically moving the platform at all. This method is quiet, has no moving parts, and is extremely responsive. The ball glides around as if by an invisible hand. The main challenge would be precise control of the magnetic fields and managing heat from the electromagnets, but it’s a creative and visually impressive alternative to traditional servo-based designs.

Components:

Electromagnets:

These are used to create a magnetic field to pull the ball in different directions. You need small but powerful electromagnets to control the ball effectively.

Position Sensors:

Sensors like capacitive or magnetic field sensors track the ball's position on the platform, sending data to the controller.

Controller:

A controller adjusts the current to the electromagnets based on the ball's position, moving the ball by changing the magnetic field.



Challenges:

Controlling Magnetic Strength:

It’s tricky to balance the magnetic field so the ball moves smoothly without getting yanked too hard.

Overheating:

Electromagnets can get hot if used too much, so managing power and heat dissipation is important.

Interference:

Strong magnetic fields can interfere with other electronics, requiring shielding.



Pros:

No moving parts – Since the platform itself doesn’t move, there’s less wear and tear and fewer things that can break.

Super quiet – No motors or mechanical noise means the whole thing can run silently.

Very responsive – Electromagnets can be turned on and off really quickly, allowing for fast, smooth control.

Futuristic and impressive – Watching a ball move around as if by magic looks really cool and can grab attention in demos.

Compact design – Everything stays under the surface, so the setup can be made very neat.



Cons:

Only works with magnetic balls – The ball needs to be metallic (steel or iron), so we are limited in material choices.

Complex control system – Managing multiple magnets at once and smoothly coordinating their strengths might be tricky.

Overheating risk – Electromagnets can heat up if they’re on too long or too strong, so we will need cooling or limits.

Limited lifting power – If the ball is too heavy, the magnets might not be strong enough to move it well.

Expensive components – High-quality electromagnets and power drivers can get pricey.



Part - 2

Approach 1: Infrared (IR) Sensors with Reflective Markers

1. Sensors and Specifications

We could use infrared (IR) sensors to detect the ball’s position. An array of IR emitters and detectors would be placed around the edges of the platform. The ball would have a reflective marker (a strip or small patch) that bounces the infrared light back to the detector as it rolls around.



2. Tracking Motion

The system can track the ball by measuring the relative position of the reflective marker using the IR sensors. As the ball rolls across the platform, it changes the intensity of the reflected light that the detectors pick up. By comparing the data from multiple sensors arranged around the edges, the system can calculate the ball’s 2D position on the platform.



3. Pros and Cons

Pros:

Low cost compared to vision systems.

Relatively simple to set up and add into a system.

Can work in low-light conditions since IR light doesn’t depend on visible light.

High responsiveness with low latency.



Cons:

Limited range and resolution so may not work well over larger distances or for very fast-moving balls.

Potential interference from other IR sources (like sunlight) or reflective surfaces.

Accuracy may decrease if the reflective marker is too small or if the ball’s position doesn’t align well with the sensors.



Approach 2: Capacitive Position Sensing

1. Sensors and Specifications

Another approach could be using capacitive sensors to detect the position of the ball. These sensors can sense changes in the electrostatic field created by the presence of the ball. A set of capacitive grid sensors could be placed under the platform to create an invisible 2D grid. As the ball rolls, it disrupts the electric field, and the system can track the position based on the changes in capacitance like our phones detect where we touch on the screen.



2. Tracking Motion

The system works by measuring the changes in capacitance across the sensor grid. When the ball rolls over different areas of the platform, the sensors detect changes in the field, and by processing this data, the system can pinpoint the ball’s position. It can even measure the ball's speed and direction by analyzing how fast these changes happen across the sensors.



3. Pros and Cons

Pros:

Relatively high accuracy for small-scale setups.

Low power consumption once set up.

Doesn’t require direct contact with the ball.



Cons:

Requires a specialized grid of sensors, which can be a bit more complex to set up.

Sensitive to environmental factors, such as humidity or material interference, which could affect the capacitance readings.

May struggle with very fast-moving or small objects due to sensitivity limits.
