import random
from pathlib import Path

import agentpy as ap
import matplotlib.pyplot as plt


class RandomWalker(ap.Agent):
    """Agent that randomly moves up, down, left, or right."""

    def setup(self):
        width, height = self.model.p.grid_size
        self.position = (
            self.model.rng.randrange(width),
            self.model.rng.randrange(height),
        )

    def move(self):
        x, y = self.position
        width, height = self.model.p.grid_size
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.model.rng.shuffle(directions)

        possible_positions = []
        for dx, dy in directions:
            # Restrict every coordinate to the grid boundaries.
            new_x = max(0, min(width - 1, x + dx))
            new_y = max(0, min(height - 1, y + dy))
            candidate = (new_x, new_y)
            if candidate not in possible_positions:
                possible_positions.append(candidate)

        # Modified rule: select an unoccupied cell when one is available.
        if self.model.p.avoid_collisions:
            occupied = {
                other.position
                for other in self.model.agents
                if other is not self
            }
            free_positions = [
                position
                for position in possible_positions
                if position not in occupied
            ]
            if free_positions:
                possible_positions = free_positions

        self.position = self.model.rng.choice(possible_positions)


class RandomWalkModel(ap.Model):
    """Multi-agent random walk model with path tracking."""

    def setup(self):
        self.rng = random.Random(self.p.seed)
        self.agents = ap.AgentList(self, self.p.num_agents, RandomWalker)
        self.agents.setup()
        self.paths = {
            agent.id: [agent.position]
            for agent in self.agents
        }

    def step(self):
        for agent in self.agents:
            agent.move()
            self.paths[agent.id].append(agent.position)

    def run_simulation(self):
        for _ in range(self.p.num_steps):
            self.step()
        return self


def run_scenario(num_agents, grid_size, num_steps, seed, avoid_collisions):
    parameters = {
        "num_agents": num_agents,
        "grid_size": (grid_size, grid_size),
        "num_steps": num_steps,
        "seed": seed,
        "avoid_collisions": avoid_collisions,
    }
    model = RandomWalkModel(parameters)
    model.setup()
    return model.run_simulation()


def draw_paths(model, axis, title):
    """Draw the complete path of every agent."""
    width, height = model.p.grid_size

    for number, agent in enumerate(model.agents, start=1):
        path = model.paths[agent.id]
        x_values, y_values = zip(*path)
        axis.plot(
            x_values,
            y_values,
            marker=".",
            linewidth=1.2,
            label=f"Agent {number}",
        )
        axis.scatter(
            x_values[0],
            y_values[0],
            marker="o",
            s=45,
            edgecolor="black",
        )
        axis.scatter(
            x_values[-1],
            y_values[-1],
            marker="X",
            s=70,
            edgecolor="black",
        )

    axis.set_xlim(-0.5, width - 0.5)
    axis.set_ylim(-0.5, height - 0.5)
    axis.set_xticks(range(width))
    axis.set_yticks(range(height))
    axis.set_xlabel("X position")
    axis.set_ylabel("Y position")
    axis.set_title(title)
    axis.grid(True, alpha=0.35)
    axis.legend(fontsize=8, loc="upper left", bbox_to_anchor=(1.02, 1))


def save_final_positions(model, filename):
    """Print and save final positions for laboratory task 3."""
    lines = ["FINAL AGENT POSITIONS"]

    for number, agent in enumerate(model.agents, start=1):
        line = f"Agent {number}: {agent.position}"
        lines.append(line)
        print(line)

    Path(filename).write_text("\n".join(lines), encoding="utf-8")


def main():
    print("RANDOM WALK SIMULATION USING AGENTPY")
    num_agents = int(input("Enter number of agents: "))
    grid_size = int(input("Enter grid size (e.g., 10 for 10x10): "))
    num_steps = int(input("Enter number of steps: "))

    choice = input("Use collision avoidance? (y/n): ").strip().lower()
    avoid_collisions = choice == "y"

    # Scenario 1 uses the values entered by the user.
    scenario_1 = run_scenario(
        num_agents,
        grid_size,
        num_steps,
        seed=42,
        avoid_collisions=avoid_collisions,
    )

    print("\nScenario 1:")
    save_final_positions(scenario_1, "TA1_final_positions.txt")

    # Scenario 2 has twice as many agents and steps for comparison.
    scenario_2 = run_scenario(
        max(2, num_agents * 2),
        grid_size,
        max(4, num_steps * 2),
        seed=99,
        avoid_collisions=avoid_collisions,
    )

    # Save a full path image for Scenario 1.
    figure_1, axis_1 = plt.subplots(figsize=(8, 7))
    draw_paths(scenario_1, axis_1, "Scenario 1 - Agent Paths")
    figure_1.tight_layout()
    figure_1.savefig("TA1_agent_paths.png", dpi=200, bbox_inches="tight")

    # Save the side-by-side comparison required by laboratory task 4.
    figure_2, axes = plt.subplots(1, 2, figsize=(14, 6))
    draw_paths(scenario_1, axes[0], "Scenario 1 - Original Parameters")
    draw_paths(scenario_2, axes[1], "Scenario 2 - More Agents and Steps")
    figure_2.tight_layout()
    figure_2.savefig("TA1_scenario_comparison.png", dpi=200, bbox_inches="tight")

    print("\nFiles created:")
    print("- TA1_final_positions.txt")
    print("- TA1_agent_paths.png")
    print("- TA1_scenario_comparison.png")
    print("Close the graph window to finish the program.")

    plt.show()


if __name__ == "__main__":
    main()
