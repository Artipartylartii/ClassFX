import gint

# --- HELPER FUNKTIONEN ---

def set_background(color):
    gint.dclear(color)

def hex_to_gint(hex_val):
    r = ((hex_val >> 16) & 0xFF) * 31 // 255
    g = ((hex_val >> 8) & 0xFF) * 31 // 255
    b = (hex_val & 0xFF) * 31 // 255
    return gint.C_RGB(r, g, b)

def draw_gradient(x, y, w, h, color1_hex, color2_hex, vertical=True):
    """Zeichnet einen Farbverlauf von color1 zu color2."""
    # Start-Farben (RGB 0-31)
    r1, g1, b1 = ((color1_hex >> 16) & 0xFF) * 31 // 255, ((color1_hex >> 8) & 0xFF) * 31 // 255, (color1_hex & 0xFF) * 31 // 255
    # End-Farben
    r2, g2, b2 = ((color2_hex >> 16) & 0xFF) * 31 // 255, ((color2_hex >> 8) & 0xFF) * 31 // 255, (color2_hex & 0xFF) * 31 // 255
    
    steps = h if vertical else w
    
    for i in range(steps):
        t = i / steps
        # Interpolation
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        col = gint.C_RGB(r, g, b)
        
        if vertical:
            gint.dline(x, y + i, x + w, y + i, col)
        else:
            gint.dline(x + i, y, x + i, y + h, col)

# --- KLASSEN ---

class Slider:
    def __init__(self, x, y, width, min_val, max_val, label):
        self.x, self.y = x, y
        self.width = width
        self.min = min_val
        self.range = max_val - min_val
        self.val = min_val
        self.label = label
        self.hit_x1, self.hit_y1 = x - 5, y - 5
        self.hit_x2, self.hit_y2 = x + width + 5, y + 25

    def update(self, tx, ty):
        if self.hit_x1 <= tx <= self.hit_x2 and self.hit_y1 <= ty <= self.hit_y2:
            ratio = (tx - self.x) / self.width
            self.val = self.min + (ratio * self.range)
            self.val = max(self.min, min(self.min + self.range, self.val))
            return True
        return False

    def draw(self):
        gint.drect_border(self.x-2, self.y-2, self.x + self.width+2, self.y+22, gint.C_NONE, 1, gint.C_BLACK)
        gint.dline(self.x, self.y + 10, self.x + self.width, self.y + 10, gint.C_BLACK)
        knob_x = self.x + int(((self.val - self.min) / self.range) * self.width)
        gint.drect(knob_x - 4, self.y, knob_x + 4, self.y + 20, gint.C_RED)
        gint.dtext(self.x, self.y - 15, gint.C_BLACK, f"{self.label}: {int(self.val)}")

class Button:
    def __init__(self, x, y, w, h, color_hex, text, text_color=gint.C_WHITE):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.color = hex_to_gint(color_hex)
        self.text = text
        self.text_color = text_color

    def draw(self):
        gint.drect(self.x, self.y, self.x + self.w, self.y + self.h, self.color)
        gint.dtext(self.x + 5, self.y + 5, self.text_color, self.text)

    def is_clicked(self, tx, ty):
        return self.x <= tx <= self.x + self.w and self.y <= ty <= self.y + self.h

class Palette:
    def __init__(self):
        self.colors = {
            "rot": 0xFF0000, "dunkelrot": 0x8B0000, "hellrot": 0xFF7F7F, "koralle": 0xFF7F50, "lachs": 0xFA8072,
            "gruen": 0x00FF00, "dunkelgruen": 0x006400, "hellgruen": 0x90EE90, "limette": 0x32CD32, "minze": 0x98FF98,
            "smaragd": 0x50C878, "oliv": 0x808000, "blau": 0x0000FF, "dunkelblau": 0x00008B, "hellblau": 0xADD8E6, 
            "cyan": 0x00FFFF, "marine": 0x000080, "stahlblau": 0x4682B4, "nachtblau": 0x191970, "tuerkis": 0x40E0D0, 
            "indigo": 0x4B0082, "gelb": 0xFFFF00, "gold": 0xFFD700, "orange": 0xFFA500, "ocker": 0xCC7722, 
            "mandarine": 0xF38500, "zitrone": 0xFFF700, "pfirsich": 0xFFDAB9, "lila": 0x800080, "violett": 0xEE82EE, 
            "magenta": 0xFF00FF, "pink": 0xFFC0CB, "lavendel": 0xE6E6FA, "lila-hell": 0xD8BFD8, "weiss": 0xFFFFFF, 
            "schwarz": 0x000000, "grau": 0x808000, "dunkelgrau": 0xA9A9A9, "silber": 0xC0C0C0, "graphit": 0x4F4F4F, 
            "schiefer": 0x708090, "braun": 0xA52A2A, "schoko": 0xD2691E, "beige": 0xF5F5DC, "khaki": 0xF0E68C, 
            "sand": 0xC2B280, "creme": 0xFFFDD0, "terrakotta": 0xE2725B, "weinrot": 0x800020, "teich": 0x008080
        }
class ToggleSwitch:
    def __init__(self, x, y, label):
        self.x, self.y = x, y
        self.label = label
        self.state = False # An/Aus

    def draw(self):
        color = gint.C_GREEN if self.state else gint.C_RED
        gint.drect(self.x, self.y, self.x + 30, self.y + 15, color)
        gint.dtext(self.x + 35, self.y, gint.C_BLACK, self.label)

    def is_clicked(self, tx, ty):
        if self.x <= tx <= self.x + 30 and self.y <= ty <= self.y + 15:
            self.state = not self.state
            return True
        return False

class RadioGroup:
    def __init__(self, x, y, options):
        self.x, self.y = x, y
        self.options = options # Liste: ["Stift", "Linie", "Kreis"]
        self.selected = 0 # Index des aktiven Tools

    def draw(self):
        for i, opt in enumerate(self.options):
            color = gint.C_BLUE if i == self.selected else gint.C_GRAY
            gint.drect(self.x, self.y + (i * 25), self.x + 80, self.y + (i * 25) + 20, color)
            gint.dtext(self.x + 5, self.y + (i * 25) + 3, gint.C_WHITE, opt)

    def update(self, tx, ty):
        for i in range(len(self.options)):
            if self.x <= tx <= self.x + 80 and self.y + (i * 25) <= ty <= self.y + (i * 25) + 20:
                self.selected = i
                return True
        return False
def draw_transparent_rect(x, y, w, h, color):
    """
    Zeichnet ein Rechteck mit 50% Transparenz 
    mittels eines Schachbrettmusters.
    """
    for py in range(y, y + h):
        for px in range(x, x + w):
            # Schachbrett-Logik: Nur jeden zweiten Pixel zeichnen
            if (px + py) % 2 == 0:
                gint.dpixel(px, py, color)

# --- 3D SYSTEM ---

def project_3d(x, y, z, factor=0.5):
    """
    Konvertiert 3D-Koordinaten (x, y, tiefe) in 2D-Screen-Koordinaten.
    'factor' bestimmt, wie stark der 3D-Effekt ist.
    """
    sx = int(x - (z * factor))
    sy = int(y - (z * factor))
    return sx, sy

def draw_3d_box(x, y, w, h, depth, color):
    """Zeichnet einen einfachen 3D-Block."""
    # Front-Rechteck
    gint.drect(x, y, x + w, y + h, color)
    gint.drect_border(x, y, x + w, y + h, gint.C_NONE, 1, gint.C_BLACK)
    
    # Seiten-Fläche (Tiefe)
    # Punkte berechnen
    x1, y1 = project_3d(x + w, y, depth, 0.5)
    x2, y2 = project_3d(x + w, y + h, depth, 0.5)
    
    # Seite zeichnen
    gint.dline(x + w, y, x1, y1, gint.C_BLACK)     # Obere Kante
    gint.dline(x + w, y + h, x2, y2, gint.C_BLACK) # Untere Kante
    gint.dline(x1, y1, x2, y2, gint.C_BLACK)       # Vertikale Kante hinten
    
    # Deckel (optional, falls gewünscht)
    gint.dline(x, y, x - int(depth*0.5), y - int(depth*0.5), gint.C_BLACK)
    gint.dline(x + w, y, x1, y1, gint.C_BLACK)

class Animator:
    def __init__(self, start_val, end_val, duration, mode="linear"):
        self.start = start_val
        self.end = end_val
        self.duration = duration
        self.mode = mode
        self.frame = 0
        self.finished = False
        self.value = start_val

    def _apply_easing(self, t):
        if self.mode == "in":
            return t * t
        if self.mode == "out":
            return 1 - (1 - t) * (1 - t)
        if self.mode == "inout":
            # Smoothstep-Funktion: 3t^2 - 2t^3
            return 3 * t**2 - 2 * t**3
        return t # linear

    def update(self):
        if self.frame < self.duration:
            self.frame += 1
            # Normalisierter Zeitwert t (0 bis 1)
            t_raw = self.frame / self.duration
            # Mathematische Kurve anwenden
            t_eased = self._apply_easing(t_raw)
            # Endwert berechnen
            self.value = self.start + (self.end - self.start) * t_eased
        else:
            self.finished = True
        return self.value

    def reset(self):
        self.frame = 0
        self.finished = False
        self.value = self.start

        # Helper: Mischt zwei Farben basierend auf 't' (0 bis 1)
def lerp_color(c1_hex, c2_hex, t):
    # Zerlege in RGB
    r1, g1, b1 = (c1_hex >> 16) & 0xFF, (c1_hex >> 8) & 0xFF, c1_hex & 0xFF
    r2, g2, b2 = (c2_hex >> 16) & 0xFF, (c2_hex >> 8) & 0xFF, c2_hex & 0xFF
    
    # Interpolation
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    
    # Zurück zu Hex
    return (r << 16) | (g << 8) | b

class AnimatedGradient:
    def __init__(self, x, y, w, h, start_c1, start_c2, end_c1, end_c2, duration):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.c1_start, self.c2_start = start_c1, start_c2
        self.c1_end, self.c2_end = end_c1, end_c2
        self.anim = Animator(0, 1, duration, mode="inout")

    def draw(self):
        t = self.anim.update()
        
        # Aktuelle Farben berechnen
        cur_c1 = lerp_color(self.c1_start, self.c1_end, t)
        cur_c2 = lerp_color(self.c2_start, self.c2_end, t)
        
        # Gradient zeichnen
        draw_gradient(self.x, self.y, self.w, self.h, cur_c1, cur_c2, vertical=True)
        
        # Loop-Logik: Wenn Animation fertig, zurücksetzen oder umkehren
        if self.anim.finished:
            self.anim.reset()

class ControlPanel:
    def __init__(self, x, y, width, height, title="Menu"):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.title = title
        self.components = [] 
        self.bg_color = 0xD3D3D3 # Light gray panel background

    def add(self, component):
        """Adds a UI element (Button, Slider, etc.) to the panel."""
        self.components.append(component)

    def draw(self):
        """Draws the panel container and automatically renders all child components."""
        import gint
        # Draw the main panel box
        gint.drect(self.x, self.y, self.x + self.width, self.y + self.height, self.bg_color)
        gint.drect_border(self.x, self.y, self.x + self.width, self.y + self.height, gint.C_NONE, 1, gint.C_BLACK)
        # Draw the panel title text
        gint.dtext(self.x + 5, self.y + 5, gint.C_BLACK, self.title)
        
        # Tell every single component inside to draw itself
        for comp in self.components:
            comp.draw()

    def handle_event(self, tx, ty):
        """Routes touch coordinates to the correct component inside the panel."""
        for comp in self.components:
            # Check if the component has an active hit-box and was clicked
            if hasattr(comp, 'is_clicked') and comp.is_clicked(tx, ty):
                return comp
            if hasattr(comp, 'update') and comp.update(tx, ty):
                return comp
        return None

    def get(self, name):
        return hex_to_gint(self.colors.get(name.lower(), 0xFFFFFF))