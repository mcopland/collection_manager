# Marvel Snap Collection Manager

## Overview
A Python utility for analyzing and managing your Marvel Snap card collection.

## Features
- Track card collection status

## Prerequisites
- Python 3.8+

## Installation
1. Clone the repository
2. Ensure you have Python installed

## Running the Application
Navigate to the parent directory of the `collection_manager` folder and run:
```bash
python -m collection_manager.main
```

## Project Structure
```
collection_manager/
│
├── common/
│   └── constants.py
│
├── models/
│   ├── card.py
│   └── collection.py
│
└── main.py
```

## Data Files
The application reads the game state from these default locations:
- Collection State: `~/AppData/Locallow/Second Dinner/SNAP/Standalone/States/nvprod/CollectionState.json`

## Troubleshooting
- Ensure you're running the script from the parent directory
- Verify game state JSON files exist and are accessible
- Check Python version compatibility
