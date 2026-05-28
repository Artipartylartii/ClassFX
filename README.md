# Cgui
My free to use UI Engine
for Micropython and the CP fx-400 :D
have fun using it!



Manual: cgui.py (v3.0) Graphics & UI Engine
To use this library in your main program, simply import it alongside gint at the top of your script:

Python
import cgui
import gint
1. Static Rendering Functions (Core Elements)
These functions draw UI components onto the screen instantly but are non-blocking (they do not pause code execution). You must call gint.dupdate() after using them to refresh the display.

draw_header(title, theme)
Draws a standardized top navigation bar with a solid black background and a theme-colored accent line.

Parameters:

title (String): The text centered inside the header.

theme (Dictionary): The active color theme (Defaults to THEME_DARK).

Use Case: Call this at the start of every render loop to give your application a clean, professional title bar.

draw_button(x, y, w, h, text, is_selected, theme)
Rendert a single button with an automatic 3D drop-shadow. If is_selected is set to True, the button flips its color scheme and gains a thicker border to indicate focus.

Parameters:

x, y (Int): Pixel coordinates for the top-left corner.

w, h (Int): Width and height of the button.

text (String): The label of the button (automatically centered).

is_selected (Boolean): True if the button has active focus, otherwise False.

theme (Dictionary): The active color theme.

draw_panel(x, y, w, h, title, theme)
Creates a decorative content card used to visually separate text, data, or game elements from the main background.

Parameters:

title (String): Optional heading in the top-left corner of the panel. If left as an empty string "", no text header is drawn.

Use Case: Perfect for framing stats, match results, vector calculations, or inventory sub-sections.

draw_progress_bar(x, y, w, h, current, maximum, theme)
Renders a precise status or loading bar. It automatically calculates the fill ratio based on your inputs.

Parameters:

current (Int/Float): The current value (e.g., current HP = 45).

maximum (Int/Float): The ceiling/max value (e.g., max HP = 100).

Use Case: RPG health bars, mana pools, loading screens, or XP progress indicators.

2. Interactive D-Pad Components
These functions completely handle the D-pad input loop autonomously. They contain internal while loops, capture keystrokes, and will block code execution until the user presses [EXE] or [EXIT].

show_dialog(title, message, btn_text, theme)
Opens a modal overlay alert box in the dead center of the screen. It freezes the program until the user acknowledges it by pressing [EXE] or [EXIT].

Return Value: None (None).

Use Case: Error popups ("Division by Zero!"), success alerts ("Level Cleared!"), or quick game instructions.

run_menu(title, options, theme, start_y, spacing)
The classic vertical main menu system. The user navigates up and down using the [↑] and [↓] arrow keys.

Parameters:

options (List of Strings): The list of entries (e.g., ["Start Game", "Options", "Exit"]).

start_y (Int): The Y-coordinate of the very first button (Default: 140).

spacing (Int): The vertical distance/gap between buttons (Default: 52).

Return Value: (Int) The index of the selected item (0 to n-1). Returns -1 if the [EXIT] key was pressed.

run_grid_menu(title, options, cols, theme, ...)
A powerful 2D matrix layout system using all four arrow keys ([↑], [↓], [←], [→]) for fluid tile-based navigation.

Parameters:

cols (Int): Number of vertical columns (Default: 2).

Optional Parameters: b_w, b_h (Button dimensions), spacing_x, spacing_y (Grid spacing overrides).

Return Value: (Int) The exact index of the selected grid tile (ordered left-to-right, top-to-bottom). Returns -1 on [EXIT].

Use Case: Level selection screens (e.g., a 4x4 level map), grid-based RPG inventories, or character select screens.

run_slider(title, label, min_val, max_val, current_val, step, theme)
A graphical slider bar component. Pressing [←] or [→] smoothly shifts the bar fill and updates the underlying value instantly using your defined interval.

Parameters:

min_val / max_val (Int): The boundary limits of the slider.

current_val (Int): The starting value when the slider opens.

step (Int): How much the value increments/decrements per key press.

Return Value: (Int) The final confirmed value after the user hits [EXE].

Use Case: Adjusting audio volume, setting game stakes/bet amounts (e.g., $10 to $500), or changing AI difficulty modifiers.

run_checkbox_list(title, item_labels, current_states, theme)
A multi-line settings configuration form. Use [↑]/[↓] to switch rows, and press [EXE], [←], or [→] to toggle the checkboxes between [X] and [ ].

Parameters:

item_labels (List of Strings): Names of the configuration toggles.

current_states (List of Booleans): The initial states of the flags (e.g., [True, False, True]).

Return Value: (List of Booleans) A completely updated list of all states after the menu is exited with [EXIT].

Use Case: Game option screens (e.g., toggling "SFX On/Off", "Enable Permadeath", or "Show FPS").

show_scroll_text(title, text_lines, theme)
A smooth text reader component featuring a dynamic vertical scrollbar tracked on the right edge. It handles endlessly long lists of text lines using [↑] and [↓].

Parameters:

text_lines (List of Strings): Every element in the list represents a single row of text on the screen.

Return Value: None. Closes on [EXE] or [EXIT].

Use Case: Rendering game credits, deep-lore story intros, system logs, or app help manuals.

3. Quick-Reference Themes
You can change the entire aesthetic of your program instantly by utilizing the built-in styles or crafting your own:

cgui.THEME_DARK: Clean, easy on the eyes software look featuring neon cyan/blue highlights.

cgui.THEME_CYBER: Futuristic vaporwave styling using deep indigos, neon purple borders, and vibrant magenta accents.



for anyone who wonders i vibecoded the entire thing lmao
