import re

with open('skills_animated.svg', 'r') as f:
    content = f.read()

# Extract all <svg ...>...</svg> blocks that are inside the <g> tags.
svgs = re.findall(r'<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"256\" height=\"256\".*?</svg>', content, flags=re.DOTALL)

# We have 8 SVGs: Rust, Solidity, Go, C++, TS, Python, Linux, Docker.
# We will draw 8 slots. 
# Slot size: 56x56. Spacing: 8.
# Total width = 8*56 + 7*8 = 448 + 56 = 504.
# Let's add some padding: 10px on all sides.
# Total width = 504 + 20 = 524
# Total height = 56 + 20 = 76

out = ['<svg width=\"524\" height=\"76\" viewBox=\"0 0 524 76\" xmlns=\"http://www.w3.org/2000/svg\">']

# Draw main inventory background
out.append('<rect fill=\"#1a1a2e\" shape-rendering=\"crispEdges\" x=\"0\" y=\"0\" width=\"524\" height=\"76\" rx=\"4\"/>')

# Draw slots and place icons
for i, svg_content in enumerate(svgs):
    x = 10 + i * (56 + 8)
    y = 10
    
    # Outer dark border
    out.append(f'<rect fill=\"#0a0a14\" shape-rendering=\"crispEdges\" x=\"{x}\" y=\"{y}\" width=\"56\" height=\"56\" />')
    
    # Inner border to create 3D sunken effect
    out.append(f'<path fill=\"#11111e\" shape-rendering=\"crispEdges\" d=\"M{x} {y} h56 v4 h-52 v52 h-4 z\"/>')
    out.append(f'<path fill=\"#2d2d4a\" shape-rendering=\"crispEdges\" d=\"M{x+56} {y+56} h-56 v-4 h52 v-52 h4 z\"/>')
    
    # Scale down
    cx = x + 6
    cy = y + 6
    
    # Strip the <svg ...> and </svg> tags from svg_content
    inner_content = re.sub(r'^<svg[^>]*>', '', svg_content)
    inner_content = re.sub(r'</svg>$', '', inner_content)
    
    out.append(f'<g transform=\"translate({cx}, {cy})\">')
    out.append(f'<animateTransform attributeName=\"transform\" type=\"translate\" values=\"{cx},{cy}; {cx},{cy-4}; {cx},{cy}\" dur=\"2.5s\" begin=\"{i*0.2}s\" repeatCount=\"indefinite\"/>')
    out.append(f'<g transform=\"scale(0.171875)\">')
    out.append(inner_content)
    out.append('</g>')
    out.append('</g>')

out.append('</svg>')

with open('inventory-stack.svg', 'w') as f:
    f.write('\n'.join(out))

print('Generated inventory-stack.svg')
