import engine
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
    # Started asking my own questions to collect more facts for reasoning
    if input("Is your budget low? (y/n): ").lower().startswith("y"):
        facts.append("budget_low")

    # comeback to this case
    if input("Is your budget not too high but also not too low (y/n): ").lower().startswith("y"):
        facts.append("budget_medium")

    # continue here with fact prompt I like
    if input("Do you need AI acceleration or GPU tensor cores? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")
    """Operating System Prefernce"""
    if input("Do you prefer macOS (y/n): ").lower().startswith("y"):
        facts.append("prefers_os_macos")
    elif input("Do you prefer Linux? (y/n): ").lower().startswith('y'):
        facts.append("prefers_os_linux")
    """Continuation of the rest of the prompts"""
    if input("Do you travel often with your laptop? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
    if input("Do you like laptops with a bigger screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Do you tend to use your laptop for creative work? I.e (video editing, desgin, etc.) (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Do you game? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Do you you mainly use your laptop for office or school work? (y/n:) ").lower().startswith("y"):
        facts.append("office_only")

    # spit out the facts you entered
    print("\nYou said : ", facts)

    return facts


def main():
    # TODO: Load rules, create engine, assert facts, and run inference
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)
    intial_facts = collect_initial_facts()
    engine.assert_facts(intial_facts)
    engine.run()
    results = engine.conclusions()

    #print("\n--- Recomended Laptop Options or the Facts Inferred")
    #for facts in results:
    #    print("-", facts)

    print("DEBUG RESULTS:", results)  # remove after testing

    # If there were no conclusions at all
    if not results or not results.get("recommendations"):
        print("> No recommendation could be made.")
        return

    # Extract the first recommendation
    raw_conclusion = results["recommendations"][0]  # e.g. "recommend:premium_ultrabook"

    # Strip the "recommend:" prefix
    if raw_conclusion.startswith("recommend:"):
        conclusion = raw_conclusion.split("recommend:")[1]
    else:
        conclusion = raw_conclusion

    # Determine explanation
    # Try to match a rule whose consequent matches the recommendation
    rule_name = None
    for rule in rules:
        if rule.consequent == raw_conclusion:
            rule_name = rule.name
            break

    print("> Recommendation:", conclusion)

    if rule_name:
        print(f"> Explanation: derived from rule '{rule_name}'")
    else:
        print("> Explanation: based on matched facts.")
if __name__ == "__main__":
    main()
