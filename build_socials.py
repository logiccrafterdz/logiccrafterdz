import os

buttons = [
    {"name": "btn-x", "text": "X / TWITTER", "color": "#1a1a2e", "delay": "0s"},
    {"name": "btn-farcaster", "text": "FARCASTER", "color": "#7b2cbf", "delay": "0.3s"},
    {"name": "btn-website", "text": "WEBSITE", "color": "#5b21b6", "delay": "0.6s"},
    {"name": "btn-email", "text": "EMAIL", "color": "#f15bb5", "delay": "0.9s"}
]

svg_template = """<svg width="150" height="36" viewBox="0 0 150 36" xmlns="http://www.w3.org/2000/svg">
  <style>
    .pixel {{ shape-rendering: crispEdges; }}
    .btn-text {{ font-family: 'Courier New', monospace; font-size: 14px; font-weight: bold; fill: #ffffff; text-anchor: middle; }}
    .bg {{ fill: {color}; }}
    .border-dark {{ fill: #000000; }}
    .border-light {{ fill: #ffffff; opacity: 0.2; }}
    
    @keyframes press {{
      0%, 100% {{ transform: translateY(0); }}
      50% {{ transform: translateY(2px); }}
    }}
    .btn-box {{ animation: press 3s ease-in-out infinite {delay}; }}
  </style>
  
  <g class="btn-box" transform="translate(0, 0)">
    <!-- Outer Border -->
    <rect class="border-dark pixel" x="0" y="0" width="150" height="36" />
    
    <!-- Button Body -->
    <rect class="bg pixel" x="2" y="2" width="146" height="32" />
    
    <!-- Highlights (Top & Left) -->
    <rect class="border-light pixel" x="2" y="2" width="146" height="2" />
    <rect class="border-light pixel" x="2" y="2" width="2" height="32" />
    
    <!-- Shadows (Bottom & Right) -->
    <rect class="border-dark pixel" x="2" y="32" width="146" height="2" opacity="0.5" />
    <rect class="border-dark pixel" x="146" y="2" width="2" height="32" opacity="0.5" />
    
    <!-- Text -->
    <text x="75" y="22" class="btn-text">{text}</text>
  </g>
</svg>"""

for btn in buttons:
    with open(f'{btn["name"]}.svg', 'w') as f:
        f.write(svg_template.format(color=btn["color"], text=btn["text"], delay=btn["delay"]))

print("Generated social buttons.")
