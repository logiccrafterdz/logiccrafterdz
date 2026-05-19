import os

svg_template = """<svg width="800" height="200" viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg { fill: #0a0a14; }
    .border-pink { fill: #f15bb5; }
    .border-cyan { fill: #00f5d4; }
    .border-dark { fill: #11111e; }
    
    .text-title { font-family: 'Courier New', monospace; font-size: 16px; font-weight: bold; fill: #00f5d4; letter-spacing: 2px; }
    .text-rank-s { font-family: 'Courier New', monospace; font-size: 24px; font-weight: bold; fill: #f15bb5; filter: drop-shadow(0 0 4px #f15bb5); }
    .text-rank-a { font-family: 'Courier New', monospace; font-size: 24px; font-weight: bold; fill: #00f5d4; filter: drop-shadow(0 0 4px #00f5d4); }
    .text-label { font-family: 'Courier New', monospace; font-size: 12px; font-weight: bold; fill: #c9d1d9; }
    
    .pixel { shape-rendering: crispEdges; }
    
    @keyframes float {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-4px); }
    }
  </style>

  <!-- Container -->
  <rect class="bg pixel" width="800" height="200" rx="4" />
  
  <!-- Title Box -->
  <rect class="border-dark pixel" x="250" y="10" width="300" height="30" />
  <rect class="border-pink pixel" x="250" y="10" width="300" height="2" />
  <rect class="border-pink pixel" x="250" y="38" width="300" height="2" />
  <text x="400" y="30" class="text-title" text-anchor="middle">UNLOCKED ACHIEVEMENTS</text>

  <!-- Achievement 1: STARS -->
  <g transform="translate(60, 60)">
    <rect class="border-dark pixel" x="0" y="0" width="140" height="120" rx="4" />
    <rect class="border-cyan pixel" x="0" y="0" width="140" height="2" />
    
    <!-- Pixel Art Star -->
    <g transform="translate(50, 15) scale(2.5)" style="animation: float 3s infinite 0.1s;">
      <path fill="#ffbd2e" class="pixel" d="M 7 0 h 2 v 2 h 2 v 2 h 4 v 2 h -3 v 2 h 3 v 4 h -2 v -2 h -2 v 4 h -2 v -4 h -2 v 4 h -2 v -4 h -2 v 2 h -2 v -4 h 3 v -2 h -3 v -2 h 4 v -2 h 2 z"/>
      <path fill="#ffd700" class="pixel" d="M 8 2 h 2 v 2 h 2 v 2 h -3 v 2 h 2 v 2 h -2 v -2 h -2 v 2 h -2 v -2 h -2 v 2 h 2 v -2 h -3 v -2 h 2 v -2 h 2 z"/>
    </g>
    
    <text x="70" y="85" class="text-label" text-anchor="middle">TOTAL STARS</text>
    <text x="70" y="110" class="text-rank-s" text-anchor="middle">RANK S</text>
  </g>

  <!-- Achievement 2: COMMITS -->
  <g transform="translate(240, 60)">
    <rect class="border-dark pixel" x="0" y="0" width="140" height="120" rx="4" />
    <rect class="border-pink pixel" x="0" y="0" width="140" height="2" />
    
    <!-- Pixel Art Sword -->
    <g transform="translate(50, 15) scale(2.5)" style="animation: float 3s infinite 0.3s;">
      <path fill="#c9d1d9" class="pixel" d="M 12 0 h 2 v 2 h 2 v 4 h -2 v 2 h -2 v 2 h -2 v 2 h -2 v 2 h -2 v -2 h -2 v -2 h -2 v -2 h -2 v -2 h 2 v -2 h 2 v -2 h 2 v -2 h 4 z"/>
      <path fill="#00f5d4" class="pixel" d="M 13 2 h 1 v 2 h -1 z M 11 4 h 1 v 2 h -1 z M 9 6 h 1 v 2 h -1 z M 7 8 h 1 v 2 h -1 z"/>
      <path fill="#5b21b6" class="pixel" d="M 2 12 h 2 v 2 h -2 z M 0 14 h 2 v 2 h -2 z"/>
    </g>
    
    <text x="70" y="85" class="text-label" text-anchor="middle">TOTAL COMMITS</text>
    <text x="70" y="110" class="text-rank-a" text-anchor="middle">RANK A</text>
  </g>

  <!-- Achievement 3: REPOS -->
  <g transform="translate(420, 60)">
    <rect class="border-dark pixel" x="0" y="0" width="140" height="120" rx="4" />
    <rect class="border-cyan pixel" x="0" y="0" width="140" height="2" />
    
    <!-- Pixel Art Shield -->
    <g transform="translate(50, 15) scale(2.5)" style="animation: float 3s infinite 0.5s;">
      <path fill="#00f5d4" class="pixel" d="M 2 0 h 12 v 2 h 2 v 6 h -2 v 4 h -2 v 2 h -2 v 2 h -4 v -2 h -2 v -2 h -2 v -4 h -2 v -6 h 2 z"/>
      <path fill="#0a0a14" class="pixel" d="M 4 2 h 8 v 8 h -2 v 2 h -4 v -2 h -2 z"/>
      <path fill="#f15bb5" class="pixel" d="M 7 4 h 2 v 4 h -2 z M 5 5 h 6 v 2 h -6 z"/>
    </g>
    
    <text x="70" y="85" class="text-label" text-anchor="middle">REPOSITORIES</text>
    <text x="70" y="110" class="text-rank-s" text-anchor="middle">RANK S</text>
  </g>

  <!-- Achievement 4: FOLLOWERS -->
  <g transform="translate(600, 60)">
    <rect class="border-dark pixel" x="0" y="0" width="140" height="120" rx="4" />
    <rect class="border-pink pixel" x="0" y="0" width="140" height="2" />
    
    <!-- Pixel Art Heart -->
    <g transform="translate(50, 15) scale(2.5)" style="animation: float 3s infinite 0.7s;">
      <path fill="#f15bb5" class="pixel" d="M 2 2 h 4 v -2 h 4 v 2 h 4 v 4 h -2 v 2 h -2 v 2 h -2 v 2 h -4 v -2 h -2 v -2 h -2 v -2 h -2 v -4 z"/>
      <path fill="#ffb3e6" class="pixel" d="M 4 2 h 2 v 2 h -2 z"/>
    </g>
    
    <text x="70" y="85" class="text-label" text-anchor="middle">FOLLOWERS</text>
    <text x="70" y="110" class="text-rank-a" text-anchor="middle">RANK A</text>
  </g>

</svg>"""

with open('achievements.svg', 'w', encoding='utf-8') as f:
    f.write(svg_template)

print("Generated achievements.svg")
