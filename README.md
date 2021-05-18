# Simple MVP Graphviz

This project is a simple implementation of Graphviz. Has a frontend based on Node.js and a backend based on Flask (API).  

On the frontend is possible to edit (ace.js) the graph using the Dot language and on change the graph is updated (Viz.js). Is possible to pan and zoom the graph (panzoom.js) and is possible to collapse the editor to enlarge the graph area.  Errors on the Dot are presented.

The frontend is self sufficient, but provides the ability to get the graph SVG from the backend (is the only thing the backend does).

## Technologies
 - Node.js (Frontend)
 - Flask (Backend)
 - Docker
 
## Languages
- Vanilla JS (Frontend)
- Python (Backend)
- HTML & CSS

## Libraries
Viz.js: Graphviz library (Frontend)
PanZoom: panning and zooming of HTML elements (Frontend)
Ace editor: embeddable code editor (Frontend)


## Requirements
 - Docker
 - Docker compose

## Configurations
 - Change the URL for the backend: on index.htm line 182
 
## Running
Clone the project and run "docker-compose up --build".
