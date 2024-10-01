The script performs basic graph analysis and visualizes a subset of the network.

## Requirements
- Python 3.x
- `networkx`
- `matplotlib`

## Installation
1. Clone the repository to your local machine:
   git clone https://github.com/edwardkrupicka/Discrete-Structures-Capstone.git
2. Install required dependencies (networkx and matplotlib)
    Put this into your terminal: `pip install -r requirements.txt`
3. Run the main.py script

## Dataset
1. An example of what we are working with

`    {
    "0": {
        "id": 0,
        "age": 75,
        "location": "Los Angeles",
        "interests": ["sports", "food", "travel"],
        "connections": [
        1, 2, 3, ...
        ]
    }
    }`

2. The data after we loop through and organize it

`    User ID: 0
    Age: 75
    Location: Los Angeles
    Interests: sports, food, travel
    Connections: [1, 2, 3, ...]`