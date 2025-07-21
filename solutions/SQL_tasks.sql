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


-- 196. Delete Duplicate Emails
DELETE FROM person
WHERE id NOT IN (
    SELECT MIN(id)
    FROM Person
    GROUP BY email
);


-- 197. Rising Temperature
SELECT latter.id
FROM Weather latter
LEFT JOIN Weather former ON latter.recordDate::date - former.recordDate::date = 1
WHERE latter.temperature > former.temperature;

---- faster one:
SELECT today.id 
FROM Weather yesterday
CROSS JOIN Weather today
WHERE today.recorddate - yesterday.recorddate = 1
    AND today.temperature > yesterday.temperature;


-- 262. Trips and Users
WITH not_banned as (
    SELECT users_id FROM users
    WHERE banned = 'No'
) 
SELECT request_at as Day,
    ROUND(SUM(CASE WHEN status LIKE 'cancelled%' THEN 1.00 ELSE 0 END) / COUNT(*), 2)
    AS "Cancellation Rate"
FROM Trips
WHERE client_id IN (SELECT users_id FROM not_banned)
    AND driver_id IN (SELECT users_id FROM not_banned)
    AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at;


-- 511. Game Play Analysis I
SELECT player_id, MIN(event_date) AS "first_login"
FROM Activity
GROUP BY player_id
ORDER BY player_id;


-- 550. Game Play Analysis IV
WITH with_agg AS (
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS row_number,
        LEAD(event_date, 1) OVER (PARTITION BY player_id ORDER BY event_date ASC) AS next_login_date
    FROM activity
),
distinct_player_id_count AS (
    SELECT COUNT(DISTINCT player_id) as cnt
    FROM activity
)
SELECT
    ROUND(COUNT(player_id)::DECIMAL/(SELECT cnt FROM distinct_player_id_count), 2) AS fraction
FROM with_agg
WHERE row_number = 1 AND event_date + INTERVAL '1day' = next_login_date;


-- 570. Managers with at Least 5 Direct Reports
SELECT name
FROM Employee managers
JOIN (
    SELECT managerId, COUNT(managerId) as "subordinates"
    FROM Employee
    GROUP BY managerId
) sub ON managers.id = sub.managerId
WHERE subordinates >= 5;


-- 577. Employee Bonus
SELECT name, bonus
FROM Employee
LEFT JOIN Bonus ON Bonus.empId = Employee.empId
WHERE bonus IS NULL or bonus < 1000;


-- 584. Find Customer Referee
SELECT name
FROM Customer
WHERE referee_id IS NULL OR referee_id != 2;


-- 585. Investments in 2016
SELECT ROUND(SUM(tiv_2016)::NUMERIC, 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);


-- 586. Customer Placing the Largest Number of Orders
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(customer_number) DESC
LIMIT 1;


-- 595. Big Countries
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;


-- 596. Classes With at Least 5 Students
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;


-- 601. Human Traffic of Stadium
SELECT DISTINCT a.*
FROM stadium AS a, stadium AS b, stadium AS c
WHERE a.people >= 100 AND b.people >= 100 AND c.people >= 100
AND (
    (a.id - b.id = 1 AND b.id - c.id = 1) OR
    (c.id - b.id = 1 AND b.id - a.id = 1) OR
    (b.id - a.id = 1 AND a.id - c.id = 1)
)
ORDER BY visit_date;

---- window function, faster one
WITH base AS (
    SELECT *,
        LEAD(id, 1) OVER(ORDER BY id) AS next_id,
        LEAD(id, 2) OVER(ORDER BY id) AS second_next_id,
        LAG(id, 1) OVER(ORDER BY id) AS last_id,
        LAG(id, 2) OVER(ORDER BY id) AS second_last_id
    FROM stadium
    WHERE people >= 100 
)
SELECT DISTINCT id, visit_date, people
FROM base 
WHERE (next_id - id = 1 AND id - last_id = 1)
    OR (second_next_id - next_id = 1 AND next_id - id = 1)
    OR (id - last_id = 1 AND last_id - second_last_id = 1)
ORDER BY visit_date;


-- 602. Friend Requests II: Who Has the Most Friends
WITH base AS (
    SELECT requester_id id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id id FROM RequestAccepted
)
select id, COUNT(*) num
FROM base
GROUP BY id
ORDER BY num DESC
LIMIT 1;


-- 607. Sales Person
WITH redz AS (
    SELECT SalesPerson.name
    FROM SalesPerson
    LEFT JOIN Orders ON Orders.sales_id = SalesPerson.sales_id
    LEFT JOIN Company ON Orders.com_id = Company.com_id
    WHERE Company.name = 'RED'
)
SELECT SalesPerson.name
FROM SalesPerson
LEFT JOIN redz on SalesPerson.name = redz.name
WHERE redz.name IS NULL;

---- faster one
SELECT SalesPerson.name
FROM SalesPerson
WHERE SalesPerson.name NOT IN (
    SELECT SalesPerson.name
    FROM SalesPerson
        LEFT JOIN Orders ON SalesPerson.sales_id = Orders.sales_id
        LEFT JOIN Company ON Orders.com_id = Company.com_id
    WHERE Company.name = 'RED'
);


-- 608. Tree Node
SELECT id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree;


-- 610. Triangle Judgement
SELECT x, y, z,
    CASE
        WHEN x >= y + z OR y >= x + z OR z >= x + y THEN 'No'
        ELSE 'Yes'
    END AS triangle
FROM Triangle;


-- 619. Biggest Single Number
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS unique_numbers;


-- 620. Not Boring Movies
SELECT *
FROM Cinema
WHERE id % 2 = 1
AND description != 'boring'
ORDER BY rating DESC;


-- 626. Exchange Seats
SELECT
  CASE
    WHEN id % 2 = 1 AND id != (SELECT MAX(id) FROM Seat) THEN id + 1
    WHEN id % 2 = 0 THEN id - 1
    ELSE id
  END AS id,
  student
FROM Seat
ORDER BY id;


-- 627. Swap Salary
UPDATE Salary
SET sex =
    CASE
        WHEN sex = 'm' THEN 'f'
        ELSE 'm'
    END;
