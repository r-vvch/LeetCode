-- 175. Combine Two Tables
SELECT firstName, lastName, city, state
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId;

-- 176. Second Highest Salary
SELECT (
  SELECT DISTINCT salary
  FROM Employee
  ORDER BY salary DESC
  LIMIT 1 OFFSET 1
) AS SecondHighestSalary;

-- 177. Nth Highest Salary
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
    IF N < 1 THEN 
        RETURN QUERY(SELECT NULL::INT AS salary);
    ELSE
        RETURN QUERY (
            SELECT DISTINCT Employee.salary
            FROM Employee
            ORDER BY salary DESC
            LIMIT 1 OFFSET N - 1
        );
    END IF;
END;
$$ LANGUAGE plpgsql;

-- 178. Rank Scores
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) as rank
FROM Scores 
ORDER BY score DESC;
---- without window function
SELECT s1.score, 
    (SELECT COUNT(DISTINCT s2.score)
    FROM Scores s2 
    WHERE s2.score >= s1.score) AS rank
FROM Scores s1
ORDER BY s1.score DESC;

-- 180. Consecutive Numbers
SELECT DISTINCT num AS ConsecutiveNums 
FROM (
    SELECT 
        num,
        LEAD(num, 1) OVER (ORDER BY id) AS num1,
        LEAD(num, 2) OVER (ORDER BY id) AS num2
    FROM Logs
) AS Logs2
WHERE num = num1 AND num = num2;
---- without window function
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1, Logs l2, Logs l3
WHERE l1.num = l2.num
    AND l2.num = l3.num
    AND l1.id = l2.id - 1
    AND l2.id = l3.id - 1;

-- 181. Employees Earning More Than Their Managers
SELECT a.name as Employee
FROM Employee a
INNER JOIN Employee b ON a.managerId = b.id
WHERE a.salary > b.salary;

-- 182. Duplicate Emails
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;

-- 183. Customers Who Never Order
SELECT name AS Customers
FROM Customers
LEFT JOIN Orders ON Customers.id = Orders.customerId
WHERE Orders.customerId IS NULL;

-- 184. Department Highest Salary
SELECT Department.name as "Department", Employee.name as "Employee", salary as "Salary"
FROM Employee
INNER JOIN Department ON departmentId = Department.id
WHERE salary = (
    SELECT MAX(salary)
    FROM Employee
    WHERE departmentId = Department.id
);

-- 185. Department Top Three Salaries
SELECT d_name as "Department", e_name as "Employee", salary as "Salary"
FROM (
    SELECT Department.name as n, Employee.name as e_name, Employee.salary, 
        DENSE_RANK() OVER (PARTITION BY Department.name ORDER BY Employee.salary DESC)
    FROM Employee
    INNER JOIN Department ON Employee.departmentId = Department.id
) AS sub
WHERE sub.dense_rank <= 3;
