(define (factorial x)
    (if (= x 1)
        1
        (* x (factorial (- x 1)))
    )
)

(define (fib x)
    (if (= x 1)
        1
        (if (= x 2)
            1
            (+ (fib (- x 1)) (fib (- x 2)))
        )
    )
)


(define (my-append a b)
    (if (null? a)
        b
        (cons (car a) (my-append (cdr a) b))
    )
)

(define (insert element lst index)
    (if (= index 0)
        (cons element lst)
        (cons (car lst) (insert element (cdr lst) (- index 1)))
    )
)

(define (duplicate lst)
    (if (null? lst)
        nil
        (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
    )
)