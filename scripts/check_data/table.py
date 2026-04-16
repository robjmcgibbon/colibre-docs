#!/bin/env python

def rst_grid_table(headers, rows, padding=0):
    """
    Function to generate an rst grid table

    headers - headers stored as a list of strings
    rows - rows stored as a list of lists of strings
    """
    # Add a bit of extra width to each column to allow some edits
    col_widths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]

    # Add soem extra space for editting the description (e.g. adding :math:)
    col_widths[-1] += padding

    def format_row(row):
        return "| " + " | ".join(f"{str(cell):<{w}}" for cell, w in zip(row, col_widths)) + " |"

    def separator(char="-"):
        return f"+{char}" + f"{char}+{char}".join(char * w for w in col_widths) + f"{char}+"

    # Build the table
    lines = [separator("-"), format_row(headers), separator("=")]
    for row in rows:
        lines.append(format_row(row))
        lines.append(separator())
    return "\n".join(lines)
