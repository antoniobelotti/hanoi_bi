#lang racket

(define (hanoi n source destination tmp)
  (cond
    ((= n 1) (write (string-append source " --> " destination)) (newline))
    (else (hanoi (- n 1) source tmp destination)
          (hanoi 1 source destination tmp)
          (hanoi (- n 1) tmp destination source))))

(define (merge n source destination tmp)
  (cond
    ((= n 1)  (hanoi 1 source destination tmp))          
    (else (merge (- n 1) destination source tmp)
          (hanoi (+ n (- n 1)) source destination tmp))))

(define (hanoiBicolorMergedTowers n source destination tmp)
  (cond
    ((= n 1) (hanoi n source destination tmp))
    (else (hanoi n source destination tmp)
          (hanoiBicolorMergedTowers (- n 1) destination source tmp))))

(define (generate-moves n source1 source2 tmp)
  (merge n source2 source1 tmp) (hanoiBicolorMergedTowers (* n 2) source1 source2 tmp))
