from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    # TODO: Ask more questions to collect facts for reasoning
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
    if input("Is your budget high? (y/n): ").lower().startswith("y"):
        facts.append("budget_high")
    #Started asking my own questions to collect more facts for reasoning
    if input("Is your budget low? (y/n): ").lower().startswith("y"):
        facts.append("budget_low")
        
    #comeback to this case
    if input("Is your budget not too high but also not too low (y/n): ").lower().startswith("y"):
        facts.append("budget_medium")
    
    
    #continue here with fact prompt I like 
    if input("Do you need AI acceleration or GPU tensor cores? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")
    """Operating System Prefernce"""
    if input("Do you prefer macOS (y/n): ").lower().startswith("y"):
        facts.append("prefers_os_macos")
    elif input("Do you prefer Linux?").lower().startswith('y'):
        facts.append("prefers_os_linux")
    """Continuation of the rest of the prompts"""
    
        
    return facts

def main():
    # TODO: Load rules, create engine, assert facts, and run inference
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)
    initial_facts = collect_initial_facts()
    engine.assert_facts(initial_facts)
    engine.run()
    results = engine.conclusions()
    
    
    load_rules()
    pass

if __name__ == "__main__":
    main()
