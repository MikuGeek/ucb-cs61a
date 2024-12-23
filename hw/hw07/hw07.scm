(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (sign num)
  (cond 
    ((< num 0) -1)
    ((> num 0) 1)
    (else      0)
  )
)

(define (square x) (* x x))

(define (pow x y)
  (if (= y 1)
      x
      (if (even? y)
          (square (pow x (/ y 2)))
          (* (pow x (- y 1)) x)
      )
  )
)

(define (unique s) 
    (if (null? s) nil
        (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s)))) (cdr s)))))
)

(define (replicate x n)
    (define (helper i prefix)
        (if (= i 0)
            prefix
            (helper (- i 1) (cons x prefix))
        )
    )
    (helper n nil)
)

(define (identity x) x)

(define (accumulate combiner start n term)
    (define (helper i prefix)
        (if (> i n)
            prefix
            (helper (+ i 1) (combiner prefix (term i)))
        )
    )
    (helper 1 start)
)

(define (accumulate-tail combiner start n term)
    (define (helper i prefix)
        (if (> i n)
            prefix
            (helper (+ i 1) (combiner prefix (term i)))
        )
    )
    (helper 1 start)
)

(define-macro
 (list-of map-expr for var in lst if filter-expr)
 `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)
