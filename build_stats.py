import os

svg_template = """<svg width="800" height="280" viewBox="0 0 800 280" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg { fill: #0a0a14; }
    .border-pink { fill: #f15bb5; }
    .border-cyan { fill: #00f5d4; }
    .border-dark { fill: #11111e; }
    
    .text-title { font-family: 'Courier New', monospace; font-size: 16px; font-weight: bold; fill: #f15bb5; letter-spacing: 2px; }
    .text-label { font-family: 'Courier New', monospace; font-size: 14px; font-weight: bold; fill: #00f5d4; }
    .text-value { font-family: 'Courier New', monospace; font-size: 14px; font-weight: bold; fill: #c9d1d9; }
    .text-accent { font-family: 'Courier New', monospace; font-size: 14px; font-weight: bold; fill: #f15bb5; }
    
    .pixel { shape-rendering: crispEdges; }
    
    @keyframes scanline {
      0% { transform: translateY(-280px); }
      100% { transform: translateY(280px); }
    }
  </style>

  <!-- Container -->
  <rect class="bg pixel" width="800" height="280" rx="4" />
  <rect class="border-cyan pixel" x="2" y="2" width="796" height="276" fill="none" stroke-width="2" />
  
  <!-- Title Box -->
  <rect class="border-dark pixel" x="250" y="10" width="300" height="30" />
  <rect class="border-cyan pixel" x="250" y="10" width="300" height="2" />
  <rect class="border-cyan pixel" x="250" y="38" width="300" height="2" />
  <text x="400" y="30" class="text-title" text-anchor="middle">PLAYER DATABANKS (STATS)</text>

  <!-- LEFT PANEL: LIFETIME METRICS -->
  <g transform="translate(40, 70)">
    <rect class="border-dark pixel" x="0" y="0" width="340" height="130" />
    <rect class="border-pink pixel" x="0" y="0" width="2" height="130" />
    
    <text x="15" y="25" class="text-label">>> TOTAL COMMITS:</text>
    <text x="200" y="25" class="text-value">1,337</text>
    
    <text x="15" y="55" class="text-label">>> PULL REQUESTS:</text>
    <text x="200" y="55" class="text-value">42</text>
    
    <text x="15" y="85" class="text-label">>> ISSUES OPENED:</text>
    <text x="200" y="85" class="text-value">128</text>
    
    <text x="15" y="115" class="text-label">>> CODE REVIEWS:</text>
    <text x="200" y="115" class="text-value">56</text>
  </g>

  <!-- RIGHT PANEL: CORE LANGUAGES -->
  <g transform="translate(420, 70)">
    <rect class="border-dark pixel" x="0" y="0" width="340" height="130" />
    <rect class="border-cyan pixel" x="0" y="0" width="2" height="130" />
    
    <!-- TypeScript -->
    <text x="15" y="25" class="text-label">TYPESCRIPT</text>
    <text x="310" y="25" class="text-value" text-anchor="end">45%</text>
    <rect class="pixel" x="15" y="32" width="300" height="6" fill="#11111e" />
    <rect class="pixel" x="15" y="32" width="135" height="6" fill="#00f5d4" />
    
    <!-- Python -->
    <text x="15" y="65" class="text-label">PYTHON</text>
    <text x="310" y="65" class="text-value" text-anchor="end">30%</text>
    <rect class="pixel" x="15" y="72" width="300" height="6" fill="#11111e" />
    <rect class="pixel" x="15" y="72" width="90" height="6" fill="#f15bb5" />
    
    <!-- Rust / Solidity -->
    <text x="15" y="105" class="text-label">RUST / SOLIDITY</text>
    <text x="310" y="105" class="text-value" text-anchor="end">25%</text>
    <rect class="pixel" x="15" y="112" width="300" height="6" fill="#11111e" />
    <rect class="pixel" x="15" y="112" width="75" height="6" fill="#7b2cbf" />
  </g>

  <!-- BOTTOM PANEL: STREAK -->
  <g transform="translate(40, 220)">
    <rect class="border-dark pixel" x="0" y="0" width="720" height="40" />
    
    <!-- Pixel Fire Icon -->
    <g transform="translate(250, 10) scale(1.5)">
      <path fill="#f15bb5" class="pixel" d="M 4 0 h 2 v 2 h 2 v 2 h 2 v 4 h -2 v 2 h -2 v 2 h -4 v -2 h -2 v -2 h -2 v -4 h 2 v -2 h 2 z"/>
      <path fill="#ffbd2e" class="pixel" d="M 5 4 h 2 v 2 h 2 v 2 h -2 v 2 h -4 v -2 h -2 v -2 h 2 z"/>
    </g>
    
    <text x="290" y="25" class="text-label">CURRENT SURVIVAL STREAK:</text>
    <text x="510" y="25" class="text-accent">14 DAYS ACTIVE</text>
  </g>

  <!-- Scanline Overlay -->
  <rect class="pixel" width="800" height="10" fill="#ffffff" opacity="0.05" style="animation: scanline 8s linear infinite;" />

</svg>"""

with open('stats.svg', 'w', encoding='utf-8') as f:
    f.write(svg_template)

print("Generated stats.svg")
