# TA1 - Random Walk Simulation Using AgentPy

This program simulates multiple agents moving randomly inside a bounded grid. It records each agent's path, prints final positions, compares two scenarios, and saves the resulting graphs.

## Requirements

- Python 3.x
- AgentPy
- Matplotlib

## Install the Libraries

Open PowerShell and run:

```powershell
python -m pip install agentpy matplotlib
```

If `python` is not recognized, use:

```powershell
py -m pip install agentpy matplotlib
```

## Run the Program

Open PowerShell and go to the folder containing the Python file:

```powershell
cd "C:\Users\Msi\Documents\Codex\2026-10-09\objective-to-understand-the-concept-of\work"
```

Run the program:

```powershell
python TA1_random_walk_code_only.py
```

Alternatively:

```powershell
py TA1_random_walk_code_only.py
```

## Suggested Input

```text
Enter number of agents: 5
Enter grid size (e.g., 10 for 10x10): 10
Enter number of steps: 20
Use collision avoidance? (y/n): n
```

Enter `y` to make agents avoid occupied cells when possible. Enter `n` to allow agents to cross paths and occupy the same cells.

## Generated Files

The program creates these files in the current folder:

- `TA1_agent_paths.png` - paths of the agents in Scenario 1
- `TA1_scenario_comparison.png` - comparison of the original and expanded scenarios
- `TA1_final_positions.txt` - final coordinates of the Scenario 1 agents

The graph window also opens after the simulation. Close it to finish the program.

## What the Graph Symbols Mean

- Colored line: complete path of one agent
- Circle: starting position
- X marker: final position

## Recommended Evidence for the PDF

Include the following:

1. The Python code
2. A terminal screenshot showing the entered values and final positions
3. `TA1_agent_paths.png`
4. `TA1_scenario_comparison.png`
5. The final-position results
6. Your observations and answers to the four questions

## Troubleshooting

### `ModuleNotFoundError: No module named 'agentpy'`

Install AgentPy using:

```powershell
python -m pip install agentpy
```

### `ModuleNotFoundError: No module named 'matplotlib'`

Install Matplotlib using:

```powershell
python -m pip install matplotlib
```

### PowerShell cannot find the Python file

Confirm that PowerShell is in the correct folder:

```powershell
Get-ChildItem
```

You should see `TA1_random_walk_code_only.py` in the list.

### No graph appears

Wait for the simulation to finish and check the current folder for the two PNG files. The images are saved even if the graph window does not appear.
