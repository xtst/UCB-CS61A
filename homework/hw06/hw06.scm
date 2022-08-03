(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (ascending? lst) 
(cond
    ((null? (cdr lst)) #t)
    ((null? lst) #t)
    ((<= (car lst) (cadr lst) ) (ascending? (cdr lst)))
    (else #f)
))

(define (interleave lst1 lst2)

    (if (null? lst1) lst2
    (if (null? lst2) lst1 (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2))))
)))

(define (my-filter func lst) 'YOUR-CODE-HERE)

(define (no-repeats lst) 'YOUR-CODE-HERE)
