### Project Overview

 For this project, we will be exploring the publicly available data from LendingClub.com. Lending Club connects people who need money (borrowers) with people 
who have money (investors). As an investor one would want to invest in people who showed a profile of having a high probability of paying the amount back.

Problem Statement
What is the probability that the borrower paid back their loan in full?


### Learnings from the project

 learned Bayers theorem


### Approach taken to solve the problem

 Independence check !
To calculate the joint probability it's very important that conditions are independent of each other. Les's check whether the condition fico credit score 
is greater than 700 and purpose == 'debt_consolidation' is independent of each other.

Bayes theorem
Calculating conditional probability is a very important step. Let's calculate the Bayes theorem for the probability of credit policy is yes and the person 
is given the loan.


