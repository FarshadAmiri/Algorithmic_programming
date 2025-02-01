import turtle
import random
import math

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
        self.orders = []
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
        # Loyal generals always say "attack"
        if not self.is_traitor:
            return ["attack"] * num_recipients

        # Traitors send random orders with at least one anomaly
        orders = []
        base_order = random.choice(["attack", "retreat"])  # Base order for traitor
        anomaly_index = random.randint(0, num_recipients - 1)  # Index of the anomalous message
        
        for i in range(num_recipients):
            if i == anomaly_index:
                # Ensure at least one order differs
                orders.append("retreat" if base_order == "attack" else "attack")
            else:
                orders.append(base_order)
        
        return orders
    
    def receive_order(self, order):
        self.orders.append(order)
    
    def display_orders(self):
        # Display the orders received by this general slightly below the node
        self.text_turtle.goto(self.x, self.y - 35)  # Position below the node
        orders_text = ", ".join(self.orders)
        self.text_turtle.clear()  # Clear previous text if any
        self.text_turtle.write(f"Orders: {orders_text}", align="center", font=("Arial", 10, "normal"))

# Function to draw a directional message line between two generals with an arrow in the middle
def draw_message(g1, g2, message, offset=10):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()

    # Get the coordinates for a slightly offset line to avoid overlap
    x1, y1 = g1.x, g1.y
    x2, y2 = g2.x, g2.y
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx**2 + dy**2)

    # Adjust the start and end positions to avoid overlap
    start_x = x1 + offset * dy / distance
    start_y = y1 - offset * dx / distance
    end_x = x2 + offset * dy / distance
    end_y = y2 - offset * dx / distance

    # Draw the main line from sender to receiver
    pen.goto(start_x, start_y)
    pen.pendown()
    pen.pencolor("green" if message == "attack" else "red")
    pen.goto(end_x, end_y)

    # Calculate the midpoint for the arrow
    mid_x = (start_x + end_x) / 2
    mid_y = (start_y + end_y) / 2
    pen.penup()
    pen.goto(mid_x, mid_y)

    # Point the arrowhead towards the receiver
    angle_to_receiver = math.degrees(math.atan2(dy, dx))
    pen.setheading(angle_to_receiver)

    # Draw the arrowhead
    pen.pendown()
    pen.forward(10)  # Draw the main arrowhead line
    pen.backward(10)
    pen.left(135)
    pen.forward(7)
    pen.backward(7)
    pen.right(270)
    pen.forward(7)
    pen.penup()



# Simulate a round of communication
def simulate_round(generals):
    # Randomize the order of generals (including traitors)
    random.shuffle(generals)
    
    for general in generals:
        orders = general.send_order(len(generals) - 1)  # Prepare orders for all other generals
        order_index = 0
        for other in generals:
            if other != general:
                # Draw a message line from general to other
                draw_message(general, other, orders[order_index])
                other.receive_order(orders[order_index])
                order_index += 1

# Create a set of generals in a circular formation
def byzantine_simulation(num_generals, num_traitors):
    generals = []
    radius = 250
    angle_step = 360 / num_generals

    # Create generals in a circular arrangement
    for i in range(num_generals):
        angle = angle_step * i
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        is_traitor = i < num_traitors  # First few generals are traitors
        generals.append(General(i, x, y, is_traitor))

    # Simulate a round of communication
    simulate_round(generals)

    # Display the orders received by each general
    for general in generals:
        general.display_orders()

# Main function
def main():
    num_generals = int(screen.numinput("Generals", "Enter number of generals:", minval=3, maxval=10))
    num_traitors = int(screen.numinput("Traitors", "Enter number of traitors:", minval=0, maxval=num_generals-1))

    byzantine_simulation(num_generals, num_traitors)

    screen.mainloop()

# Run the simulation
main()
