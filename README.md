**ClassFX** is a lightweight, fast, stylish and easy to use UI tool (or if you want UI Engine idek prob tool tho).
What I wanted to achieve with ClassFX is:
1. An easier way to Program UI's
2. More UI style possibilities
3. To make animations look less robotic and make this process easier as well 
4. To make it easier for people to focus on the logic of their app or program which is the more important thing anyway

**Key Features of ClassFX:**
**Holistic UI System:** Includes Buttons, Sliders, Toggle Switches, and Radio Groups.

**Animation Engine:** Built in support for linear and Easing-based (In/Out) motion design.

**Visual Fidelity:** Native support for color gradients, transparency simulation (dithering), and 3D projections.

**Performance:** Optimized for the specific hardware constraints of the calculator while maintaining a professional look and feel. (some features are maybe not great optimised but that will probably change later)

The Tool is used by just importing it with:
**Import classfx**

**When building apps or programs ensure you do this to have little to no problems:**

**1. Initialization:**
Define all objects outside the while loop. This ensures they are allocated in memory only once.

**2. Event loop:**
Process inputs here. Thanks to the ControlPanel concept, you don't need to manage every individual element manually.

**3. Render logic:**
Instead of writing 20 lines of code for like 5-6 buttons, sliders etc. just to make them render and just show the old image with ClassFX you only need cp.draw() this makes it easier to focus and it looks much cleaner.
