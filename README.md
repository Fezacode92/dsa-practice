# AFTR Stock Manager

A simple Python inventory manager for AFTR, a streetwear clothing brand based in Buenos Aires.

## Features
- **Show inventory**: lists every product with its price and units in stock
- **Record sales**: subtracts stock and blocks a sale if there aren't enough units
- **Restock**: adds units when new stock arrives from the supplier
- **Low stock alerts**: flags products at or below a minimum so you know what to reorder

## How it works
Products are stored in a dictionary, so each one can be found instantly (O(1) lookup).
Each product holds its price and current stock.

## How to run
```bash
python3 inventario.py
```

## What I practised
- Dictionaries and nested data
- Functions with default parameters
- Loops, conditions and early returns
- Big-O thinking: O(1) lookups vs O(n) loops

## Also in this repo
`warmup.py`: data structures and algorithms practice (linear search, string loops, slicing, sorting with `key` and `lambda`).