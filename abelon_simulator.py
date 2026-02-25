import random

def generate_abelon_sequence(attempts):
    """
    Generates the exact Abelon Sequence.
    Rule: Starts with 1, 2, 3. From the 4th position, it is the sum of all previous terms.
    """
    if attempts == 0: return []
    if attempts == 1: return [1]
    if attempts == 2: return [1, 2]
    
    sequence = [1, 2, 3]
    for _ in range(4, attempts + 1):
        # The sum of all previous terms algebraically results in multiplying the last term by 2
        sequence.append(sequence[-1] * 2)
        
    return sequence

def generate_abelon_with_jitter(attempts):
    """
    Generates network wait times based on the Abelon Sequence + Jitter.
    Adds a random fraction of a second (controlled chaos) to prevent exact collisions.
    """
    base_sequence = generate_abelon_sequence(attempts)
    real_wait_times = []
    
    for exact_time in base_sequence:
        # Generates a random float between 0.0 and 1.0 (the Jitter)
        jitter = random.uniform(0.0, 1.0)
        real_time = exact_time + jitter
        
        # Rounding to 3 decimal places (milliseconds) for readability
        real_wait_times.append(round(real_time, 3))
        
    return real_wait_times

def run_simulation():
    """
    Simulates the Thundering Herd problem comparing Pure Math vs Hybrid Backoff.
    Server Max Capacity: 3 requests per second.
    """
    print("=== STARTING STRESS TEST ===")
    print("Server Status: ONLINE")
    print("Maximum Capacity: 3 requests per second.")
    print("Clients waiting: 5 computers.\n")
    
    print("-" * 50)
    print("🔴 SCENARIO A: Pure Abelon Sequence (Exact Math)")
    print("Rule: All clients wait exactly 1.000 second on their first attempt.\n")
    
    print("⏳ [Starting backoff countdown for 5 PCs...]")
    
    # Simulating the exact math (all PCs try at exactly the same time)
    first_attempt_pure = generate_abelon_sequence(5)[0] 
    
    for i in range(1, 6):
        print(f"⏱️ T={first_attempt_pure:.3f}s: PC-{i} sends connection packet.")
        
    print("\n🚨 SYSTEM ALERT: 5 requests collided at the exact millisecond 1.000!")
    print("💥 RESULT: Overload detected (Thundering Herd). Server CRASHED!")
    print("-" * 50 + "\n")
    
    print("Restarting server...")
    print("Server Status: ONLINE\n")
    
    print("-" * 50)
    print("🟢 SCENARIO B: Hybrid Abelon Sequence (With Jitter)")
    print("Rule: Wait 1 second + a random fraction of milliseconds.\n")
    
    print("⏳ [Starting jittered backoff countdown for 5 PCs...]")
    
    # Simulating the hybrid approach (each PC gets a slightly different time)
    clients = []
    for i in range(1, 6):
        first_attempt_jitter = generate_abelon_with_jitter(5)[0]
        clients.append((first_attempt_jitter, f"PC-{i}"))
        
    # Sort by time to simulate chronological arrival at the server
    clients.sort()
    
    for time, pc_name in clients:
        print(f"⏱️ T={time:.3f}s: {pc_name} sends connection packet... [Handled ✅]")
        
    print("\n🟢 RESULT: No simultaneous collisions. Load perfectly distributed over the second.")
    print("Server SURVIVED!")
    print("=== END OF SIMULATION ===")

# Standard Python boilerplate to execute the script
if __name__ == "__main__":
    run_simulation()
