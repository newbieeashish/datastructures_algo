'''Given an array of unique integers salary where salary[i] is the 
salary of the employee i.

Return the average salary of employees excluding the minimum and
maximum salary.'''

'''Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum
 salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is
(2000+3000)/2= 2500'''

def AverageSalary(salary_list):

    Highest_salary = max(salary_list)
    Lowest_salary = min(salary_list)
    total = 0
    for i in salary_list:
        total += i

    avg = (total-Highest_salary-Lowest_salary)/(len(salary_list)-2)
    return avg

salary = [1000,2000,3000]

print(AverageSalary(salary))

