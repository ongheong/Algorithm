SELECT NAME, DATETIME
FROM ANIMAL_INS
WHERE ANIMAL_ID NOT IN (
    SELECT A.ANIMAL_ID
    FROM ANIMAL_INS A
    JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
)
ORDER BY DATETIME
LIMIT 3