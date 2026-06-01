-- In this example, we used the concatenation operator || to concatenate the first name, space, and last name of every customer.
-- If a column alias contains one or more spaces, you need to surround it with double quotes like this:
-- SELECT
--     first_name || ' ' || last_name "full name",
-- 	email
-- FROM
--     customer;



-- Because the ORDER BY clause is evaluated after the SELECT clause, the column alias len is available and can be used in the ORDER BY clause.
-- SELECT
--   first_name,
--   LENGTH(first_name) len
-- FROM
--   customer
-- ORDER BY
--   len DESC;



-- To place NULL before other non-null values, you use the NULLS FIRST option:
-- SELECT
--   num
-- FROM
--   sort_demo
-- ORDER BY
--   num NULLS FIRST;


-- DISTINCT Removes all duplicate rows from the result set — every column must match for a row to be considered a duplicate.
-- SELECT DISTINCT name, subject, score  from student_scores order by "name";

-- -- DISTINCT ON (expression) A PostgreSQL-specific extension that keeps only the first row for each unique value of the specified expression(s), while still letting you select other columns.
-- SELECT
--   DISTINCT ON (name) name,
--   subject,
--   score
-- FROM
--   student_scores
-- ORDER BY
--   name,
--   score DESC;


-- SELECT
--     film_id,
--     title
-- FROM
--     film
-- ORDER BY
--     title
-- OFFSET 5 ROW
-- FETCH FIRST 5 ROW ONLY;

-- To match the values in the payment_date column with a list of dates, you need to cast them to date values that have the date part only.

-- To do that you use the :: cast operator:

-- SELECT
--   payment_id,
--   amount,
--   payment_date
-- FROM
--   payment
-- WHERE
--   payment_date::date IN ('2007-02-15', '2007-02-16');


-- inner join 

-- SELECT
--   customer_id,
--   first_name,
--   last_name,
--   amount,
--   payment_date
-- FROM
--   customer
--   INNER JOIN payment USING(customer_id)
-- ORDER BY
--   payment_date;