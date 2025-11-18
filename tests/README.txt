Add your own test cases here.



Test 1:

Prompt: 
      Is portability important? y 
      Do you need a long battery life? y 
      Is your budget high? Y 

Expected Output: 
      >Recommendation: premium_ultrabook
      >Explanation: derived from rule 'Premium Ultrabook'







Test 2:

Prompt: 
      Do you need a long battery life? Y 
      Is your budget hight? Y 
      Do you need AI acceleration or GPU tensor cores? Y 
      Do you game? Y 
Expected Output:
      >Recommendation: high_end_gaming_laptop
      >Explanation: derived from rule 'High End Gaming Laptop'






Test 3:

Prompt:
      Is portability important? Y 
      Do you need AI acceleration or GPU tensor cores? Y
      Do you tend to use your laptop for creative work? I.e (video editing, desgin, etc.) ? Y 
      Do you you mainly use your laptop for office or school work? Y
Expected Output:
      >No recommendation could be made.




