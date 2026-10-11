# TA2 Rule Based Agent

This Python program simulates a rule-based vacuum agent in an environment containing two rooms, A and B. Each room can be either Dirty or Clean.

## Requirements

- Python 3.x
- No external libraries are required

## Files

- `TA2_rule_based.py` - Python program
- `TA2_simulation_results.txt` - output created after running the program

## Open the TA2 Folder

Open PowerShell and enter:

```powershell
cd "C:\Users\Msi\Documents\School\CS elective\TA2"
```

Quotation marks are required because the folder name `CS elective` contains a space.

Check that the Python file is present:

```powershell
Get-ChildItem
```

## Run the Program

```powershell
python .\TA2_rule_based.py
```

If the `python` command is unavailable, try:

```powershell
py .\TA2_rule_based.py
```

## Recommended Input

Enter the following values when prompted:

```text
Initial condition of Room A: Dirty
Initial condition of Room B: Dirty
Starting location (A/B): A
Number of simulation steps: 6
```

Input is not case-sensitive, so `dirty`, `Dirty`, and `DIRTY` are accepted.

## Expected Behavior

The agent should perform these actions:

1. Clean Room A.
2. Move from Room A to Room B.
3. Clean Room B.
4. Move from Room B to Room A.
5. Move from Room A to Room B.
6. Move from Room B to Room A.

The final result should show:

```text
Room A: Clean
Room B: Clean
Agent location: A
Results saved to TA2_simulation_results.txt
```

## Agent Rules

1. If the current room is Dirty, the agent cleans it.
2. If the current room is Clean, the agent moves to the other room.
3. The simulation continues until the requested number of steps is completed.

## Generated Output

The program automatically creates:

```text
TA2_simulation_results.txt
```

This file contains every simulation step, including the agent's location, perception, action, room conditions, and location after the action.

## Evidence for the PDF

Take a screenshot that clearly shows:

- The four input values
- All six simulation steps
- The final state of Rooms A and B
- The final agent location
- The saved-results message

Include the Python code, terminal screenshot, observation, and analysis answers in `TA2_Sabulao.pdf`.

## Troubleshooting

### PowerShell cannot find the folder

Use quotation marks around the complete path:

```powershell
cd "C:\Users\Msi\Documents\School\CS elective\TA2"
```

### Python cannot find the file

Check the filename:

```powershell
Get-ChildItem *.py
```

Then run the exact filename displayed by PowerShell.

### The program does not ask for the number of steps

You are running the older version of the code. Replace it with the corrected `TA2_rule_based.py`, which asks for:

```text
Number of simulation steps:
```

### Invalid room status

Enter only:

```text
Dirty
```

or:

```text
Clean
```

### Invalid starting location

Enter only `A` or `B`.
