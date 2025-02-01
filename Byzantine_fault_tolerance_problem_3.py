import turtle
import random
import math
import time
from PIL import Image
import os

# Screen setup
screen = turtle.Screen()
screen.title("Byzantine Generals Problem Simulation")
screen.bgcolor("white")
screen.setup(width=800, height=800)

# General class
class General:
    def __init__(self, id, x, y, is_traitor=False):
        self.id = id
        self.is_traitor = is_traitor
        self.orders = []  # Stores lists of orders from each round
        self.majority_votes = []  # Stores majority votes from each round
        self.x = x
        self.y = y
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.shape("circle")
        self.turtle.color("blue" if not is_traitor else "red")
        self.turtle.goto(x, y)
        self.turtle.stamp()  # Draw the general

        # Separate turtle for text display
        self.text_turtle = turtle.Turtle()
        self.text_turtle.hideturtle()
        self.text_turtle.penup()

    def send_order(self, num_recipients):
        if not self.is_traitor:
            return ["attack"] * num_recipients
        orders = []
        base_order = random.choice(["attack", "retreat"])
        anomaly_index = random.randint(0, num_recipients - 1)

        for i in range(num_recipients):
            if i == anomaly_index:
                orders.append("retreat" if base_order == "attack" else "attack")
            else:
                orders.append(base_order)

        return orders

    def receive_order(self, order):
        self.orders.append(order)

    def relay_orders(self, all_orders, num_recipients):
        if self.is_traitor:
            for i in range(len(all_orders)):
                if random.random() < 0.5:
                    all_orders[i] = "retreat" if all_orders[i] == "attack" else "attack"
        return all_orders[:num_recipients]

    def display_orders(self):
        self.text_turtle.goto(self.x, self.y - 35)
        orders_text = ", ".join(self.orders[-1])  # Display last round orders
        self.text_turtle.clear()
        self.text_turtle.write(f"Orders: {orders_text}", align="center", font=("Arial", 10, "normal"))

    def display_majority_vote(self):
        if self.majority_votes:
            majority_vote_text = f"Majority: {self.majority_votes[-1]}"
            self.text_turtle.goto(self.x, self.y - 55)
            self.text_turtle.write(majority_vote_text, align="center", font=("Arial", 10, "italic"))

# Function to draw a directional message line between two generals with arrow in the middle
def draw_message(g1, g2, message, offset=10):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()

    x1, y1 = g1.x, g1.y
    x2, y2 = g2.x, g2.y
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx**2 + dy**2)

    start_x = x1 + offset * dy / distance
    start_y = y1 - offset * dx / distance
    end_x = x2 + offset * dy / distance
    end_y = y2 - offset * dx / distance

    pen.goto(start_x, start_y)
    pen.pendown()
    pen.pencolor("green" if message == "attack" else "red")
    pen.goto(end_x, end_y)

    mid_x = (start_x + end_x) / 2
    mid_y = (start_y + end_y) / 2
    pen.penup()
    pen.goto(mid_x, mid_y)

    angle_to_receiver = math.degrees(math.atan2(dy, dx))
    pen.setheading(angle_to_receiver)

    pen.pendown()
    pen.forward(10)
    pen.penup()
    pen.backward(10)
    pen.left(135)
    pen.pendown()
    pen.forward(7)
    pen.penup()
    pen.backward(7)
    pen.right(270)
    pen.pendown()
    pen.forward(7)
    pen.penup()
    return pen  # Return pen for clearing later

# Display the current iteration number
iteration_display = turtle.Turtle()
iteration_display.hideturtle()
iteration_display.penup()
iteration_display.goto(0, 350)
iteration_display.write("Iteration: 0", align="center", font=("Arial", 16, "bold"))

def update_iteration_display(iteration):
    iteration_display.clear()
    iteration_display.write(f"Iteration: {iteration}", align="center", font=("Arial", 16, "bold"))

# Capture each iteration as an image
def capture_iteration(iteration):
    file_name = f"iteration_{iteration}.eps"
    canvas = screen.getcanvas()
    canvas.postscript(file=file_name, colormode="color")

    # Convert EPS to PNG using Pillow
    img = Image.open(file_name)
    img.save(f"iteration_{iteration}.png")
    os.remove(file_name)  # Clean up EPS file

# Clear all edges for each new iteration
def clear_edges(pens):
    for pen in pens:
        pen.clear()

# Display the majority vote for each general after each iteration
def display_majority_vote(generals):
    for general in generals:
        last_orders = general.orders[-1] if general.orders else []
        if last_orders:
            majority_vote = max(set(last_orders), key=last_orders.count)
            general.majority_votes.append(majority_vote)
            general.display_majority_vote()

# Check if consensus has been achieved among all loyal generals
def check_consensus(generals):
    majority_votes = [max(set(general.orders[-1]), key=general.orders[-1].count) for general in generals if not general.is_traitor]
    return len(set(majority_votes)) == 1

# Simulate multiple rounds of communication
def simulate_rounds(generals, num_rounds):
    for round_num in range(1, num_rounds + 1):
        update_iteration_display(round_num)

        # First phase: Each general sends orders
        message_pens = []  # Store pens for clearing edges
        for general in generals:
            orders = general.send_order(len(generals) - 1)
            order_index = 0
            for other in generals:
                if other != general:
                    pen = draw_message(general, other, orders[order_index])
                    message_pens.append(pen)
                    other.receive_order(orders[order_index])
                    order_index += 1

        # Second phase: Each general relays received orders
        for general in generals:
            relayed_orders = general.relay_orders(general.orders, len(generals) - 1)
            for other in generals:
                if other != general:
                    for order in relayed_orders:
                        pen = draw_message(general, other, order)
                        message_pens.append(pen)
                    other.orders.extend(relayed_orders)

        # Display all orders and majority votes, then pause
        for general in generals:
            general.display_orders()
            display_majority_vote(generals)
        
        # Pause for 3 seconds to show orders and majority votes
        time.sleep(3)

        # Clear the edges and orders display
        clear_edges(message_pens)
        for general in generals:
            general.text_turtle.clear()

        # Capture the state of each round as an image
        capture_iteration(round_num)

        # Check if consensus is achieved
        if check_consensus(generals):
            iteration_display.goto(0, 300)
            iteration_display.write(f"Consensus Achieved at Iteration {round_num}", align="center", font=("Arial", 16, "bold"))
            time.sleep(10)
            break

# Create a set of generals in a circular formation
def byzantine_simulation(num_generals, num_traitors, num_rounds):
    generals = []
    radius = 250
    angle_step = 360 / num_generals

    for i in range(num_generals):
        angle = angle_step * i
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        is_traitor = i < num_traitors
        generals.append(General(i, x, y, is_traitor))

    simulate_rounds(generals, num_rounds)

# Main function
def main():
    num_generals = int(screen.numinput("Generals", "Enter number of generals:", minval=3, maxval=10))
    num_traitors = int(screen.numinput("Traitors", "Enter number of traitors:", minval=0, maxval=num_generals-1))
    num_rounds = int(screen.numinput("Rounds", "Enter number of rounds:", minval=1, maxval=5))

    byzantine_simulation(num_generals, num_traitors, num_rounds)
    screen.mainloop()

if __name__ == "__main__":
    main() 