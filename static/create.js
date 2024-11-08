document.addEventListener('DOMContentLoaded', () => {
  const svg = d3.select('#mindmap')
    .append('svg')
    .attr('width', '100%')
    .attr('height', '100%')
    .append('g')
    .attr('transform', 'translate(400, 200)'); // Center the SVG in the container

  const width = 800;
  const height = 400;

  // Basic mindmap structure
  const data = {
    name: 'MindMap',
    children: []
  };

  const root = d3.hierarchy(data);
  const treeLayout = d3.tree().size([width - 160, height - 160]);
  treeLayout(root);

  // Draw links
  svg.selectAll('line')
    .data(root.links())
    .enter()
    .append('line')
    .attr('x1', d => d.source.x)
    .attr('y1', d => d.source.y)
    .attr('x2', d => d.target.x)
    .attr('y2', d => d.target.y)
    .attr('stroke', '#00e676')
    .attr('stroke-width', 2);

  // Draw nodes
  svg.selectAll('circle')
    .data(root.descendants())
    .enter()
    .append('circle')
    .attr('cx', d => d.x)
    .attr('cy', d => d.y)
    .attr('r', 5)
    .attr('fill', '#00e676');

  svg.selectAll('text')
    .data(root.descendants())
    .enter()
    .append('text')
    .attr('x', d => d.x + 10)
    .attr('y', d => d.y)
    .text(d => d.data.name)
    .attr('fill', '#e0f7fa');
});
