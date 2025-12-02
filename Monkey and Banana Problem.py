# Monkey and Banana Problem Simulation

# Initial State
state = {
    "monkey": "door",
    "box": "window",
    "monkey_on_box": False,
    "bananas": "middle",
    "has_bananas": False
}

def print_state(step):
    print(f"\nStep {step} State:")
    for key, value in state.items():
        print(f"{key}: {value}")

print("Initial State:")
print_state(0)

# Step 1: Monkey moves to the box
state["monkey"] = state["box"]
print_state(1)

# Step 2: Monkey pushes the box to the banana position
state["box"] = state["bananas"]
state["monkey"] = state["bananas"]
print_state(2)

# Step 3: Monkey climbs on the box
state["monkey_on_box"] = True
print_state(3)

# Step 4: Monkey grabs the bananas
state["has_bananas"] = True
print_state(4)

# Final Output
if state["has_bananas"]:
    print("\n🎉 Success! The monkey has grabbed the bananas!")
else:
    print("\n❌ The monkey failed to get the bananas.")
