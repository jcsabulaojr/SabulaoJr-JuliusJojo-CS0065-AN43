from dataclasses import dataclass
from pathlib import Path


@dataclass
class TwoRoomEnvironment:
    """Stores and updates the condition of rooms A and B."""

    rooms: dict[str, str]

    def perceive(self, location: str) -> str:
        return self.rooms[location]

    def is_dirty(self, location: str) -> bool:
        """Return True when the selected room is dirty."""
        return self.rooms[location] == "Dirty"

    def clean(self, location: str) -> None:
        self.rooms[location] = "Clean"

class RuleBasedVacuumAgent:
    """Chooses actions using predefined condition-action rules."""

    def __init__(self, starting_location: str):
        self.location = starting_location

    def perceive_and_act(self, environment: TwoRoomEnvironment) -> str:
        """Apply the required rules and return a readable action."""
        # Rule 1: If the current room is dirty, clean it.
        if environment.is_dirty(self.location):
            environment.clean(self.location)
            return f"CLEANED Room {self.location}"

        # Rule 2: If the current room is clean, move to the other room.
        previous_location = self.location
        self.move()
        return f"MOVED from Room {previous_location} to Room {self.location}"

    def move(self) -> None:
        """Switch between Room A and Room B."""
        self.location = "B" if self.location == "A" else "A"


def normalize_status(value: str) -> str:
    value = value.strip().lower()
    if value == "dirty":
        return "Dirty"
    if value == "clean":
        return "Clean"
    raise ValueError("Room status must be Dirty or Clean.")


def run_simulation(room_a: str, room_b: str, start: str, number_of_steps: int):
    environment = TwoRoomEnvironment({"A": room_a, "B": room_b})
    agent = RuleBasedVacuumAgent(start)
    records = []

    print("\nRULE-BASED VACUUM AGENT")
    print("Step | Location Before | Perception | Action                        | Room A | Room B | Location After")
    print("-" * 108)

    for step in range(1, number_of_steps + 1):
        location_before = agent.location
        perception = environment.perceive(location_before)
        action = agent.perceive_and_act(environment)

        record = {
            "step": step,
            "location": location_before,
            "perception": perception,
            "action": action,
            "room_a": environment.rooms["A"],
            "room_b": environment.rooms["B"],
            "location_after": agent.location,
        }
        records.append(record)

        print(
            f"{step:>4} | {location_before:^15} | {perception:^10} | "
            f"{action:<29} | {environment.rooms['A']:^6} | "
            f"{environment.rooms['B']:^6} | {agent.location:^14}"
        )

    return environment, agent, records


def save_results(records, filename="TA2_simulation_results.txt"):
    lines = [
        "TA2 - RULE-BASED VACUUM AGENT RESULTS",
        "",
        "Step | Location Before | Perception | Action | Room A | Room B | Location After",
        "-" * 108,
    ]

    for row in records:
        lines.append(
            f"{row['step']:>4} | {row['location']:^15} | {row['perception']:^10} | "
            f"{row['action']:<29} | {row['room_a']:^6} | {row['room_b']:^6} | "
            f"{row['location_after']:^14}"
        )

    Path(filename).write_text("\n".join(lines), encoding="utf-8")


def main():
    print("TA2 - RULE-BASED AGENT")
    print("Enter either Dirty or Clean for each room.")

    try:
        room_a = normalize_status(input("Initial condition of Room A: "))
        room_b = normalize_status(input("Initial condition of Room B: "))
        start = input("Starting location (A/B): ").strip().upper()
        number_of_steps = int(input("Number of simulation steps: "))

        if start not in {"A", "B"}:
            raise ValueError("Starting location must be A or B.")
        if number_of_steps <= 0:
            raise ValueError("Number of steps must be greater than zero.")

        environment, agent, records = run_simulation(
            room_a, room_b, start, number_of_steps
        )
        save_results(records)

        print("\nFINAL RESULT")
        print(f"Room A: {environment.rooms['A']}")
        print(f"Room B: {environment.rooms['B']}")
        print(f"Agent location: {agent.location}")
        print("Results saved to TA2_simulation_results.txt")

    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    main()
