from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""    
        self.facts.update(initial)




 
    #Implement -> potentuially done
    def can_fire(self, rule: Rule) -> bool:
        """TODO: Return True if all antecedents are true and consequent not yet known."""
        #All the antecedents must be in the facts
        #Consequent shouldn't already be in the facts
        if all (cond in self.facts for cond in rule.antecedents):
            return rule.consequent not in self.facts
        return False
        
        #pass

    def run(self) -> None:
        """TODO: Implement the forward chaining loop."""
        # while there are rules that can fire:
        #     select one rule (students decide tie-breaking)
        #     add its consequent to facts
        #     record in trace
        
        fired_any = True

        while fired_any:
            fired_any = False #reset the iterations

            for rule in sorted(self.rules, key = lambda r: r.priority, reverse = True):
                if self.can_fire(rule):
                    self.facts.add(rule.consequent)

                    self.trace.append({
                        "rule" : rule.name,
                        "fired" : rule.consequent
                    })

                    fired_any = True
                    

       #pass

    def conclusions(self) -> Dict[str, List[str]]:
        """TODO: Return separated results (recommendations, specs, other facts)."""
        
        
        
        #recommendations = [fact for fact in self.facts if fact.startswith("recommend:")]
        #specs = [fact for fact in self.facts if fact.startswith("spec:")]
        #others = [fact for fact in self.facts if not (fact.startswith("recommendations:")or fact.startswith("spec"))]
        recommendations = [fact for fact in self.facts if fact.startswith("recommend:")]        
        specs = [fact for fact in self.facts if fact.startswith("spec:")]
        others = [fact for fact in self.facts
                  if not (fact.startswith("recommend:") or fact.startswith("spec:"))]
        
        
        
        return {
            "recommendations" : recommendations,
            "specs" : specs,
            "others" : others
        }
        
        #pass
