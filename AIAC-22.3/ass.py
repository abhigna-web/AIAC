'''# Task 1
# Sample candidate data
candidates = [
    {"name": "Aman", "gpa": 9.5, "college": "IIT", "experience": 2, "skills": 3, "gender": "M"},
    {"name": "Sara", "gpa": 8.0, "college": "Local", "experience": 3, "skills": 5, "gender": "F"},
    {"name": "John", "gpa": 9.0, "college": "NIT", "experience": 1, "skills": 4, "gender": "M"},
    {"name": "Priya", "gpa": 8.5, "college": "Local", "experience": 2, "skills": 5, "gender": "F"},
    {"name": "Ali", "gpa": 7.5, "college": "Local", "experience": 4, "skills": 5, "gender": "M"}
]

# -------------------------------
# Biased Shortlisting Function
# -------------------------------
def biased_shortlist(candidates):
    def score(c):
        college_weight = 5 if c["college"] in ["IIT", "NIT"] else 1
        return (c["gpa"] * 2) + (c["experience"] * 2) + college_weight
    
    ranked = sorted(candidates, key=score, reverse=True)
    return ranked[:3]


# -------------------------------
# Unbiased / Diversity-Aware Function
# -------------------------------
def unbiased_shortlist(candidates):
    def score(c):
        return (c["gpa"] * 1.5) + (c["experience"] * 2) + (c["skills"] * 2)
    
    ranked = sorted(candidates, key=score, reverse=True)
    
    # Ensure diversity (at least one female candidate)
    selected = []
    female_added = False
    
    for c in ranked:
        if len(selected) < 3:
            if c["gender"] == "F":
                female_added = True
            selected.append(c)
    
    # If no female selected, replace last with best female
    if not female_added:
        for c in ranked:
            if c["gender"] == "F":
                selected[-1] = c
                break
    
    return selected


# -------------------------------
# Main Execution
# -------------------------------
print("Biased Shortlist:")
for c in biased_shortlist(candidates):
    print(c["name"])

print("\nUnbiased (Diversity-Aware) Shortlist:")
for c in unbiased_shortlist(candidates):
    print(c["name"])

# Explanation:
# The biased_shortlist function gives extra weight to candidates from prestigious colleges, which can lead to overlooking talented candidates from less-known institutions. The unbiased_shortlist function focuses on a more holistic evaluation of candidates and ensures diversity by including at least one female candidate, thus promoting fairness and inclusivity in the selection process.
'''

'''# Task 2
import hashlib

# Function to mask email
def mask_email(email):
    parts = email.split("@")
    return parts[0][0] + "***@" + parts[1]

# Function to hash roll number (encryption alternative)
def hash_roll(roll):
    return hashlib.sha256(roll.encode()).hexdigest()

# Sample student data
students = [
    {"roll": "101", "marks": 85, "email": "student1@gmail.com"},
    {"roll": "102", "marks": 90, "email": "student2@gmail.com"}
]

# Secure processing
for s in students:
    secure_roll = hash_roll(s["roll"])
    masked_email = mask_email(s["email"])
    
    print("Roll (Encrypted):", secure_roll)
    print("Marks:", s["marks"])
    print("Email (Masked):", masked_email)
    print("------")

# Explanation:
# The original script likely stored roll numbers and emails in plain text, which is a security risk. In the improved version, roll numbers are hashed using SHA-256, making them unreadable and secure. Emails are masked to protect student privacy while still allowing for identification. This approach enhances data security and privacy, reducing the risk of sensitive information being exposed.
'''

'''# Task 3
import re
import hashlib

# Validate card number (simple check: 16 digits)
def validate_card(card):
    return bool(re.fullmatch(r"\d{16}", card))

# Mask card number (show only last 4 digits)
def mask_card(card):
    return "****-****-****-" + card[-4:]

# Hash card number (for secure storage)
def hash_card(card):
    return hashlib.sha256(card.encode()).hexdigest()

# Payment processing function
def process_payment(card, amount):
    if not validate_card(card):
        print("Invalid card number!")
        return
    
    encrypted_card = hash_card(card)
    masked = mask_card(card)
    
    print("Processing payment...")
    print("Card:", masked)
    print("Encrypted Card:", encrypted_card)
    print("Amount:", amount)
    print("Payment Successful")

# Example usage
process_payment("1234567812345678", 5000)
# Explanation:
# The original script may have accepted card numbers without validation and stored them in plain text, which is a major security vulnerability. The improved version includes validation to ensure the card number is in the correct format, masks the card number for display to protect user privacy, and hashes the card number for secure storage. This approach significantly enhances the security of sensitive payment information, reducing the risk of data breaches and unauthorized access.
'''

'''# Task 4
import logging
import random

# Configure logging (tracks responsibility)
logging.basicConfig(
    filename="traffic_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Simulated AI decision
def ai_decision(traffic_density):
    if traffic_density > 70:
        return "GREEN"
    elif traffic_density > 40:
        return "YELLOW"
    else:
        return "RED"

# Validation check (engineer's responsibility)
def validate_signal(signal):
    valid_signals = ["RED", "YELLOW", "GREEN"]
    return signal in valid_signals

# Human override (authority control)
def human_override():
    return input("Override signal? (RED/YELLOW/GREEN or NO): ")

# Main traffic control system
def traffic_system():
    traffic_density = random.randint(0, 100)
    print("Traffic Density:", traffic_density)

    signal = ai_decision(traffic_density)

    # Validate AI output
    if not validate_signal(signal):
        logging.error("Invalid AI signal detected!")
        print("Error: Invalid signal")
        return

    # Log AI decision
    logging.info(f"AI suggested signal: {signal}")

    # Human override option
    override = human_override()
    if override in ["RED", "YELLOW", "GREEN"]:
        signal = override
        logging.info(f"Human override applied: {signal}")

    print("Final Signal:", signal)
    logging.info(f"Final signal executed: {signal}")

# Run system
traffic_system()
# Explanation:
# The original traffic control system may have relied solely on AI decisions without proper validation or logging, which can lead to unsafe traffic signals and lack of accountability. The improved version includes validation to ensure the AI's output is valid, logging to track decisions and overrides for accountability, and a human override option to allow for authority control in case of AI errors. This approach enhances the safety and reliability of the traffic control system while ensuring that responsibility is clearly defined and traceable. 
'''

'''#Task 5
import random
import logging

# Logging for safety tracking
logging.basicConfig(
    filename="aircraft_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Simulated sensor data
def get_sensor_data():
    return {
        "engine_temp": random.randint(50, 120),
        "fuel_level": random.randint(10, 100),
        "pressure": random.randint(20, 80)
    }

# AI-based fault detection (simplified)
def detect_fault(data):
    if data["engine_temp"] > 100:
        return "ENGINE OVERHEAT"
    elif data["fuel_level"] < 20:
        return "LOW FUEL"
    elif data["pressure"] < 30:
        return "LOW PRESSURE"
    return "NORMAL"

# Human validation (expert check)
def expert_validation(fault):
    decision = input(f"AI detected: {fault}. Confirm? (YES/NO): ")
    return decision == "YES"

# Fail-safe action
def fail_safe():
    print("Activating fail-safe mode!")
    logging.warning("Fail-safe activated")

# Main system
def aircraft_system():
    data = get_sensor_data()
    print("Sensor Data:", data)

    fault = detect_fault(data)
    logging.info(f"AI detected: {fault}")

    # Human oversight
    if fault != "NORMAL":
        if expert_validation(fault):
            print("Fault confirmed:", fault)
            logging.info("Fault confirmed by expert")
        else:
            print("Fault rejected by expert")
            logging.warning("AI fault rejected")
    else:
        print("System Normal")

    # Safety backup
    if fault != "NORMAL":
        fail_safe()

# Run system
aircraft_system()

# Explanation:
# The original aircraft system may have relied solely on AI for fault detection without human validation or fail-safe mechanisms, which can lead to catastrophic failures if the AI makes an error. The improved version includes human validation to confirm AI-detected faults, logging for accountability and tracking, and a fail-safe mechanism to ensure safety in case of AI errors. This approach enhances the reliability and safety of the aircraft system while ensuring that responsibility is clearly defined and that there are safeguards in place to prevent accidents. 
'''

# Task 6
# Example: AI-generated sorting function (must verify before use)

def sort_numbers(arr):
    # Simple bubble sort (for understanding, not efficiency)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Manual verification (test cases)
def test_sort():
    print(sort_numbers([5, 3, 8, 1]))   # Expected: [1, 3, 5, 8]
    print(sort_numbers([10, -1, 2]))   # Expected: [-1, 2, 10]

# Proper attribution (ethical practice)
print("Note: This code is AI-assisted and manually verified.")

# Run tests
test_sort()
# Explanation:
# The original AI-generated code may have been used without proper verification, which can lead to errors and unintended consequences. The improved version includes manual verification through test cases to ensure the correctness of the sorting function. Additionally, it includes a note about the AI-assisted nature of the code, promoting transparency and ethical practice in software development. This approach ensures that the code is reliable and that the contributions of AI are acknowledged while maintaining human oversight for quality assurance.
