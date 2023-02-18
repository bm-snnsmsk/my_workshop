class Question :   
   def __init__(self, text, choice, answer):
      self.text = text 
      self.choice = choice
      self.answer = answer 
   
   def check_answer(self, answer) : 
      return self.answer == answer
   
     
class Quiz :   
   def __init__(self, questions):
      self.questions = questions 
      self.score = 0 
      self.questionIndex = 0 

   def getQuestion(self) : 
      return self.questions[self.questionIndex]     

   def displayQuestion(self) : 
      question = self.getQuestion()
      print(f"Soru {self.questionIndex + 1} : {question.text} ") 

      for i in question.choice :
         print("-",i)
      
      answer = input("cevap : ").lower()
      self.quess(answer)         
      self.load_question() 

   def quess(self, answer) : 
      question = self.getQuestion()
      if question.check_answer(answer) :
         self.score += 1
      self.questionIndex += 1 
      

   def load_question(self) :
      if(len(self.questions) == self.questionIndex) :
         self.show_score()
      else :
         self.displayProgress()
         self.displayQuestion()
   
   def show_score(self) :
     print("toplamn scorunuz : ",self.score)

   def displayProgress(self) :
      totalQuestion = len(self.questions)
      questionNumber = self.questionIndex + 1

      if questionNumber > totalQuestion :
         print("Quiz bitti")
      else :
         print(f" question {questionNumber} of {totalQuestion} ".center(80,"*"))
           




q1 = Question("en iyi proglamlama dili ? ", ["python", "C#", "php", "java"], "python")
q2 = Question("en popüler dili ? ", ["python", "C#", "php", "java"], "python")
q3 = Question("en çok kazandıran dili ? ", ["python", "C#", "php", "java"], "python")
q4 = Question("betik dili ? ", ["python", "C#", "php", "java"], "php")
questions = [q1, q2, q3, q4]

quiz = Quiz(questions)
quiz.load_question()

