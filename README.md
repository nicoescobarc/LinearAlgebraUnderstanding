# LinearAlgebraUnderstanding

This repository contains a bunch of scripts mainly focused on understanding numerical linear algebra concepts and algorithms.

## Goals and thoughts
I wrote the scripts to help myself to understand concepts and develop intuition; consequently, they are not intended to be efficient in terms of storage or operations involving zeros, as I always work with full matrices. However, they are supposed to depict the ideas behind some of the efficient algorithms to actually compute things, so I would like to believe that they are not written with a fully naive approach either.

## What will you find here?
So far, unless this readme isn't up to date (which, I must admit, is a possibility), you can find the following:
* A script that uses householder transformations to compute a Hessenberg matrix that is similar to the original matrix A.
* A script that uses householder transformations to get the QR decomposition of a matrix (this could be more efficient if the matrix is a Hessenberg one, this code simply illustrates the method).
* A script that uses QR decomposition for the purpose of computing the eigenvalues of a matrix using the QR iteration.
* This README :)
